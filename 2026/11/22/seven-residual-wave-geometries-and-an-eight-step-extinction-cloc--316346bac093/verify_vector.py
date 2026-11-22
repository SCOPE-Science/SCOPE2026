"""Independent whole-space vector-iterate census; requires Python 3 and NumPy."""
from collections import Counter
import csv
from pathlib import Path
import numpy as np
N = 3**12
adj = [tuple(int(z) for z in line.split()) for line in Path('adjacency.txt').read_text().splitlines()]
assert len(adj)==12 and all(len(row)==5 for row in adj)
powers = 3**np.arange(12,dtype=np.int64)
ids=np.arange(N,dtype=np.int64)
x=(ids[:,None]//powers[None,:])%3
# Independent vector formulation: all 12 sites' Boolean contacts at once.
y=np.where(x==1,2,0)
for v in range(12):
    excited=np.count_nonzero(x[:,adj[v]]==1,axis=1)
    y[:,v]=np.where((x[:,v]==0)&(excited>=2),1,y[:,v])
f=np.sum(y*powers[None,:],axis=1,dtype=np.int64)
iterates=[ids]
for t in range(11):iterates.append(f[iterates[-1]])
assert np.array_equal(iterates[8],iterates[11])
assert not np.array_equal(iterates[7],iterates[10])
entry=np.full(N,-1,dtype=np.int8)
per=np.full(N,0,dtype=np.int8)
for t in range(9):
    first=(entry<0)&(iterates[t]==iterates[t+3])
    entry[first]=t
    per[first]=np.where(iterates[t][first]==iterates[t+1][first],1,3)
assert (entry>=0).all()
counts=Counter(zip(entry.tolist(),per.tolist()))
print('states',N)
print('fixed_orbits',1)
periodic3=ids[(entry==0)&(per==3)]
assert len(periodic3)%3==0
print('three_orbits',len(periodic3)//3)
print('fixed_basin',int(np.count_nonzero(per==1)))
print('three_basin_total',int(np.count_nonzero(per==3)))
print('entry_period_counts:')
for k,v in sorted(counts.items()):print(f'{k[0]},{k[1]}:{v}')
print('max_entry',int(entry.max()),'states_at_max',int(np.count_nonzero(entry==entry.max())))
root=np.minimum(np.minimum(iterates[8],iterates[9]),iterates[10])
roots=np.unique(np.minimum(np.minimum(periodic3,f[periodic3]),f[f[periodic3]]))
assert len(roots)==200
basins=Counter(root[per==3].tolist())
assert set(basins)==set(roots)
print('three_basin_histogram',sorted(Counter(basins.values()).items()))
# Independent local successor-phase count and full rotation of all period-three vertices.
neighbor_cond=np.ones(N,dtype=bool)
for v in range(12):
    c=np.count_nonzero(x[:,adj[v]]==((x[:,v]+1)%3)[:,None],axis=1)
    neighbor_cond&=(c>=2)
assert np.array_equal(np.flatnonzero(neighbor_cond),periodic3)
assert np.array_equal(y[periodic3],((x[periodic3]+1)%3))
print('phase_constraint_states',int(neighbor_cond.sum()))
print('witness_code',2824,'first_periodic_entry',int(entry[2824]))
with open('vector_roots.csv','w',newline='') as fh:
    w=csv.writer(fh,lineterminator='\n');w.writerow(['root_code','basin_size']);w.writerows((int(r),basins[int(r)]) for r in roots)
with open('orbit_roots.csv',newline='') as fh:
    a=list(csv.reader(fh))
with open('vector_roots.csv',newline='') as fh:
    b=list(csv.reader(fh))
assert a==b, 'independent root-and-basin lists differ'
print('independent_root_table_matches',len(roots))
