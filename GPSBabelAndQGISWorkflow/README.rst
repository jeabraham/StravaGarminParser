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

1. move_file:  the filename and group name for the file, e.g. the original .fit filename, e.g. `Move_2018_07_14_12_11_57_Cycling`
2. gpx_file:   the full relative path to the gpx file, e.g. `../../SuuntoExport/moves_gpx/Move_2018_07_14_12_11_57_Cycling.fit.gpx`
3. points_id:   a unique ID for the track points
4. track_id: a unique ID for the track view

I deleted the extent information, to see if it would regenerate.

Python templating
^^^^^^^^^^^^^^^^^

The program make_qlr.py will apply the jinja2 template to a gpx file

So, you can

  `` for file in *.gpx; do python3 make_qlr.py $file; done ``

Project Setup
=============

Of course we have to deal with The Python Problem of conflicting installs and using a
virtual environment to manage it.

	```
	# TODO Ask harley how to use VEs to solve The Python Problem
	```
