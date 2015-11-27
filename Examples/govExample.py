__author__ = 'iseyjn'

import json
from collections import Counter
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
path = 'pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

counts=get_counts(time_zones)

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

counts=Counter(time_zones)

frame=DataFrame(records)
tz_counts=frame['tz'].value_counts()

clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='unknown'
tz_counts=clean_tz.value_counts()

results = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
print(indexer[:10])
#tz_counts[:10].plot(kind='barh', rot=0)
count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
plt.show()
