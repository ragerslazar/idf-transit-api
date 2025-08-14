from flask import Blueprint, jsonify
from api.v1.controllers.MetroController import MetroController

metro_routes = Blueprint("metro_routes", __name__)
metro_controller = MetroController()

@metro_routes.route("/lines", methods=["GET"])
def get_all_metro_lines():
    return jsonify(metro_controller.getAllMetrosController()), 200


@metro_routes.route("/lines/<string:metro_line>", methods=["GET"])
def get_station_by_line(metro_line):
    _get_station_by_line = metro_controller.getStationsByLineController(metro_line)
    if _get_station_by_line:
        return jsonify(_get_station_by_line), 200

    return jsonify({"status": "error",
                    "message": "provided metro line is unknown"}), 404

@metro_routes.route("/stations", methods=["GET"])
def get_all_stations():
    return jsonify(metro_controller.getAllStationsController()), 200

@metro_routes.route("/stations/<int:station>/lines", methods=["GET"])
def get_lines_by_station(station):
    _get_lines_by_station = metro_controller.getLinesByStationController(station)
    if _get_lines_by_station:
        return jsonify(_get_lines_by_station), 200

    return jsonify({"status": "error",
                    "message": "Unknown station"}), 404
