#!/usr/bin/env python3
"""Exact integer checks for the root-set Fourier phase diagram of complete graphs.

Public scientific checker, using only Python standard library. No external dependencies.
"""
from itertools import combinations, product
from math import comb

checks = 0

def eq(actual, expected, label):
    global checks
    checks += 1
    if actual != expected:
        raise AssertionError((label, actual, expected))


def formula(n, t, s):
    assert n >= 2 and 0 <= s <= n and t > 0
    if s == 0:
        return t * (n+t)**(n-1)
    if s == n:
        return -t * (n-t)**(n-1)
    return t * (n-t-2*s) * (n+t)**(n-s-1) * (n-t)**(s-1)


def root_counts(n):
    """Independent enumeration by edge subsets and all choices of component roots."""
    E = list(combinations(range(n), 2))
    out = [0] * (1 << n)
    for bits in range(1 << len(E)):
        parent = list(range(n))
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        cycle = False
        for i,(u,v) in enumerate(E):
            if bits >> i & 1:
                ru, rv = find(u), find(v)
                if ru == rv:
                    cycle = True
                    break
                parent[ru] = rv
        if cycle:
            continue
        parts = {}
        for v in range(n):
            parts.setdefault(find(v), []).append(v)
        for chosen in product(*parts.values()):
            m = sum(1 << v for v in chosen)
            out[m] += 1
    return out


def walsh(counts):
    a = counts.copy()
    h = 1
    while h < len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):
                x,y=a[i],a[i+h]
                a[i],a[i+h]=x+y,x-y
        h <<= 1
    return a


def infer_rank(n,t):
    return sum(comb(n,s) for s in range(n+1) if formula(n,t,s) != 0)

for n in range(2,7):
    f = root_counts(n)
    for t in sorted(set([1,2,3,n,n+1,2*n+1])):
        weighted = [f[b] * t**b.bit_count() for b in range(1 << n)]
        transformed = walsh(weighted)
        for chi,x in enumerate(transformed):
            eq(x, formula(n,t,chi.bit_count()), f'n={n},t={t},chi={chi}')
        eq(sum(weighted), t*(n+t)**(n-1), f'total n={n} t={t}')
        eq(sum(x==0 for x in transformed), (1<<n)-infer_rank(n,t), f'nullity n={n} t={t}')

# Each of the claimed exact resonance and nonsingularity cases, with independent
# integer evaluation of all n+1 symmetry classes.
for n in range(2,130):
    resonances = {n} | {n-2*s for s in range(1,(n-1)//2+1)}
    for t in range(1,n+4):
        zeros = [s for s in range(n+1) if formula(n,t,s) == 0]
        should = list(range(2,n+1)) if t == n else ([ (n-t)//2 ] if t in resonances else [])
        eq(zeros,should,f'resonance n={n},t={t}')
        if t < n:
            for s in range(n+1):
                F = formula(n,t,s)
                predicted = 1 if n-t-2*s>0 else (-1 if n-t-2*s<0 else 0)
                eq((F>0)-(F<0),predicted,f'sign n={n},t={t},s={s}')
        elif t > n:
            for s in range(n+1):
                F = formula(n,t,s)
                eq((F>0)-(F<0),(-1)**s,f'outer sign n={n},t={t},s={s}')

# Sharp nonzero gap and maximal multiplier magnitude at unit activity.
for n in range(2,160):
    vals = [formula(n,1,s) for s in range(n+1)]
    nonzero = [abs(a) for a in vals if a]
    m = n//2
    if n % 2 == 0:
        gap = (n*n-1)**(m-1)
        idx = m
    else:
        gap = 2*(n+1)**(m-1)*(n-1)**m
        idx = m+1
    eq(min(nonzero),gap,f'gap n={n}')
    eq(abs(vals[idx]),gap,f'gap attainer n={n}')
    eq(max(nonzero),(n+1)**(n-1),f'max n={n}')
    if n%2:
        eq(sum(comb(n,s) for s in range(n+1) if vals[s]==0),comb(n,(n-1)//2),f'null n={n}')
    else:
        eq(sum(comb(n,s) for s in range(n+1) if vals[s]==0),0,f'null n={n}')

print(f'PASS {checks} exact assertions; independent root-forest enumeration up to n=6; all-symmetry arithmetic through n=159')
