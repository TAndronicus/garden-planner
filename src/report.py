from garden_plotter import plot_garden, plot_rotations, plot_calendar
from src.plans import garden_23_03, garden_23_07

prev_gardens = {
    '23.03': garden_23_03.garden
}
current_garden = garden_23_07.garden


plot_garden(current_garden)
for date, prev_garden in prev_gardens.items():
    plot_rotations(prev_garden, current_garden, date)
plot_calendar(current_garden)
