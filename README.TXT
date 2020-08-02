Very simple script for parsing Garmin files from Strava to ShapeFile.

Supports GPX, TCX, and FIT files.

Usage: Put into the same folder as your unzipped stava data and run. Python3. Only works on Garmin file types, GPX, FIT, and TCX. Has some requirements.

Like:

fitparse
ogr
osr


python3 -m pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`
python3 -m pip install ogr
python3 -m pip install fitparse
