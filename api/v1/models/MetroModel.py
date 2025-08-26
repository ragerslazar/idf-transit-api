import json
import os

class MetroModel:
    def __init__(self):
        self.data = None

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(base_dir, '../../../data.json'))

        try:
            with open(file_path, 'r') as f:
                self.data = json.load(f)
            print("JSON data loaded successfully:")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{file_path}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def getAllMetroModel(self):
        lines = sorted({station.get("res_com") for station in self.data})
        return {
            "data": {
                "metro_lines": {
                    "count": len(lines),
                    "names": lines
                }
            }
        }

    def getAllStationsModel(self):
        stations = sorted({station.get("nom_gares") for station in self.data})
        return {
            "data": {
                "stations": {
                    "count": len(stations),
                    "names": stations
                }
            }
        }

    def getStationsByLineModel(self, metro_line):
        stations = []
        locations = []
        operator = None
        img = self.getLineImg(metro_line)

        for station in self.data:
            if station.get("indice_lig") == metro_line:
                stations.append(station.get("nom_gares"))
                loc = station.get("geo_point_2d")
                locations.append({"lat": loc.get("lat"), "lon": loc.get("lon")})
                operator = station.get("exploitant")

        stations = sorted(stations)

        return {
            "data": {
                "metro_line": metro_line,
                "img": img,
                "operator": operator,
                "stations": {
                    "count": len(stations),
                    "names": stations,
                    "locations": locations
                }
            }
        }

    def getLinesByStationModel(self, _station):
        lines = []
        locations = []
        picto = []
        operator = None
        station_name = None

        for station in self.data:
            if station.get("id_ref_zdc") == _station:
                lines.append(station.get("res_com"))
                loc = station.get("geo_point_2d")
                locations.append({"lat": loc.get("lat"), "lon": loc.get("lon")})
                operator = station.get("exploitant")
                picto.append(station["picto"]["url"])
                station_name = station.get("nom_gares")

        return {
            "data": {
                "station": {
                    "name": station_name,
                    "location": locations,
                    "operator": operator,
                    "lines": {
                        "count": len(lines),
                        "names": lines,
                        "picto": picto
                    }
                }
            }
        }

    def getStationNameByCode(self, code):
        name = next((station.get("nom_gares") for station in self.data if station.get("id_ref_zdc") == code), None)
        return {
            "data": {
                "station": {
                    "code": code,
                    "name": name
                }
            }
        }

    def getLineImg(self, line):
        return next((station.get("picto").get("url") for station in self.data if station.get("indice_lig") == line), None)