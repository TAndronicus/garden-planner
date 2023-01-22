class Plant:
    def __init__(self, plant_id, name,
                 sow_start, sow_end,
                 harvest_start, harvest_end,
                 group, radius):
        self.id = plant_id
        self.name = name
        self.sow_start = sow_start
        self.sow_end = sow_end
        self.harvest_start = harvest_start
        self.harvest_end = harvest_end
        self.group = group
        self.radius = radius
