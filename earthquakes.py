"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""

# 1
import json

infile = open("eq_data.json", "r")
earthquake_dict = json.load(infile)
earthquake_list = earthquake_dict["features"]

print(len(earthquake_list))
print()
print()

# 2

eq_dict = {}
for earthquake in earthquake_list:
    if earthquake["properties"]["mag"] > 6:
        location = earthquake["properties"]["place"]
        magnitude = earthquake["properties"]["mag"]
        latitude = earthquake["geometry"]["coordinates"][0]
        longitude = earthquake["geometry"]["coordinates"][1]
        eq_dict[location] = {
            "Magnitude": magnitude,
            "Latitude": latitude,
            "Longitude": longitude,
        }
print(eq_dict)
print()
print()

# 3
for k, v in eq_dict.items():
    print(f"Location: ", k)
    print(f"Magnitude: " + str(v["Magnitude"]))
    print(f"Longitude: " + str(v["Longitude"]))
    print(f"Latitude: " + str(v["Latitude"]))
    print()
    print()
