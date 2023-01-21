from garden_plotter import plot_garden, plot_rotations, plot_calendar
import garden_23_05
import garden_23_08

prev_garden = garden_23_05.garden
next_garden = garden_23_08.garden


plot_garden(prev_garden)
plot_rotations(prev_garden, next_garden)
plot_calendar(prev_garden)
