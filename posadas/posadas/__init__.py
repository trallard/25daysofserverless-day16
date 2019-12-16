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
    loc_path = Path("./posadas/data/locations.json").resolve()
    with open(loc_path, "r") as json_file:
        locations = json.load(json_file)
    return locations.get("locations")


def get_loc(day, locations):
    for posada in locations:
        date = datetime.datetime.strptime(posada.get("date"), "%B %d, %Y").date()
        if date.day == int(day):
            return posada
