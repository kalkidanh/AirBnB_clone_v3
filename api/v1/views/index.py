#!/usr/bin/python3
"""Imports app_views from api.v1.views"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """Return JSON status"""
    return jsonify({'status': 'OK'})
