from domain.garden import Garden
from domain.bed import Bed
from domain.bed_part import BedPart

from garden_plotter import plot_garden

garden = Garden([
    [
        Bed([
            BedPart(0, 1, 0, 1, "Tomatoes")
        ]),
        Bed([
            BedPart(0, .5, 0, 1, "Zucchini"),
            BedPart(.5, 1, 0, 1, "Squash")
        ])
    ],
    [
        Bed([
            BedPart(0, .5, 0, 1, "Carrots"),
            BedPart(.5, 1, 0, 1, "Potatoes")
        ]),
        Bed([
            BedPart(0, .5, 0, .5, "Thyme"),
            BedPart(0, .5, .5, 1, "Basil"),
            BedPart(.5, 1, 0, .5, "Oregano"),
            BedPart(.5, 1, .5, 1, "Rosemary")
        ])
    ]
])

plot_garden(garden)
