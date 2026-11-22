"""Exact finite checks for the overlap network of independent uniform recursive trees.

Run with Python 3 standard library: python3 verify.py
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction as Q
from math import factorial, prod

checks = 0

def verify(a, b, label):
    global checks
    assert a == b, (label, a, b)
    checks += 1

def rank(q, edges):
    parent = list(range(q))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = root(a), root(b)
        parent[ra] = rb
    return q - len({root(v) for v in range(q)})

def step_distribution(q, edges, k):
    ans = Counter()
    for colors in product(range(k), repeat=q):
        bits = tuple(int(colors[a] == colors[b]) for a, b in edges)
        ans[bits] += 1
    return {bits: Q(number, k**q) for bits, number in ans.items()}

def pgf_law(q, edges, n):
    law = {tuple(0 for _ in edges): Q(1)}
    for k in range(1, n):
        next_law = Counter()
        for v, pv in law.items():
            for bits, pp in step_distribution(q, edges, k).items():
                next_law[tuple(x+y for x,y in zip(v, bits))] += pv*pp
        law = dict(next_law)
    return law

def direct_law(q, edges, n):
    parent_options = [tuple(product(*(range(k) for k in range(1, n))))] * q
    law = Counter()
    for parents in product(*parent_options):
        overlap = tuple(sum(parents[a][k] == parents[b][k]
                            for k in range(n-1)) for a,b in edges)
        law[overlap] += 1
    return {v: Q(count, factorial(n-1)**q) for v, count in law.items()}

def cycle_cumulant_from_law(law, m, n):
    mu = sum((Q(1,k) for k in range(1,n)), Q(0))
    return sum((prob * prod((x-mu for x in vec), start=Q(1))
                for vec, prob in law.items()), Q(0))

for q, edges in [(3,((0,1),(1,2),(0,2))),
                 (4,((0,1),(1,2),(2,3),(3,0))),
                 (4,((0,1),(1,2),(2,3)))]:
    m = len(edges)
    for k in range(1,6):
        counts = step_distribution(q, edges, k)
        for mask in range(1<<m):
            picked = [edges[i] for i in range(m) if (mask >> i) & 1]
            prob = sum((p for bits,p in counts.items()
                        if all(bits[i] for i in range(m) if (mask >> i)&1)), Q(0))
            verify(prob, Q(1,k**rank(q,picked)), (q,k,mask,'rank'))
            if m == 3 and q == 4:  # path: independent Bernoulli events
                verify(prob, Q(1,k**len(picked)), (q,k,mask,'forest'))
    for n in range(2, (6 if q == 3 else 5)):
        law = pgf_law(q,edges,n)
        verify(sum(law.values()), Q(1), (q,n,'normalized'))
        exact = direct_law(q,edges,n)
        verify(law, exact, (q,n,'entire-labeled-overlap-law'))
        if m == q: # simple cycle
            predicted = sum((Q(k-1,k**m) for k in range(1,n)),Q(0))
            verify(cycle_cumulant_from_law(law,m,n), predicted,
                   (q,n,'cycle-cumulant'))

# All pair-overlap marginals have the Stirling (permutation-cycle) distribution.
for n in range(2,9):
    law = pgf_law(2, ((0,1),), n)
    vals = [0,1]
    for i in range(2,n):
        prev=vals
        vals=[0]*(i+1)
        for k in range(1,i+1):
            vals[k] = (prev[k-1] if k-1 < len(prev) else 0) + (i-1)*(prev[k] if k < len(prev) else 0)
    for k in range(1,n):
        verify(law.get((k,),Q(0)), Q(vals[k],factorial(n-1)), (n,k,'Stirling'))

# A distinct-index forest of overlaps is jointly independent, not only uncorrelated.
for n in range(2,6):
    forest=((0,1),(1,2),(2,3))
    law=pgf_law(4, forest,n)
    marg=pgf_law(2,((0,1),),n)
    for v,p in law.items():
        verify(p,prod((marg[(k,)] for k in v),start=Q(1)), (n,v,'forest independence'))

print(f'VERIFY_OK {checks} exact-rational assertions')
