from domain.plant import Plant
from domain.plant_group import PlantGroup


class Plants:
    TOMATOES = Plant(1, "Tomatoes", 4, 6, 7, 9, PlantGroup.GR1)
    POTATOES = Plant(2, "Potatoes", 4, 6, 7, 9, PlantGroup.GR1)
    BASIL = Plant(3, "Basil", 4, 6, 7, 9, PlantGroup.GR2)
    ZUCCHINI = Plant(4, "Zucchini", 4, 6, 7, 9, PlantGroup.GR2)
    SQUASH = Plant(5, "Squash", 4, 6, 7, 9, PlantGroup.GR2)
    CARROTS = Plant(6, "Carrots", 4, 6, 7, 9, PlantGroup.GR2)
    THYME = Plant(7, "Thyme", 4, 6, 7, 9, PlantGroup.GR2)
    OREGANO = Plant(8, "Oregano", 4, 6, 7, 9, PlantGroup.GR2)
    ROSEMARY = Plant(8, "Rosemary", 4, 6, 7, 9, PlantGroup.GR2)


def get_plants_map(garden):
    res = {}
    for row in garden.beds:
        for bed in row:
            for bed_part in bed.bed_parts:
                res[bed_part.plant.name] = bed_part.plant
    return res