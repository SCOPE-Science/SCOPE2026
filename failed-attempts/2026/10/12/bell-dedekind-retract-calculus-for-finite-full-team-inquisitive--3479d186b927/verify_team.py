#!/usr/bin/env python3
"""Self-contained exhaustive finite checks for full-team inquisitive/dependence algebras."""
from itertools import product
from collections import Counter
from math import comb, factorial

CHECKS = 0

def check(condition, explanation='failed check'):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(explanation)

def powerset_bitmask(n, s):
    out = 0
    t = s
    while True:
        out |= 1 << t
        if t == 0:
            return out
        t = (t - 1) & s

def downsets(n):
    size = 1 << n
    low = [powerset_bitmask(n, x) for x in range(size)]
    return [a for a in range(1, 1 << size, 2)
            if all((a & low[s]) == low[s] for s in range(size) if (a >> s) & 1)]

def implication(n, a, b):
    size = 1 << n
    low = [powerset_bitmask(n, x) for x in range(size)]
    answer = 0
    for t in range(size):
        if ((a & ~b) & low[t]) == 0:
            answer |= 1 << t
    return answer

def tensor(n, a, b):
    size = 1 << n
    low = [powerset_bitmask(n, x) for x in range(size)]
    result = 0
    for s in range(size):
        if a >> s & 1:
            for t in range(size):
                if b >> t & 1:
                    result |= low[s | t]
    return result

def lift_f(f, n, m, a):
    # f maps the m target worlds to the n source worlds.
    img = [0] * (1 << m)
    for t in range(1, 1 << m):
        lowbit = t & -t
        j = lowbit.bit_length() - 1
        img[t] = img[t ^ lowbit] | (1 << f[j])
    return sum(1 << t for t in range(1 << m) if a >> img[t] & 1)

def kernel(f):
    classes = {}
    for j, val in enumerate(f):
        classes.setdefault(val, []).append(j)
    return tuple(sorted(tuple(v) for v in classes.values()))

def refines(P, Q):
    return all(any(set(a) <= set(b) for b in Q) for a in P)

def stirling(n, k):
    if n == k == 0: return 1
    if not k or k > n: return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)

Ds = {n: downsets(n) for n in range(1, 5)}
for n, expected in [(1, 2), (2, 5), (3, 19), (4, 167)]:
    check(len(Ds[n]) == expected, ('Dedekind', n))
    core = [powerset_bitmask(n, s) for s in range(1 << n)]
    check(all(c in Ds[n] for c in core), ('core contained', n))
    check(all(implication(n, core[s], core[t]) == core[((1 << n) - 1) & (~s | t)]
              for s in range(1 << n) for t in range(1 << n)), ('core implication', n))

# Each explicitly constructed map is operation-preserving through 3 source worlds.
cross_maps = 0
for n in range(1, 4):
    D = Ds[n]
    for m in range(1, 4):
        targets = set(Ds[m])
        for f in product(range(n), repeat=m):
            cross_maps += 1
            h = {a: lift_f(f, n, m, a) for a in D}
            check(set(h.values()) <= targets, ('well-defined', n, m, f))
            check(h[1] == 1, ('bottom', n, m, f))
            check(all(h[powerset_bitmask(n, s)] == powerset_bitmask(m, sum(1 << j for j in range(m) if f[j] in [i for i in range(n) if s >> i & 1]))
                     for s in range(1 << n)), ('core', n, m, f))
            for a in D:
                for b in D:
                    check(h[a & b] == h[a] & h[b], ('meet', n, m, f, a, b))
                    check(h[a | b] == h[a] | h[b], ('join', n, m, f, a, b))
                    check(h[implication(n, a, b)] == implication(m, h[a], h[b]), ('implication', n, m, f, a, b))
                    check(h[tensor(n, a, b)] == tensor(m, h[a], h[b]), ('tensor', n, m, f, a, b))

# Exhaustively screen all 5^5 functions I(2) -> I(2), with designated core.
n = 2
D = Ds[n]
pos = {v: i for i, v in enumerate(D)}
core = set(powerset_bitmask(n, s) for s in range(1 << n))
H = set()
for f in product(range(len(D)), repeat=len(D)):
    if f[pos[1]] != pos[1]: continue
    if any(D[f[pos[c]]] not in core for c in core): continue
    good = True
    for a in D:
        for b in D:
            if any(D[f[pos[op(a, b)]]] != op(D[f[pos[a]]], D[f[pos[b]]])
                   for op in (lambda x,y:x&y, lambda x,y:x|y,
                              lambda x,y:implication(2,x,y),lambda x,y:tensor(2,x,y))):
                good = False
                break
        if not good: break
    if good: H.add(tuple(D[j] for j in f))
check(H == {tuple(lift_f(g,2,2,a) for a in D) for g in product(range(2),repeat=2)},
      'all homomorphisms for n=2')

for n in range(1,5):
    D = Ds[n]
    images = {}
    rank_counts = Counter()
    idempotents = 0
    for f in product(range(n),repeat=n):
        k = len(set(f))
        image = frozenset(lift_f(f,n,n,a) for a in D)
        rank_counts[len(image)] += 1
        part = kernel(f)
        if part in images:
            check(images[part] == image, ('image depends on kernel',n,f))
        else:
            images[part] = image
        if all(f[f[j]] == f[j] for j in range(n)):
            idempotents += 1
            check(all(lift_f(f,n,n,lift_f(f,n,n,a)) == lift_f(f,n,n,a)
                      for a in D), ('idempotent endomorphism',n,f))
    check(len(set(map(frozenset,images.values()))) == len(images),('distinct images',n))
    check(len(images) == sum(stirling(n,k) for k in range(1,n+1)),('Bell retract count',n))
    check(idempotents == sum(comb(n,k)*k**(n-k) for k in range(1,n+1)),('idempotent count',n))
    check(rank_counts == Counter({len(Ds[k]): comb(n,k)*factorial(k)*stirling(n,k)
                                 for k in range(1,n+1)}),('rank polynomial',n,rank_counts))
    for P, AP in images.items():
        for Q, AQ in images.items():
            check((AQ <= AP) == refines(P,Q),('reverse partition lattice',n,P,Q))
    print('n=%d: size=%d end=%d idempotents=%d retracts=%d rank_counts=%r' %
          (n,len(D),n**n,idempotents,len(images),dict(sorted(rank_counts.items()))))
print('VERIFY_OK %d assertions; %d constructed cross-size homomorphisms; 3125 scalar set maps screened' % (CHECKS,cross_maps))
