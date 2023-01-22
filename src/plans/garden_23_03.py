from ..domain.garden import Garden
from ..domain.bed import Bed
from ..domain.bed_part import BedPart

from ..plants import Plants

garden = Garden([
    [
        Bed([
            BedPart(0, 1, 0, 1, Plants.POTATOES)
        ]),
        Bed([
            BedPart(0, .5, 0, 1, Plants.POTATOES),
            BedPart(.5, 1, 0, 1, Plants.POTATOES)
        ])
    ],
    [
        Bed([
            BedPart(0, .5, 0, 1, Plants.POTATOES),
            BedPart(.5, 1, 0, 1, Plants.CARROTS)
        ]),
        Bed([
            BedPart(0, .5, 0, .5, Plants.TOMATOES),
            BedPart(0, .5, .5, 1, Plants.POTATOES),
            BedPart(.5, 1, 0, .5, Plants.POTATOES),
            BedPart(.5, 1, .5, 1, Plants.TOMATOES)
        ])
    ]
])
