#!/usr/bin/env python3
"""Reproducible graph-distance and discrete-Morse checks for a 16-vertex graph."""
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

N = 16
E = set()
for i in range(8):
    for a, b in ((i,(i+1)%8),(i,i+8),(i+8,8+(i+3)%8)):
        E.add(tuple(sorted((a,b))))
assert len(E) == 24
adj = [set() for _ in range(N)]
for a,b in E:
    adj[a].add(b); adj[b].add(a)
assert all(len(row)==3 for row in adj)

dist = []
for src in range(N):
    d = [-1]*N; d[src] = 0; queue = deque([src])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if d[w]<0:
                d[w]=d[v]+1; queue.append(w)
    assert all(x>=0 for x in d)
    assert Counter(d)=={0:1,1:3,2:6,3:5,4:1}
    dist.append(d)

far = {tuple(sorted((i,(i+4)%8))) for i in range(8)} | {
    tuple(sorted((8+i,8+(i+4)%8))) for i in range(8)}
assert len(far)==8
assert {(a,b) for a in range(N) for b in range(a+1,N) if dist[a][b]==4}==far

colors = [-1]*N; colors[0]=0;queue=deque([0])
while queue:
    v=queue.popleft()
    for w in adj[v]:
        if colors[w]<0:
            colors[w]=1-colors[v];queue.append(w)
        assert colors[w]!=colors[v]
X={i for i in range(N) if colors[i]==0};Y=set(range(N))-X
assert len(X)==len(Y)==8
for side in (X,Y):
    for a,b in combinations(sorted(side),2):
        assert dist[a][b] in (2,4)
    assert sum(dist[a][b]==4 for a,b in combinations(sorted(side),2))==4
    opp=Y if side is X else X
    triples=[frozenset(adj[v]) for v in opp]
    assert len(set(triples))==8
    edge_mult=Counter(tuple(sorted(p)) for t in triples for p in combinations(sorted(t),2))
    assert len(edge_mult)==24 and set(edge_mult.values())=={1}
    assert set(edge_mult)=={(a,b) for a,b in combinations(sorted(side),2) if dist[a][b]==2}


def all_faces(radius):
    # Exhaust all nonempty vertex masks, with every pair at graph distance <= radius.
    faces=set()
    for mask in range(1,1<<N):
        verts=[i for i in range(N) if mask&(1<<i)]
        if all(dist[i][j]<=radius for i,j in combinations(verts,2)):
            faces.add(mask)
    return faces

f1=all_faces(1); f2=all_faces(2);f3=all_faces(3)
assert [Counter(f.bit_count()-1 for f in fs) for fs in (f1,f2,f3)]==[
    Counter({0:16,1:24}),
    Counter({0:16,1:72,2:112,3:48}),
    Counter({0:16,1:112,2:448,3:1120,4:1792,5:1792,6:1024,7:256})]
assert len(f2)==248 and len(f3)==6560
assert all(all(not(f&(1<<a) and f&(1<<b)) for a,b in far) for f in f3)
assert len(f3)==3**8-1 # all choices: none, first, second from each forbidden pair

# Check a self-contained face-deletion sequence: each Morse pair has a free
# lower face and a maximal upper coface at the time of its deletion.
cert=json.loads((Path(__file__).resolve().parent/'morse_certificate.json').read_text(encoding='utf-8'))
assert set(cert)=={'pairs','critical','operations'}
# The original certificate stores pair removals followed by critical removals
# as lists; the interleaving is carried separately in the chronological log.
if 'operations' in cert:
    ops=cert['operations']
else:
    raise AssertionError('The certificate requires the chronological operation log')
current=set(f2)
pairs=Counter();critical=Counter();matched=set()
for op in ops:
    if op[0]=='C':
        f=op[1]; assert f in current
        assert not any(g!=f and (g&f)==f for g in current)
        current.remove(f);critical[f.bit_count()-1]+=1
        assert f not in matched
    elif op[0]=='P':
        a,b=op[1:];assert a in current and b in current
        assert b.bit_count()==a.bit_count()+1 and (a&b)==a
        assert not any(g!=a and g!=b and (g&a)==a for g in current)
        current.remove(a);current.remove(b);pairs[a.bit_count()-1]+=1
        assert a not in matched and b not in matched
        matched.add(a);matched.add(b)
    else:raise AssertionError('Unknown operation')
assert not current
assert critical=={0:1,2:9,3:2}
assert sum(pairs.values())==118

# Independent bitwise boundary rank check over F2, verifying the Morse result.
by_dim={d:sorted(f for f in f2 if f.bit_count()==d+1) for d in range(4)}
def rank_mod2(d):
    lows={f:i for i,f in enumerate(by_dim[d-1])}
    pivots={}
    for mask in by_dim[d]:
        v=0
        for i in range(N):
            if mask&(1<<i):v^=1<<lows[mask^(1<<i)]
        while v:
            p=v.bit_length()
            if p not in pivots:pivots[p]=v;break
            v^=pivots[p]
    return len(pivots)
ranks={d:rank_mod2(d) for d in (1,2,3)}
betti={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(4)}
assert betti=={0:0,1:0,2:9,3:2}
print('VERIFY_OK graph=GP(8,3) vertices=16 edges=24 distance4_pairs=8 '
      'f1=40 f2=248 f3=6560 morse_pairs=118 critical=(1,0,9,2) '
      'mod2_betti_scale2=(0,0,9,2)')
