# Core
from app.api import api
from flask import jsonify
from flask.ext.cors import cross_origin
# Models
from app.models.location import Location


@cross_origin()
@api.route('/locations', methods=['GET'])
def get_locations():
    """
    :return: Return a list with all locations
    """
    # Get all movies from DB
    locations = Location.query.all()

    result = []
    for location in locations:
        result.append(location.get_information())

    return jsonify(locations=result)
