# Guide to updating the data:

> Never change rattraps_position.csv directly. Instead, modify `ratraps.csv`
    and run `join_location_trap.py`.

## Running `join_location_trap.py`

1. Ensure you have at least python 3.7 installed. You can install python from here https://www.python.org/downloads/. You can verify the version of python which is installed by running the command

        python --version
2. Ensure requirements are installed (you only need to do this once). Run the following command.

        pip install requirements.txt

3. Run the program.

        python join_location_trap.py

    This will generate a new file `data/rattraps_position.csv`, containing the trap data and their position. You can do this every time you change the rattraps.csv file to get up to date data.

> Note: On Linux/MacOS you may need to run python3 and pip3 instead of python and pip.

## Output

The output file latitudes/longitudes are in the EPSG:4326 projection.

They can be imported into the QGIS project (make sure you set the CRS to EPSG:4326) via `Layer -> Add Layer -> Add Delimited Text Layer`.

The data should look something like this:

![Output](images/traps-topo.png)

or

![Output](images/traps-osm.png)

Depending on whether OpenStreetMaps or LINZ is the base layer.