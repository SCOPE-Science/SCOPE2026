"""Direct finite-field checks for commuting-idempotent bi-rank census.

Run: python checker.py. All multiplication and rank calculations use the
original algebra basis, not the orbit-counting formulas being tested.
"""
from itertools import product
from collections import Counter


def structure(kind):
    if kind in ('line', 'triangle'):
        arrows = [(0, 1), (1, 2), (0, 2)]
    elif kind == 'fork':
        arrows = [(0, 1), (0, 2)]
    elif kind == 'cofork':
        arrows = [(1, 0), (2, 0)]
    else:
        raise ValueError(kind)
    n = 3
    d = n + len(arrows)
    mul = {}
    for i in range(n):
        mul[i, i] = i
    for a, (s, t) in enumerate(arrows, start=n):
        mul[s, a] = a
        mul[a, t] = a
    if kind == 'line':
        mul[n, n+1] = n+2
    left_sizes = [1 + sum(s == i for s, t in arrows) for i in range(n)]
    right_sizes = [1 + sum(t == i for s, t in arrows) for i in range(n)]
    return d, mul, arrows, left_sizes, right_sizes


def rank(matrix, p):
    if not matrix:
        return 0
    a = [list(row) for row in matrix]
    height, width = len(a), len(a[0])
    k = 0
    for j in range(width):
        z = next((i for i in range(k, height) if a[i][j] % p), None)
        if z is None:
            continue
        a[z], a[k] = a[k], a[z]
        scale = pow(a[k][j], -1, p)
        a[k] = [(x * scale) % p for x in a[k]]
        for i in range(k+1, height):
            if a[i][j]:
                c = a[i][j]
                a[i] = [(x-c*y) % p for x,y in zip(a[i], a[k])]
        k += 1
        if k == height:
            break
    return k


def direct(kind, p, r):
    d, mul, arrows, left_sizes, right_sizes = structure(kind)
    vecs = list(product(range(p), repeat=d))
    prod = {}
    for a in vecs:
        for b in vecs:
            v = [0]*d
            for (i,j), k in mul.items():
                if a[i] and b[j]:
                    v[k] = (v[k] + a[i]*b[j]) % p
            prod[a, b] = tuple(v)
    idems = [a for a in vecs if prod[a,a] == a]
    sig = {}
    for a in idems:
        matL = [[prod[a, tuple(int(j==k) for j in range(d))][i]
                 for k in range(d)] for i in range(d)]
        matR = [[prod[tuple(int(j==k) for j in range(d)),a][i]
                 for k in range(d)] for i in range(d)]
        sig[a] = (rank(matL,p), rank(matR,p))
    out = Counter()
    for tup in product(idems, repeat=r):
        if all(prod[a,b] == prod[b,a] for i,a in enumerate(tup) for b in tup[i+1:]):
            out[tuple(sig[a][0] for a in tup) + tuple(sig[a][1] for a in tup)] += 1
    return out, len(idems)


def predicted(kind, p, r):
    d, mul, arrows, ls, rs = structure(kind)
    out=Counter()
    for colors in product(range(1<<r),repeat=3):
        exponent=sum(colors[s] != colors[t] for s,t in arrows)
        key=(tuple(sum(ls[i]*((colors[i]>>j)&1) for i in range(3)) for j in range(r))
             +tuple(sum(rs[i]*((colors[i]>>j)&1) for i in range(3)) for j in range(r)))
        out[key]+=p**exponent
    return out


def main():
    tests=[('line',2,1),('line',2,2),('line',2,3),('triangle',2,2),
           ('fork',2,2),('cofork',2,2),('line',3,2),('triangle',3,2),
           ('fork',3,2),('cofork',3,2)]
    cache={}
    for kind,p,r in tests:
        direct_dist, count_idems = direct(kind,p,r)
        formal = predicted(kind,p,r)
        assert direct_dist == formal, (kind,p,r, direct_dist-formal,formal-direct_dist)
        cache[(kind,p,r)] = direct_dist
        print(f'{kind} F_{p} r={r}: idempotents={count_idems}, tuples={sum(direct_dist.values())}, rank_profiles={len(direct_dist)}: OK')
    for p in (2,3):
        a=cache[('line',p,2)]; b=cache[('triangle',p,2)]
        assert a==b
        c=cache[('fork',p,2)]; d=cache[('cofork',p,2)]
        assert sum(c.values())==sum(d.values()) and c!=d
        print(f'F_{p}: multiplication-blind pair verified; fork opposite equal totals but distinct bi-rank distributions')
    print('ALL_BASIC_ALGEBRA_SIMULTANEOUS_IDEMPOTENT_BIRANK_CHECKS_OK')

if __name__=='__main__':
    main()
