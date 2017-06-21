#!/bin/env python3


import nsfg

def rprint(s):
    print(repr(s))



preg = nsfg.ReadFemPreg()
rprint(preg.head())
rprint(preg.columns)
rprint(preg.columns[1])
pregordr = preg['pregordr']
rprint(type(pregordr))
rprint(pregordr)
rprint(pregordr[0])
rprint(pregordr[2:5])
pregordr = preg.pregordr
rprint(preg.outcome.value_counts().sort_index())
rprint(preg.birthwgt_lb.value_counts().sort_index())
rprint(preg.birthord.value_counts().sort_index())
print('nan: ' + repr(preg.birthord.isnull().sum()))
rprint(preg.prglngth.value_counts().sort_index())
rprint(preg.totalwgt_lb.mean())
preg['totalwgt_kg'] = preg.totalwgt_lb * 0.453592
rprint('totalwgt_kg mean: ' + repr(preg['totalwgt_kg'].mean()))
# 1 lb = 0.453592 kg
resp = nsfg.ReadFemResp()
rprint(resp.head())
resp['age_r'].value_counts().sort_index()
rprint(resp[resp.caseid==2298])
rprint(preg[preg.caseid==2298])
rprint(resp.age_r[resp.caseid==1])
rprint(preg['prglngth'][preg.caseid==2298])
rprint(preg['birthwgt_lb'][preg.caseid==5012])
rprint(preg[preg.caseid==5012].birthwgt_lb)
rprint(preg[preg.caseid==5012]['birthwgt_lb'])
