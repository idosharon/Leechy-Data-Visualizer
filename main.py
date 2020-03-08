#  Copyright (c) 2020 Ido Sharon.
#  This Software created for leechy by Ido Sharon.

import matplotlib.pyplot as plt
import os
import pandas as pd

folder = "data/meas/"
files = os.listdir(folder)
files.sort()

colors = ["black", "fuchsia", "blue", "sienna", "yellow", "green", "brown", "grey", "orange", "darkorchid", "darkcyan",
          "red", "#c91414"]
counter = 0

comparison = []
const = 1182.69

for file in files:

    file = open(folder + file, "r", encoding="ISO-8859-1")
    name = file.name[10:].replace(".txt", "").split("_")

    print(f"{name[1]} {name[-1]}%")

    data = file.readlines()[17:529]
    data = [value.replace("\n", "").split("\t") for value in data]

    points_data = [[float(number) for number in value] for value in data]

    print(points_data)
    x_values = []
    y_values = []

    [x_values.append(point[0]) for point in points_data]
    [y_values.append(point[1]) for point in points_data]

    plt.figure(num="leechy | data from " + folder)
    plt.plot(x_values, y_values, "--" if name[1] == "water" else "-",
             label="water" if name[1] == "water" else f"{name[1]} {name[-1]}%", color=colors[counter])
    plt.ylabel('OD value')
    plt.xlabel('wave length')
    plt.legend()

    plt.figure(num="leechy | comparison")
    plt.plot([val[0].replace(name[1], "") for val in comparison], [val[-1] for val in comparison], "-", color="red")
    plt.ylabel(f'OD value at - x={str(const)}')
    plt.xlabel(f'precents of {name[1]}')

    comparison.append(["water" if name[1] == "water" else f"{name[1]} {name[-1]}%", y_values[x_values.index(const)]])

    counter += 1


def last(elem):
    return elem[-1]


comparison = sorted(comparison, key=last)
comparison = {f'{name[1]} percent: ': [percent[0].replace(name[1], "") for percent in comparison],
              'OD value: ': [val[-1] for val in comparison]}
print(pd.DataFrame(data=comparison, index=files))

plt.show()
