"""Build + verify the found sigma-invariant STS(21): FIX 000000012, MIX/P3 above."""
from itertools import combinations
def sig(x): return x^1 if x<18 else x
FIX=[0,0,0,0,0,0,0,1,2]
MIX=[(14,16,18),(0,14,20),(2,4,20),(6,8,20),(10,12,20),(2,8,19),(4,12,19),(0,6,19),(10,16,19)]
P3=[(0,3,15),(4,6,15),(2,7,15),(4,10,14),(8,12,15),(8,11,14),(12,14,17),(0,2,13),(2,5,10),(2,6,17),(2,9,11),(2,12,16),(6,10,13),(0,5,12),(6,9,12),(4,7,17),(0,7,10),(0,11,16),(0,4,8),(0,9,17),(4,9,16)]
blocks=set()
blocks.add((18,19,20))
for i,f in enumerate(FIX):
    blocks.add(tuple(sorted((18+f,2*i,2*i+1))))
for t in MIX:
    blocks.add(tuple(sorted(t)))
    blocks.add(tuple(sorted((sig(t[0]),sig(t[1]),sig(t[2])))))
for t in P3:
    blocks.add(tuple(sorted(t)))
    blocks.add(tuple(sorted((sig(t[0]),sig(t[1]),sig(t[2])))))
print("num blocks:",len(blocks))
assert len(blocks)==70
cov={}
for b in blocks:
    for p in combinations(b,2):
        assert p not in cov, ("dup",p)
        cov[p]=b
print("pairs covered:",len(cov))
assert len(cov)==210
fixed=[b for b in blocks if tuple(sorted((sig(b[0]),sig(b[1]),sig(b[2]))))==b]
print("fixed blocks:",len(fixed))
for b in fixed: print("  ",b)
# Pasch enumeration
pasch=[]
for s6 in combinations(range(21),6):
    s=set(s6)
    inside=[b for b in blocks if set(b)<=s]
    if len(inside)==4:
        # verify Pasch structure: each point degree 2
        from collections import Counter
        d=Counter()
        for b in inside:
            for x in b: d[x]+=1
        if all(d[x]==2 for x in s6):
            pasch.append((s6,inside))
print("num Pasch:",len(pasch))
for s6,inside in pasch:
    print("6-set:",s6,"blocks:",inside)
import json
json.dump({"blocks":sorted(blocks),"pasch":[[list(s),[list(b) for b in ins]] for s,ins in pasch]},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1574/output/artifacts/sts21_candidate.json","w"),indent=1)
print("saved")
