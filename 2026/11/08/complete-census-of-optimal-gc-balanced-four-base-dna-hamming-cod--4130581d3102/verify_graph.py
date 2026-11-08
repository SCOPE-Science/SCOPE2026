#!/usr/bin/env python3
"""Independent exhaustive maximal-clique enumeration of RC-orbit graph.

No external dependency; uses Bron--Kerbosch with pivoting on 44 vertices.
"""
import itertools,json
from collections import Counter
from pathlib import Path
S='ACGT'; comp={'A':'T','T':'A','C':'G','G':'C'}
def rho(w):return ''.join(comp[x] for x in w[::-1])
def dist(a,b):return sum(a[i]!=b[i] for i in range(4))
words=[''.join(t) for t in itertools.product(S,repeat=4) if sum(c in 'CG' for c in t)==2]
O=sorted({tuple(sorted({w,rho(w)})) for w in words})
O=[o for o in O if len(o)==1 or dist(o[0],o[1])>=3]
assert len(O)==44
n=len(O)
adj=[0]*n
for i in range(n):
    for j in range(i):
        if all(dist(x,y)>=3 for x in O[i] for y in O[j]):
            adj[i] |= 1<<j
            adj[j] |= 1<<i

def bits(s):
    while s:
        t=s & -s
        yield t.bit_length()-1
        s-=t

# Each maximal clique is a maximal compatible family of RC-orbits.
maximal=[]
def bk(R,P,X):
    if not (P|X):
        maximal.append(R)
        return
    U=P|X
    pivot=max(bits(U),key=lambda u:(P & adj[u]).bit_count()) if U else 0
    Q=P & ~adj[pivot]
    for v in list(bits(Q)):
        bk(R | (1<<v),P & adj[v],X & adj[v])
        P &= ~(1<<v)
        X |= 1<<v
bk(0,(1<<n)-1,0)
assert len(maximal)==704
sizes=[sum(len(O[v]) for v in bits(m)) for m in maximal]
assert max(sizes)==12 and Counter(sizes)[12]==16
codes={tuple(sorted(x for v in bits(m) for x in O[v])) for m,s in zip(maximal,sizes) if s==12}
assert len(codes)==16
assert all(sum(dist(a,b)==4 for i,a in enumerate(code) for b in code[i+1:])==18
           for code in codes)
ref=json.loads(Path(__file__).with_name('optimal_codes.json').read_text('utf-8'))
assert codes=={tuple(c) for c in map(tuple,ref['codes'])}
print('GRAPH_ENUM_OK: 44 permissible RC-orbits, 704 maximal compatible sets, exactly 16 weight-12 optima')
