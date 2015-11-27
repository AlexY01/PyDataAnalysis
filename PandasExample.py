__author__ = 'alexyuan'

from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])
obj.values
obj.index
obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
obj2
obj2['b']
obj2[1]
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj4 = Series(sdata)
States = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = Series(sdata, index=States)
obj3
pd.isnull(obj3)
pd.notnull(obj3)
obj3+obj4
obj3.name = 'Population'
obj3.index.name = 'State'
obj3
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
obj

data = {'State': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame
DataFrame(data, columns=['year', 'State', 'pop'])
frame2 = DataFrame(data, columns=['year', 'State', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.index
frame2.year
frame2.ix['three']
frame2.ix[2]
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2
frame2['eastern'] = frame2.State == 'Ohio'
frame2
del frame2['eastern']
frame2
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
frame3
frame3.T
DataFrame(pop, index=[2001, 2002, 2003])
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
DataFrame(pdata)
frame3.values
frame2.values