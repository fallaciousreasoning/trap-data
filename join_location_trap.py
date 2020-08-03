TRAPS_FILE="data/rattraps.csv"
GPX_FILE="data/gps_waypoints.gpx"

TRAPS_ID="Trap.ID"
GPX_TRACK_NAME="Holly Craigie traps GPS waypoints 8June20 waypoints"

import gpxpy

gpx_data = gpxpy.parse(open(GPX_FILE, 'r'))

for waypoint in gpx_data.waypoints:
    print(waypoint.name)
# track = get_track(gpx_data)
# print(track)