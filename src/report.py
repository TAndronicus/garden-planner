from garden_plotter import plot_garden, plot_rotations, plot_calendar
import garden_23_07
import garden_23_03

prev_gardens = [
    garden_23_03.garden
]
current_garden = garden_23_07.garden


plot_garden(current_garden)
for prev_garden in prev_gardens:
    plot_rotations(prev_garden, current_garden)
plot_calendar(current_garden)
