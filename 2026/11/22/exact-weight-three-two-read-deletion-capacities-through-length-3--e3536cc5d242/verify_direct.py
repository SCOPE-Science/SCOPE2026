"""Standalone finite certificate validator for fixed-weight-three two-read codes.
Requires only the Python standard library. Run: python3 verify_direct.py
"""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json

P=Path(__file__).with_name('certificates.json')
data=json.loads(P.read_text(encoding='utf-8'))['lengths']

def deck(triple,n):
    return {sum(1 << (p-(p>i)) for p in triple if p!=i) for i in range(n)}

def target(n):
    if n==3:return 1
    if n%2==0:
        m=n//2
        return (2*m**3-6*m**2+13*m-12)//3
    m=(n-1)//2
    return (m-1)*(2*m*m-m+12)//3

for n in range(3,33):
    vertices=list(combinations(range(n),3)); k=len(vertices)
    c=data[str(n)]
    code=c['independent_indices']; parts=c['clique_partition']
    assert c['alpha']==target(n)==len(code)==len(parts), (n,'size')
    assert len(set(code))==len(code) and all(0<=x<k for x in code)
    assert sorted(v for clique in parts for v in clique)==list(range(k)),(n,'partition')
    decks=[deck(v,n) for v in vertices]
    # An exhaustive clique partition proves no independent family can use > one from each class.
    for clique in parts:
        for a,b in combinations(clique,2):
            assert len(decks[a]&decks[b])>=2,(n,'not clique',a,b)
    # Independently prove code validity by counting shared deletion outputs, not graph edges.
    byread=defaultdict(list)
    for v in code:
        for read in decks[v]:byread[read].append(v)
    pair_counts=defaultdict(int)
    for participants in byread.values():
        for pair in combinations(participants,2):
            pair_counts[pair]+=1
            assert pair_counts[pair]<=1,(n,'ambiguous pair',pair)
    print(f'n={n}: {k} candidates, alpha={len(code)}, exact certificate passed')
print('PASS: every code and clique-cover pair independently certified by deletion sets for n=3,...,32')
