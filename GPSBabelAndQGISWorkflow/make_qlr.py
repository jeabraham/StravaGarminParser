import jinja2
import os, sys
import uuid

gpx_file = sys.argv[1]
print(gpx_file)
move_file_ext = os.path.basename(gpx_file)
move_file = os.path.splitext(move_file_ext)[0]
print(move_file_ext, move_file)
move_file = os.path.splitext(move_file)[0]
print(move_file)

points_id = uuid.uuid4()
line_id = uuid.uuid4()

print (points_id, line_id)

from jinja2 import Template
with open('QGISTrackPointsAndLine.template.qlr') as file_:
    template = Template(file_.read())

rendered = template.render(gpx_file = gpx_file,
    move_file = move_file,
    points_id = points_id,
    line_id = line_id,
)

qlr_file = os.path.splitext(gpx_file)[0] + ".qlr"

with open(qlr_file, "w") as fh:
    fh.write(rendered)
