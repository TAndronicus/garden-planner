import matplotlib.pyplot as plt

from garden_calculator import calculate_amount


def plot_garden(garden):
    col_n = 0
    for row in garden.beds:
        row_n = 0
        for bed in row:
            for bed_part in bed.bed_parts:
                x_min, x_max, y_min, y_max = calculate_coordinates(col_n, row_n, bed_part)
                plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='k')
                plt.text((x_min + x_max) / 2, (y_min + y_max) / 2, bed_part.plant.name, color='k',
                         horizontalalignment='center', verticalalignment='center')
            row_n += 1.5
        col_n += 1.5
    plt.show()


def plot_rotations(prev_garden, next_garden, title=None):
    col_n = 0
    for i in range(min(len(prev_garden.beds), len(next_garden.beds))):
        row_n = 0
        prev_row, next_row = prev_garden.beds[i], next_garden.beds[i]
        for j in range(min(len(prev_row), len(next_row))):
            prev_bed, next_bed = prev_row[j], next_row[j]
            for k in range(min(len(prev_bed.bed_parts), len(next_bed.bed_parts))):
                prev_bed_part, next_bed_part = prev_bed.bed_parts[k], next_bed.bed_parts[k]
                x_max, x_min, y_max, y_min = calculate_coordinates(col_n, row_n, prev_bed_part)
                plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='k')
                if prev_bed_part.plant.group == next_bed_part.plant.group:
                    plt.fill([x_min, x_max, x_max, x_min], [y_min, y_min, y_max, y_max], color='r')
                    plt.text((x_min + x_max) / 2, (y_min + y_max) / 2,
                             prev_bed_part.plant.name + ' /\n' + next_bed_part.plant.name, color='k',
                             horizontalalignment='center', verticalalignment='center')
            row_n += 1.5
        col_n += 1.5
    if title is not None:
        plt.title(title)
    plt.show()


def plot_calendar(garden):
    names = []
    for row in garden.beds:
        for bed in row:
            for bed_part in bed.bed_parts:
                plant = bed_part.plant
                plt.plot([plant.sow_start, plant.sow_end + 1], [plant.name, plant.name], color='g')
                plt.plot([plant.harvest_start, plant.harvest_end + 1], [plant.name, plant.name], color='r')
                names.append(plant.name)
    plt.yticks(names)
    plt.show()


def plot_garden_detailed(garden):
    col_n = 0
    plt.figure(figsize=(10, 10))
    for row in garden.beds:
        row_n = 0
        for bed in row:
            for bed_part in bed.bed_parts:
                x_min, x_max, y_min, y_max = calculate_coordinates(col_n, row_n, bed_part)
                plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='k')
                amount = calculate_amount(bed_part.plant.radius, x_max - x_min, y_max - y_min)
                plt.text((x_min + x_max) / 2, (y_min + y_max) / 2,
                         bed_part.plant.name + '\n' + str(amount) + f' (r = {bed_part.plant.radius})', color='k',
                         horizontalalignment='center', verticalalignment='center')
            row_n += 1.5
        col_n += 1.5
    plt.show()


def calculate_coordinates(col_n, row_n, bed_part):
    x_min, x_max = row_n + bed_part.x_min, row_n + bed_part.x_max
    y_min, y_max = col_n + bed_part.y_min, col_n + bed_part.y_max
    return x_min, x_max, y_min, y_max

