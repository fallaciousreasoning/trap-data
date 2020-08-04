TRAPS_FILE="data/rattraps.csv"
GPX_FILE="data/gps_waypoints.gpx"

TRAPS_ID="Trap.ID"
GPX_TRACK_NAME="Holly Craigie traps GPS waypoints 8June20 waypoints"

import gpxpy
import csv

gpx_data = gpxpy.parse(open(GPX_FILE, 'r'))

def build_waypoint_dict(waypoints):
    result = {}
    for waypoint in waypoints:
        name = waypoint.name.upper().lstrip('0')

        if name[0] == "B":
            name = name[1:]
            if name in result:
                print(f"Encountered duplicate key {name} (one had that B prefix)")
                continue
        # Note: Some names have leading letters. However, removing them results
        # in duplicates, so not sure how to treat them yet :/
        result[name] = waypoint
    return result

def trap_id(row):
    trap_line = row[1]
    trap_id = row[2]

    return trap_id[len(trap_line):]

waypoints = build_waypoint_dict(gpx_data.waypoints)
print(waypoints.keys())
print(len(waypoints.keys()))

with open(TRAPS_FILE) as csv_file:
    reader = csv.reader(csv_file)
    for index, line in enumerate(reader):
        if index == 0: continue

        id = trap_id(line)
        if not id in waypoints:
            print("Couldn't find a waypoint for", id)
            continue
        # print(id, waypoints[id])
# track = get_track(gpx_data)
# print(track)