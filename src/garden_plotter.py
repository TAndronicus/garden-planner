import matplotlib.pyplot as plt


def plot_garden(garden):
    col_n = 0
    for row in garden.beds:
        row_n = 0
        for bed in row:
            for bed_part in bed.bed_parts:
                x_min, x_max = row_n + bed_part.x_min, row_n + bed_part.x_max
                y_min, y_max = col_n + bed_part.y_min, col_n + bed_part.y_max
                plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='k')
                plt.text((x_min + x_max) / 2, (y_min + y_max) / 2, bed_part.plant_id, color='k',
                         horizontalalignment='center', verticalalignment='center')
            row_n += 1.5
        col_n += 1.5
    plt.show()
