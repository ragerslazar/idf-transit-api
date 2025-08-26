from api.v1.models.MetroModel import MetroModel

class MetroController:
    def __init__(self):
        self.metro_model = MetroModel()

    def getAllMetrosController(self):
        return self.metro_model.getAllMetroModel()

    def getAllStationsController(self):
        return self.metro_model.getAllStationsModel()

    def getStationsByLineController(self, metro_line):
        line_info = self.metro_model.getStationsByLineModel(metro_line)
        if line_info["data"]["stations"]["count"] == 0:
            return None
        return line_info

    def getLinesByStationController(self, station):
        lines_by_station = self.metro_model.getLinesByStationModel(station)
        if lines_by_station["data"]["station"]["lines"]["count"] == 0:
            return None
        return lines_by_station
