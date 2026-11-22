"""Produces exact numerical certificate, cross-checking two independent enumerators."""
from itertools import combinations
import json
from direct_walk import calc
from peeling_certificate import census

def publicize(x):
  return {k:v for k,v in x.items() if k not in ('k','B')}
rows=[]
for k in range(4):
    for subset in combinations((2,4,11),k):
        direct=calc(subset)
        mask=sum(1<<(i-1) for i in subset)
        peeled=census(mask)
        assert publicize(direct)==peeled,(subset,direct,peeled)
        rows.append({'biased_vertices':list(subset),'result':peeled})
obj={'graph':'Herschel graph, vertices 1..11, edge list in scripts/peeling_certificate.py',
     'update':'Neighbor-majority, incumbent tie except vertices specified, where ties become one',
     'initial_state_count':2048,
     'all_bias_subsets':[{'size':x['biased_vertices'].__len__(),'vertices':x['biased_vertices'],**x['result']} for x in rows],
     'cross_validation':'Complete direct orbit walk and independent functional-graph indegree peeling agree for all 8 bias subsets',
     'all_orbits_have_period_1_or_2':True}
with open('certificates/census.json','w') as f:json.dump(obj,f,indent=2);f.write('\n')
print('PASS: 16,384 full initial-state trajectories certified twice; 8 intervention subsets')
