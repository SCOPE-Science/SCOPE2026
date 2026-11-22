from itertools import permutations,combinations
from collections import Counter
import io,contextlib,runpy
with contextlib.redirect_stdout(io.StringIO()):a=runpy.run_path('cubo_ice_independent.py')
Q=a['Q'];E=a['E'];sol=a['solutions'];idx={t:i for i,t in enumerate(Q)};edgeindex={t:i for i,t in enumerate(E)}
zero=[]
for c in combinations(range(24),4):
    mask=sum(1<<k for k in c)
    if sum(1 if (s&mask).bit_count()%2==0 else -1 for s in sol)==0:zero.append(mask)
zero=set(zero);assert len(zero)==864
permEdge=[]
for perm in permutations(range(3)):
 for trans in range(8):
    def xf(u):return sum(((u>>perm[k])&1)<<k for k in range(3))^trans
    qmap=[]
    for i,j in Q: qmap.append(idx[tuple(sorted((xf(i),xf(j))))])
    emap=[]
    for i,j in E: emap.append(edgeindex[tuple(sorted((qmap[i],qmap[j])))])
    permEdge.append(emap)
assert len(set(tuple(x) for x in permEdge))==48
orbits=[]
while zero:
 rep=min(zero);support=[i for i in range(24) if rep>>i&1]
 orb={sum(1<<p[i] for i in support) for p in permEdge}
 assert orb<=zero
 orbits.append((len(orb),support,[E[i] for i in support]))
 zero-=orb
print('zero-orbits count:',len(orbits));print('orbit sizes',Counter(x[0] for x in orbits));print('first reps:')
for o in orbits:print(o)
