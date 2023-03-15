import csv
import json
res= {"type": "FeatureCollection", "features": []}
f = open('data.csv', newline='')
reader = csv.DictReader(f)
for line in reader:
    coordsSplit = line["Section_Coordinates"].split(',')
    coords = [[float(coordsSplit[i]), float(coordsSplit[i+1])] for i in range(0,len(coordsSplit) -1, 2)]
    feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": coords[-1]}, "properties": {"Location": line["Trip_Arrival_Display_Name"], "Date": line["Trip_End_Date"]}}
    res["features"].append(feature)
    feature = {"type": "Feature", "geometry": {"type": "Point", "coordinates": coords[0]}, "properties": {"Location": line["Trip_Start_Display_Name"], "Date": line["Trip_Start_Date"]}}
    res["features"].append(feature)
    feature = {"type": "Feature", "geometry": {"type": "LineString", "coordinates": coords}}
    res["features"].append(feature)
f.close()
out = json.dumps(res)
f2 = open('out.geojson', 'w')
f2.write(out)
