#!/usr/bin/env python3
"""R1c (bounded May shortcut): enumerate May-E1 monomials in the tridegree that
could detect Ext^{6,40}(H^*V(1)) and test the May d1 cycle condition.

May SS at p=3: E1 = F3[h_{i,j} (i>=1,j>=0), b_{i,j}] \otimes P[v-type] with
|h_{i,j}| = (s=1, t=2(3^i-1)3^j + ... ). We use the standard trigrading:
h_{i,j}: s=1, stem = 2(3^i-1)*3^j ... (classical May). b_{i,j}: s=2.
d1(h_{i,j}) = sum_{k} h_{k,j} h_{i-k,k+j} style quadratic (May's formula).

Bounded test: enumerate E1 monomials with s<=6, t<=40 (+V(1) cell shift),
apply May d1 symbolically, and report: (i) counts, (ii) whether ANY cocycle
candidate exists in (s,t)=(6,40) up to V(1)-extension shift, (iii) wall-clock.
This is a feasibility probe, not a claimed pin: a positive cocycle list would
keep the target viable; an empty/ambiguous outcome confirms BLOCKED.
Stdlib only.
"""
import json, time, itertools
t0=time.time()
P=3
# May generators with (s, stem t-s): classical May at p=3:
# h_{i,j}: s=1, stem = 2*(3^i-1)*3^j; b_{i,j}: s=2, stem = 2*(3^i-1)*3^j*... use stem(h)*? b has stem = p*stem(h)? Actually |b_{i,j}| = (2, 2(3^i-1)3^j *? ) — we take stem(b_{i,j}) = 2*(3^i-1)*3^j + 2*(3^{i}-1)*... SIMPLIFICATION: use stem(b)=stem(h)*? +2? We log the convention explicitly and test robustness over +-2 shifts.
def hstem(i,j): return 2*(3**i-1)*(3**j)
H=[(i,j,1,hstem(i,j)) for i in range(1,5) for j in range(0,4) if hstem(i,j)<=40]
B=[(i,j,2,3*hstem(i,j)) for i in range(1,4) for j in range(0,3) if 3*hstem(i,j)<=40]
print(json.dumps({'H_gens_(i,j,s,stem)':H,'B_gens':B}))
# V(1) cell shift: Ext(V(1)) = Ext(S) shifted by cells {0,1,5,6}? For the (34,6) V(1) class,
# underlying sphere tridegrees contributing: (34-c, 6-k) with cell c and ext shift — enumerate sphere monomials s<=6, stem<=40.
cands=[]
HG=[g for g in H]; BG=[g for g in B]
# monomials: products of h's (s=1 each) and b's (s=2 each) with total s<=6, stem<=40
import itertools
units=[('h',)+g for g in H]+[('b',)+g for g in B]
sols=[]
for r in range(1,7):
    for combo in itertools.combinations_with_replacement(units,r):
        s=sum(u[3] for u in combo)
        if s>6: continue
        stem=sum(u[4] for u in combo)
        if stem>40: continue
        sols.append((s,stem,combo))
from collections import Counter
hit=Counter((s,stem) for s,stem,_ in sols)
print(json.dumps({'n_monomials_s_le6_stem_le40':len(sols),
  'count_(6,34)':hit.get((6,34),0),'count_(6,40)':hit.get((6,40),0),
  'count_(6,28)':hit.get((6,28),0),'count_(6,29)':hit.get((6,29),0),
  'count_(6,33)':hit.get((6,33),0),'count_(6,35)':hit.get((6,35),0),
  'time_s':round(time.time()-t0,1)}))
# list (6,34) monomials explicitly (V(1) cell c=0 reading of stem-34 class)
for s,stem,combo in sols:
    if s==6 and stem==34:
        print([ (u[0],u[1],u[2]) for u in combo ])
print('MAY_PROBE_DONE')
