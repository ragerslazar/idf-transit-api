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
        stations = set()
        for station in self.data:
            stations.add(station.get("res_com"))

        return {"metro_lines": list(stations)}

    def getAllStationsModel(self):
        stations = set()
        for station in self.data:
            stations.add(station.get("nom_gares"))

        return {"data": {
            "stations": {
                "count": len(stations),
                "name": sorted(stations)
            }
        }}

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
            "metro_line": metro_line,
            "img": img,
            "operator": operator,
            "data": {
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
            "station": station_name,
            "location": locations,
            "operator": operator,
            "data": {
                "lines": {
                    "count": len(lines),
                    "names": lines,
                    "picto": picto
                }
            }
            }

    def getStationNameByCode(self, code):
        return next((station.get("nom_gares") for station in self.data if station.get("id_ref_zdc") == code), None)

    def getLineImg(self, line):
        return next((station.get("picto").get("url") for station in self.data if station.get("indice_lig") == line), None)