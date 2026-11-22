#!/usr/bin/env python3
"""Brute-force the game and check its excursion-run description."""
from itertools import product
from collections import Counter
G={'':0}
for n in range(1,15):
    counts=Counter()
    for bits in product('ab',repeat=n):
        w=''.join(bits)
        options=set()
        for cut in range(n):
            suffix=w[cut:]
            if suffix[0]==suffix[-1]=='a' and suffix.count('a')==suffix.count('b'):
                options.add(G[w[:cut]])
        g=0
        while g in options: g+=1
        G[w]=g
        height=0; first=None; signs=[]
        for letter in reversed(w):
            if height==0:first=letter
            height+=(1 if letter=='a' else -1)
            if height==0:signs.append(first)
        predicted=0
        if signs and signs[0]=='a':
            predicted=sum(signs[j]=='b' and (j==0 or signs[j-1]=='a') for j in range(len(signs)))
        assert g==predicted,(w,g,signs,predicted)
        counts[g]+=1
    assert sum(counts.values())==2**n
    print(f'n={n:2} count={2**n:5} nimber_spectrum={sorted(counts.items())}')
print(f'PASS: {len(G)} positions, direct mex equals independently parsed excursion-sign statistic')
