from ..domain.garden import Garden
from ..domain.bed import Bed
from ..domain.bed_part import BedPart

from ..plants import Plants

garden = Garden([
    [
        Bed([
            BedPart(0, 1, 0, 1, Plants.TOMATOES)
        ]),
        Bed([
            BedPart(0, .5, 0, 1, Plants.ZUCCHINI),
            BedPart(.5, 1, 0, 1, Plants.SQUASH)
        ])
    ],
    [
        Bed([
            BedPart(0, .5, 0, 1, Plants.CARROTS),
            BedPart(.5, 1, 0, 1, Plants.POTATOES)
        ]),
        Bed([
            BedPart(0, .5, 0, .5, Plants.THYME),
            BedPart(0, .5, .5, 1, Plants.BASIL),
            BedPart(.5, 1, 0, .5, Plants.OREGANO),
            BedPart(.5, 1, .5, 1, Plants.ROSEMARY)
        ])
    ]
])
