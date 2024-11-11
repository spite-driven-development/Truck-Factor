#!/usr/bin/env python3

import glob
import json
import re

result_files = glob.glob('../gittruckfactor/results_linguist/*.txt')

records = {}

first_line_pattern = r'TF = (\d+) \(coverage = ([\d.]+)%\)'
contrib_pattern = r'([^;]+);(\d+);([\d.]+)'

for file in result_files:
    filename = file.split('/')[-1]
    result = {'developers': []}
    with open(file, 'r') as fh:
        for line in fh:
            # first line
            match = re.search(first_line_pattern, line)
            contrib_match = re.search(contrib_pattern, line)
            if match:
                result['tf'] = int(match.group(1))
                result['coverage'] = float(match.group(2))
            elif contrib_match:
                name = contrib_match.group(1)
                files = int(contrib_match.group(2))
                percentage = float(contrib_match.group(3))
                result['developers'].append({'name': name, 'file_count': files, 'percentage': percentage})
    records[filename] = result

with open('results_linguist.json', 'w') as fh:
    json.dump(records, fh, indent=2, sort_keys=True)
