#!/usr/bin/env python3
"""Independent definition-level verifier of the strong-odd coloring formula for clique bouquets."""
from itertools import product, permutations
from math import comb, factorial, ceil


def bouquet_graph(sizes):
    count = 1 + sum(sizes)
    adj = [set() for _ in range(count)]
    first = 1
    for s in sizes:
        blade = range(first, first+s)
        for x in blade:
            adj[x].add(0); adj[0].add(x)
            for y in blade:
                if x != y: adj[x].add(y)
        first += s
    return adj


def is_strong_odd(adj, labels):
    for v, nbrs in enumerate(adj):
        if any(labels[v] == labels[u] for u in nbrs): return False
        mult = {}
        for u in nbrs:
            a = labels[u]
            mult[a] = mult.get(a, 0) + 1
        if any(x % 2 == 0 for x in mult.values()): return False
    return True


def krawtchouk(s, j, k):
    return sum((-1)**h * comb(j,h)*comb(k-j,s-h)
               for h in range(max(0,s-(k-j)), min(s,j)+1))


def count_formula(sizes, q):
    if q == 0: return 0
    S = sum(sizes)
    scale = 1
    for s in sizes: scale *= factorial(s)
    total = 0
    for k in range(min(q-1,S)+1):
        numerator = 0
        for j in range(k+1):
            v = (-1)**j*comb(k,j)
            for s in sizes: v *= krawtchouk(s,j,k)
            numerator += v
        numerator *= scale
        assert numerator % 2**k == 0
        total += comb(q-1,k)*(numerator//2**k)
    return q*total


def formula_min_uniform(t, s):
    return (1+s) if t%2 else (1+2*ceil(t*s/(2*(t-1))))


def construct_uniform(t, s):
    k = formula_min_uniform(t,s)-1
    if t%2:
        degrees = [t]*s
    else:
        degrees = [1]*k
        available = (t*s-k)//2
        for j in range(k):
            add = min(available, (t-2)//2)
            degrees[j] += 2*add
            available -= add
        assert available == 0
    assert sum(degrees) == t*s
    assert all(0 < v <= t and v%2 for v in degrees)
    rows = [set() for _ in range(t)]
    for j, d in enumerate(degrees):
        for i in range(d): rows[i].add(j)
    while max(map(len,rows)) > min(map(len,rows)):
        large = max(range(t),key=lambda i:len(rows[i]))
        small = min(range(t),key=lambda i:len(rows[i]))
        assert len(rows[large])-len(rows[small])>=2
        j=min(rows[large]-rows[small])
        rows[large].remove(j); rows[small].add(j)
    assert all(len(row)==s for row in rows)
    col=[k]
    for row in rows: col.extend(sorted(row))
    assert is_strong_odd(bouquet_graph([s]*t),col)
    return col


print('VERIFY_OK')
tests = [
    (1,1),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),
    (1,2),(1,3),(2,3),(3,2,1),(2,1,2),(2,2,2),(1,1,1),
    (1,1,2),(1,2,2),(3,1,1),(2,3,1),(1,1,1,1),
    (2,2,1,1),(3,2,1,1),(1,2,1,2,1)
]
comps=0
checked=0
for sizes in tests:
    adj=bouquet_graph(sizes)
    for q in range(1,7):
        counts=[list(permutations(range(1,q),s)) for s in sizes]
        budget=1
        for a in counts: budget *= len(a)
        if budget > 1_000_000: continue
        direct=0
        for blades in product(*counts):
            arr=(0,)+tuple(v for blade in blades for v in blade)
            checked+=1
            direct+=is_strong_odd(adj,arr)
        direct *= q
        got=count_formula(sizes,q)
        assert got==direct,(sizes,q,got,direct)
        comps+=1
    print('sizes=',sizes,'palette q=6 count=',count_formula(sizes,6))

construction_count=0
for t in range(2,21):
    for s in range(1,31):
        chrom=formula_min_uniform(t,s)
        arr=construct_uniform(t,s)
        assert len(arr)==1+t*s
        assert len(set(arr))==chrom
        assert count_formula([s]*t,chrom)>0
        assert count_formula([s]*t,chrom-1)==0
        construction_count+=1

print('independent_direct_palette_comparisons =',comps)
print('center_normalized_colorings_directly_checked =',checked)
print('uniform_constructive_pairs =',construction_count)
print('constructed uniform range 2<=t<=20, 1<=s<=30')
print('Every check matched')
