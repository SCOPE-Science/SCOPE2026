#!/usr/bin/env python3
"""Independent finite arithmetic and recoloring-graph checks for the closed-walk formula.
Python standard library only. All graph and path definitions are explicit.
Usage: python3 verify.py [--extended]
"""
from itertools import combinations
from collections import Counter
import sys

P = list(combinations(range(5), 2))
N = tuple(tuple(j for j, y in enumerate(P) if not set(x).intersection(y)) for x in P)
assert len(P) == 10 and all(len(t) == 3 for t in N)
E = [(u, v) for u in range(10) for v in N[u]]
B = [tuple(j for j, (v, w) in enumerate(E) if v == b and w != a)
     for a, b in E]
assert len(E) == 30 and all(len(row) == 2 for row in B)

def traceB(k):
    total = 0
    for source in range(len(E)):
        d = [0] * len(E)
        d[source] = 1
        for _ in range(k):
            nxt = [0] * len(E)
            for i, value in enumerate(d):
                if value:
                    for j in B[i]:
                        nxt[j] += value
            d = nxt
        total += d[source]
    return total

def circle_count(n, primitive):
    out = 0
    for d, p in primitive.items():
        if n % 2:
            if d % 2:
                out += p * (( (n-2)//d + 1)//2)
        elif d % 2:
            out += p * ((n-2)//(2*d))
        else:
            out += 2*p*((n-2)//d)
    return out

def maps(n):
    def rec(a):
        if len(a) == n:
            if a[0] in N[a[-1]]:
                yield tuple(a)
        else:
            for v in N[a[-1]]:
                a.append(v)
                yield from rec(a)
                a.pop()
    for x in range(10):
        yield from rec([x])

def cyclic_length(path):
    a = list(path)
    while len(a) > 2:
        j = next((i for i in range(len(a))
                  if a[(i-1)%len(a)] == a[(i+1)%len(a)]), None)
        if j is None:
            break
        for q in sorted({j,(j+1)%len(a)}, reverse=True):
            a.pop(q)
    return 0 if len(a) <= 2 else len(a)

def enumerate_components(n):
    remaining = set(maps(n))
    distribution = Counter()
    while remaining:
        seed = remaining.pop()
        queue = [seed]
        for a in queue:
            for i in range(n):
                if a[(i-1)%n] == a[(i+1)%n]:
                    for z in N[a[(i-1)%n]]:
                        if z == a[i]:
                            continue
                        b = a[:i] + (z,) + a[i+1:]
                        if b in remaining:
                            remaining.remove(b)
                            queue.append(b)
        distribution[(cyclic_length(seed),len(queue))] += 1
    return distribution

def main():
    maxi = 13 if '--extended' in sys.argv else 12
    traces = {i: traceB(i) for i in range(1, maxi+1)}
    primitive = {}
    for i in range(1, maxi+1):
        v = traces[i] - sum(d*primitive[d] for d in range(1,i) if i%d == 0)
        assert v%i == 0
        primitive[i] = v//i
    for n in range(3,maxi+1):
        dist = enumerate_components(n)
        r = sum(v for (ell,size),v in dist.items() if size == 1)
        c = sum(v for (ell,size),v in dist.items() if size > 1 and ell > 0)
        z = sum(v for (ell,size),v in dist.items() if ell == 0)
        exp_r, exp_c, exp_z = traces[n], circle_count(n,primitive), int(n%2==0)
        assert (r,c,z) == (exp_r,exp_c,exp_z), (n,r,c,z,exp_r,exp_c,exp_z)
        assert n != 3 or not dist
        print(f'n={n} homomorphisms={sum(size*ct for (ell,size),ct in dist.items())} '
              f'rigid={r} circles={c} null_components={z} '
              f'distribution={sorted((ell,size,ct) for (ell,size),ct in dist.items())}')
    assert [traces[n] for n in range(5,13)] == [120,120,0,240,360,1320,2640,3360]
    print('OK: transfer-trace/Mobius counts and exact recoloring components agree.')

if __name__=='__main__':
    main()
