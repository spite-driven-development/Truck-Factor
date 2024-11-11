#!/usr/bin/env python3
import csv
import json

filename = 'output.csv'

with open(filename, 'r') as fh:
    json_array = []
    csv_reader = csv.DictReader(fh)
    for row in csv_reader:
        json_array.append(row)

with open('original_results.json', 'w') as fh:
    json_string = json.dumps(json_array, indent=4)
    fh.write(json_string)
