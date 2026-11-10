from flask import Blueprint, jsonify

maintenance_bp = Blueprint("maintenance", __name__)

@maintenance_bp.route("/maintenance_records", methods=["GET"])
def get_maintenance_records():
    return jsonify([]), 200