TRAPS_FILE="data/rattraps.csv"
OUTPUT_FILE="data/ratraps_position.csv"
GPX_FILE="data/gps_waypoints.gpx"

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
        # Note: Some names have leading letters. However, removing them results
        # in duplicates, so not sure how to treat them yet :/
        result[name] = waypoint
    return result

def trap_id(row):
    trap_line = row[1]
    trap_id = row[2]

    # The trap id is currently of the form "{trap_line}{trap_id}", so we strip
    # off however many characters are in trap_line from the start.
    # DTF100 --> 100
    return trap_id[len(trap_line):]

waypoints = build_waypoint_dict(gpx_data.waypoints)

input_csv = open(TRAPS_FILE)
ouput_csv = open(OUTPUT_FILE, 'w', newline='')

reader = csv.reader(input_csv)
writer = csv.writer(ouput_csv)

for index, line in enumerate(reader):
    if index == 0:
        # Write the new header row.
        writer.writerow([*line, 'sanitized_id', 'latitude', 'longitude', 'gps_elevation'])
        continue

    id = trap_id(line)
    if not id in waypoints:
        # We couldn't find a matching waypoint. Log it and carry on.
        print(f"Couldn't find a waypoint for trap #{id}")
        continue

    waypoint = waypoints[id]
    writer.writerow([*line,id,waypoint.latitude,waypoint.longitude,waypoint.elevation])
input_csv.close()
ouput_csv.close()

print(f"Wrote the new data to {OUTPUT_FILE}")