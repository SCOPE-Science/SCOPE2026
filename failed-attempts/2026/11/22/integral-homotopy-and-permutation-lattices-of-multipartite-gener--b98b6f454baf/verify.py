#!/usr/bin/env python3
"""Finite independent checks of complete multipartite general-position complexes.
Run: python3 verify.py. Uses only the Python standard library.
"""
from itertools import product, combinations
from math import prod


def rank(columns, prime):
    pivots = {}
    for col in columns:
        v = {i: x % prime for i, x in col.items() if x % prime}
        while v:
            k = max(v)
            if k in pivots:
                lead = v[k] * pow(pivots[k][k], -1, prime) % prime
                for j, x in pivots[k].items():
                    z = (v.get(j, 0) - lead*x) % prime
                    if z: v[j] = z
                    else: v.pop(j, None)
            else:
                mul = pow(v[k], -1, prime)
                pivots[k] = {j: (x*mul) % prime for j, x in v.items()}
                break
    return len(pivots)


def case(sizes):
    t = len(sizes)
    parts = [i for i, a in enumerate(sizes) for _ in range(a)]
    n = len(parts)
    def distance(i, j):
        return 0 if i == j else (2 if parts[i] == parts[j] else 1)
    faces = {0: []}
    for k in range(n+1):
        for s in combinations(range(n), k):
            direct = all(distance(a, c) != distance(a, b)+distance(b, c)
                         for a, b, c in combinations(s, 3)
                         for a, b, c in ((a,b,c),(a,c,b),(b,a,c)))
            per_part = [sum(parts[v] == i for v in s) for i in range(t)]
            formula = max(per_part,default=0) == k or max(per_part,default=0) <= 1
            assert direct == formula, (sizes, s, direct, formula)
            if direct: faces.setdefault(k, []).append(s)
    ranks = {}
    for k in range(1, n+1):
        source = faces.get(k, [])
        targets = faces.get(k-1, [])
        index = {f: j for j,f in enumerate(targets)}
        cols = []
        for s in source:
            cols.append({index[s[:i]+s[i+1:]]: (-1)**i for i in range(k)})
        ranks[k] = {p: rank(cols, p) for p in (2,101)}
        assert len(set(ranks[k].values())) == 1, (sizes, k, ranks[k])
    def expect(k):
        if k == 1: return (prod(sizes)-1 if t == 2 else sum(x-1 for x in sizes))
        if k == t-1 and t >= 3: return prod(x-1 for x in sizes)
        return 0
    for k in range(1,n+1):
        beta = len(faces.get(k+1, [])) - ranks.get(k+1, {2:0})[2] - ranks.get(k+2, {2:0})[2]
        assert beta == expect(k), (sizes, 'beta', k, beta, expect(k))
    assert 1 == len(faces[0])
    return len(sum(faces.values(), []))


def orientation_check():
    # Fundamental alternating octahedral 2-cycle of K_{2,2,2}.
    vertices = [[0,1], [2,3], [4,5]]
    cyc = {tuple(v): (-1)**sum(j for j in ix)
           for ix in product(range(2), repeat=3)
           for v in [[vertices[i][ix[i]] for i in range(3)]]}
    def signed_image(perm):
        out={}
        for face,coef in cyc.items():
            q=[perm[x] for x in face]
            sign=(-1)**sum(q[i]>q[j] for i in range(3) for j in range(i+1,3))
            s=tuple(sorted(q))
            out[s]=out.get(s,0)+sign*coef
        return out
    # Swap first and second parts, preserving labels within each part.
    part_swap={0:2,1:3,2:0,3:1,4:4,5:5}
    assert signed_image(part_swap)=={f:-c for f,c in cyc.items()}
    # Swap the two vertices within the first part.
    vertex_swap={0:1,1:0,2:2,3:3,4:4,5:5}
    assert signed_image(vertex_swap)=={f:-c for f,c in cyc.items()}

if __name__=='__main__':
    cnt=0;total=0
    for t in (2,3,4):
        for sizes in product((1,2,3),repeat=t):
            if sum(sizes)>10: continue
            total+=case(sizes);cnt+=1
    orientation_check()
    print('VERIFY_OK cases=',cnt,'faces_checked=',total,'primes=2,101','orientation=PASS')
