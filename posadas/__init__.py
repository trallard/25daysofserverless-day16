import datetime
import json
import logging
from pathlib import Path

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Someone is looking for a posada! ✨")

    day = req.params.get("day")
    if not day:
        locations = json_locations()
        return func.HttpResponse(f"{json.dumps(locations)}", status_code=200)

    if day:
        locations = json_locations()
        posada = get_loc(day, locations)
        return func.HttpResponse(f"{json.dumps(posada)}", status_code=200)
    else:
        return func.HttpResponse("Please pass a day", status_code=400)


def json_locations():
    """Function to parse the json file with the locations,
    we use Pathlib to resolve the full path of the file
    """
    loc_path = Path("/home/site/wwwroot/posadas/locations.json")
    with open(loc_path, "r") as json_file:
        locations = json.load(json_file)
    return locations.get("locations")


def get_loc(day, locations):
    """This function searches for the location corresponding to the 
    query day. 
    We need to make sure the dates are actually converted into datetime objs.
    """
    for posada in locations:
        date = datetime.datetime.strptime(posada.get("date"), "%B %d, %Y").date()
        if date.day == int(day):
            return posada
