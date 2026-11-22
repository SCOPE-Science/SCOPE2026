#!/usr/bin/env python3
"""Exact finite-state verification for strand-agnostic no-homopolymer 3-mer coverage."""
from functools import lru_cache
from itertools import product
from collections import Counter

D = range(4)  # A, C, G, T in this order, so complement is 3 - symbol
rc = lambda t: tuple(3 - x for x in t[::-1])
edges = [(a,b,c) for a,b,c in product(D,repeat=3) if a != b and b != c]
classes = sorted({min(t,rc(t)) for t in edges})
assert len(edges) == 36 and len(classes) == 18
index = {t:i for i,r in enumerate(classes) for t in (r,rc(r))}
vertices = sorted({(a,b) for a,b,c in edges})
vi = {v:i for i,v in enumerate(vertices)}
out = [[] for _ in vertices]
for a,b,c in edges:
    out[vi[a,b]].append((vi[b,c],index[a,b,c],c))
assert classes[5] == (0,3,0) and classes[11] == (1,2,1)
FULL = (1 << 18) - 1

def count(extra,closed):
    ans = []
    for start in range(len(vertices)):
        @lru_cache(None)
        def f(cur,seen,e5,e11):
            if seen == FULL and e5+e11 == extra:
                return int(not closed or cur == start)
            total = 0
            for dst,j,_ in out[cur]:
                if not (seen & (1 << j)):
                    total += f(dst, seen | (1 << j), e5,e11)
                elif j == 5 and e5 == 0 and e5+e11 < extra:
                    total += f(dst,seen,1,e11)
                elif j == 11 and e11 == 0 and e5+e11 < extra:
                    total += f(dst,seen,e5,1)
            return total
        ans.append(f(start,0,0,0))
        f.cache_clear()
    return ans

# Quotient vertices and degrees for each reverse-complement 3-mer orbit.
rep = lambda v: min(v, (3-v[1],3-v[0]))
qvertices = sorted({rep(v) for v in vertices})
deg = Counter({v:0 for v in qvertices})
odd_edges = []
for i,t in enumerate(classes):
    p,q = rep(t[:2]),rep(t[1:])
    deg[p] += 1; deg[q] += 1
    if p in ((0,3),(1,2),(2,1),(3,0)) and q in ((0,3),(1,2),(2,1),(3,0)) and p != q:
        odd_edges.append(i)
assert sorted(deg.values()) == [3,3,3,3,6,6,6,6]
assert odd_edges == [5,11]
linear = count(1,False)
circular = count(2,True)
assert linear == [0,0,14496,0,14496,0,0,14496,0,14496,0,0]
assert circular == [21744,21744,28992,21744,28992,21744,21744,28992,21744,28992,21744,21744]
assert sum(linear) == 57984
assert sum(circular) == 289920 and sum(circular) % 20 == 0
assert sum(circular)//20 == 14496

def check(word,cyclic):
    x = tuple('ACGT'.index(ch) for ch in word)
    assert all(x[i]!=x[(i+1)%len(x)] for i in range(len(x)-(0 if cyclic else 1)))
    factors = [tuple(x[(i+j)%len(x)] for j in range(3)) for i in range(len(x) if cyclic else len(x)-2)]
    hist = Counter(index[t] for t in factors)
    assert len(hist)==18
    assert sorted((j,c) for j,c in hist.items() if c>1) == ([(5,2),(11,2)] if cyclic else [(11,2)])

check('ATACACGACTCAGATGCGCTA',False)
check('ACACGACTATCAGAGCGCAT',True)
print('DP_VERIFY_OK 18_orbits=18 min_linear_symbols=21 linear_words=57984 min_circle_symbols=20 rotational_circles=14496')
