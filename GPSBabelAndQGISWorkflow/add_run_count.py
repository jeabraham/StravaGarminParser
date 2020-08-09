import sqlite3
import sys
import os

sqlite_file = sys.argv[1]

if len(sys.argv) > 2:
    sqlite_table = sys.argv[2]
else:
    sqlite_file_base = os.path.basename(sqlite_file)
    sqlite_table = os.path.splitext(sqlite_file_base)[0]
    sqlite_table = os.path.splitext(sqlite_table)[0].lower() # In case it's .this.that

conn = sqlite3.connect(sqlite_file)

runs = []
cur_run = 1
bottom_elevation = None
bottom_point = None
top_elevation = None
c = conn.cursor()
going_up = True
for row in c.execute(
    'SELECT track_seg_id, track_seg_point_id, ele FROM \'{}\' where ele is not null ORDER BY track_seg_id, track_seg_point_id '.format(
    sqlite_table)):
    if bottom_elevation is None:
        bottom_elevation =  row[2]
        top_elevation = row[2]
        bottom_point = (row[0],row[1])
        print("New bottom elevation is ",bottom_elevation)
        runs.append((cur_run, bottom_point))
    else:
        cur_elevation = row[2]
        #if cur_elevation is not None:
        print('{}{}-{},'.format('U' if going_up else 'D', row[1], cur_elevation), end = '')
        if cur_elevation - bottom_elevation > 25:
            if not going_up:
                cur_run = cur_run + 1
                runs.append((cur_run, bottom_point))
                print("\n***** Recording the new bottom of run {} at elevation {} point {} (recorded at {},{})".format(
                    cur_run, bottom_elevation, bottom_point, row[0], row[1]))
                going_up = True
                top_elevation = cur_elevation
        if top_elevation - cur_elevation > 25:
            if going_up:
                print ("\n*****Going down! at point {},{}".format(row[0],row[1]))
                bottom_elevation = cur_elevation
                going_up = False
        if not going_up and cur_elevation < bottom_elevation:
            bottom_elevation = cur_elevation
            bottom_point =  (row[0],row[1])
            print("b ", end = '')
            #print("New bottom point {} at elevation {}".format(bottom_point, bottom_elevation))
        if going_up and cur_elevation > top_elevation:
            #print("Getting higher! at point {},{} elevation {}".format(row[0], row[1], bottom_elevation))
            print("t ", end = '')
            top_elevation = cur_elevation
print(runs)
for run_val in runs:
    sql_cmd = "update '{}' set name = '{}' where track_seg_id >= {} and track_seg_point_id >= {}".format(
        sqlite_table, "Run {}".format(run_val[0]), run_val[1][0], run_val[1][1])
    print(sql_cmd)
    c.execute(sql_cmd)

conn.commit()
conn.close()
