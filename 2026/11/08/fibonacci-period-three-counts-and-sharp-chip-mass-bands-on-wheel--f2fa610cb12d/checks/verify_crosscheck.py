#!/usr/bin/env python3
"""Exact mass-by-mass reconciliation between independent update and phase methods."""
import json
from verify_direct import run
from verify_transfer import word_mass

rows=[]
for n in range(3,7):
    direct=run(n)
    _,_,mass,_=word_mass(n)
    assert direct['mass_counts']==sorted(mass.items()), (n,'mass discrepancy')
    rows.append({'n':n,'candidate_states':direct['states_checked'],'period_three':direct['period_three'],'mass_coefficients_matched':len(mass)})
print(json.dumps({'status':'PASS','method':'complete mass-by-mass comparison of separate exact algorithms','cases':rows},separators=(',',':'),sort_keys=True))
