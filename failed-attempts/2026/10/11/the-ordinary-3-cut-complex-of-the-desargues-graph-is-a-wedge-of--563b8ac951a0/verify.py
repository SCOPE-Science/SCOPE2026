#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256
import json
N=20
FULL=(1<<N)-1
adj=[set() for _ in range(N)]
def add(a,b): adj[a].add(b); adj[b].add(a)
for i in range(10):
    add(i,(i+1)%10)
    add(i,10+i)
    add(10+i,10+((i+3)%10))
assert all(len(a)==3 for a in adj)
# girth by BFS
g=99
for s in range(N):
    dist={s:0}; par={s:-1}; q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in dist:
                dist[y]=dist[x]+1; par[y]=x; q.append(y)
            elif par[x]!=y:
                g=min(g,dist[x]+dist[y]+1)
assert g==6
connected=[]; disconnected=[]
for S in combinations(range(N),3):
    ss=set(S); seen={S[0]}; q=[S[0]]
    for x in q:
        for y in adj[x]&ss:
            if y not in seen: seen.add(y); q.append(y)
    mask=sum(1<<i for i in S)
    (connected if len(seen)==3 else disconnected).append(mask)
assert len(connected)==60 and len(disconnected)==1080
D=set(disconnected)
# Directly verify the complete 15-skeleton condition: every 4-set contains a disconnected triple.
for Q in combinations(range(N),4):
    qm=sum(1<<i for i in Q)
    assert any((d & ~qm)==0 for d in D)
# Proposition 6.2 from the cited source applies because girth 6 > 4. Hence the
# ordinary 3-cut complex consists of every nonempty face of size <=16, together
# with the 17-vertex facets whose 3-vertex complements are disconnected.
faces=set()
for f in range(1,1<<N):
    s=f.bit_count()
    if s<=16 or (s==17 and (FULL^f) in D): faces.add(f)
assert len(faces)==1048304
fc=Counter(f.bit_count()-1 for f in faces)
expected={0:20,1:190,2:1140,3:4845,4:15504,5:38760,6:77520,7:125970,8:167960,9:184756,10:167960,11:125970,12:77520,13:38760,14:15504,15:4845,16:1080}
assert dict(sorted(fc.items()))==expected
# Sequential element matching M_0,...,M_19. Such a sequence is acyclic by the
# element-matching lemma used in Bayer et al., Topology of Cut Complexes of Graphs.
unmatched=set(faces)
pairs=0
for v in range(N):
    bit=1<<v
    lows=[]
    for f in unmatched:
        if f & bit: continue
        if (f|bit) in unmatched: lows.append(f)
    for f in lows:
        h=f|bit
        if f in unmatched and h in unmatched:
            unmatched.remove(f); unmatched.remove(h); pairs+=1
crit=Counter(f.bit_count()-1 for f in unmatched)
assert pairs==524096
assert crit==Counter({16:111,0:1})
critical_top=sorted(f for f in unmatched if f.bit_count()==17)
digest=sha256(b''.join(x.to_bytes(3,'little') for x in critical_top)).hexdigest()
chi=sum(((-1)**d)*c for d,c in fc.items())
assert chi==112
assert chi-1==111
out={"vertices":N,"girth":g,"connected_triples":len(connected),"disconnected_triples":len(disconnected),"nonempty_faces":len(faces),"face_vector":[fc[d] for d in range(17)],"matched_pairs":pairs,"critical_cells":{"0":1,"16":111},"critical_top_masks_sha256":digest,"euler_characteristic":chi,"reduced_euler_characteristic":chi-1}
print(json.dumps(out,sort_keys=True))
