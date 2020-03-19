#  Copyright (c) 2020 Ido Sharon.
#  This Software was created for leechy by Ido Sharon.

import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

folder = "data/meas/"
files = os.listdir(folder)
files.sort()

colors = ["black", "fuchsia", "blue", "sienna", "yellow", "green",
          "brown", "grey", "orange", "darkorchid", "darkcyan", "red",
          "#c91414", "purple", '#FF6633', '#FFB399', '#FFFF99', '#00B3E6',
          '#3366E6', '#999966', '#99FF99', '#B34D4D', '#80B300',
          '#E6B3B3', '#6680B3', '#66991A', '#FF99E6', '#FF33FF',
          '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC', '#66994D',
          '#B366CC', '#4D8000', '#B33300', '#CC80CC', '#809900',
          '#991AFF', '#E666FF', '#4DB3FF', '#1AB399', '#66664D',
          '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
          '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
          '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
          '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF']
counter = 0

comparison = []
const = 1182.69

plt.figure(num=f"Leechy | data folder= {folder}", figsize=(9.5, 8))
grid = plt.GridSpec(4, 3, wspace=1, hspace=1)

plt.subplot(grid[:3, :4])
for file in files:
    file = open(folder + file, "r")
    name = file.name[10:].replace(".txt", "").split("_")

    # print(f"{name[1]} {name[-1]}%")

    data = file.readlines()[17:529]
    data = [value.replace("\n", "").split("\t") for value in data]

    points_data = [[float(number) for number in value] for value in data]

    # print(points_data)
    x_values = []
    y_values = []

    [x_values.append(point[0]) for point in points_data]
    [y_values.append(point[1]) for point in points_data]

    plt.axis([const-7, const+7, 0.575, 0.72])

    plt.plot(x_values, y_values, ".--" if name[1] == "water" else ".-",
             label="water" if name[1] == "water" else f"{name[1]} {name[-1]}%", color=colors[counter])
    plt.ylabel('OD value')
    plt.xlabel('wave length')
    plt.legend()

    comparison.append(["water" if name[1] == "water" else f"{name[1]} {name[-1]}%", y_values[x_values.index(const)]])

    counter += 1


def last(elem):
    return elem[-1]


plt.subplot(grid[3, :4])
plt.plot([val[0].replace(name[1], "") for val in comparison], [val[-1] for val in comparison], "o--",
         color="#c91414")
plt.ylabel(f'OD value at - x={str(const)}')
plt.xlabel(f'Percents of {name[1]}')

comparison = sorted(comparison, key=last)

print(pd.DataFrame(data={f'Percents: ': [val[0] for val in comparison], 'OD value: ': [val[-1] for val in comparison]},
                   index=files))

print("Average: ", np.average([float(val[-1]) for val in comparison]))

plt.show()
