#!/usr/bin/env python
import glob
import pandas
import pandas.io.json
import json


def fix_frame(filename, columns):
    frame = pandas.DataFrame.from_csv(filename, index_col=False)
    frame.columns = columns
    data = frame.to_dict()
    for key in data:
        data[key] = [data[key][k] for k in data[key]]
    json_filename = filename.replace('.csv', '.json')
    json_data = json.dumps(data)
    with open(json_filename, 'w+') as out:
        out.write(json_data)


highfreqs = [f for f in glob.glob('sixify_*_*.csv')]
# print highfreqs

# fix_frame('sixify_aggregation_btcusd.csv',
#           ['amount', 'price', 'date'])


for filename in highfreqs:
    print filename
    fix_frame(filename,
              ['price', 'amount', 'date'])
