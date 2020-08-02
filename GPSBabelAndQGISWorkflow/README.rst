To get SUUNTO data into QGIS
============================


Download all your data
----------------------

Suunto MovesCount website allows you to prepare a zip file of all your data, and download it



Convert to GPX
--------------


.fit files are ANT / GARMIN files showing your "moves", (exercises).  GPSBabel can process
them

	``for file in *.fit; do /Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel -i garmin_fit -f $file -o gpx -F ../moves_gpx/$file.gpx; done``

Import them into QGIS
---------------------

I prefer to have the points and line for the GPX file inside of the GIS, so I created
a layer definition file `QGISTrackPointsAndLine.qml` for this.

I've templated it as `QGISTrackPointsAndLine.template.qml` with the following jinja2
fields

1. move_file:  the filename
