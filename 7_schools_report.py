"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

# taking a json file and turning it into a list
import json

infile = open("school_data.json", "r")

schools = json.load(infile)
conference_schools = [372, 108, 107, 130]

print(type(schools))

# How many schools are in this file?
print(len(schools))


# name of school, in state living, graduation rate, which schools have above 80%
for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if school["Graduation rate  women (DRVGR2020)"] > 80:
            print(school["instnm"])
            print(school["Graduation rate  women (DRVGR2020)"])
            print()
            print()
