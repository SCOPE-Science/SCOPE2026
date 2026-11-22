#!/usr/bin/env python3
"""Exact graph-pegging reach and Fano symmetry census. Python 3, standard library only."""
from functools import lru_cache
from itertools import combinations
from collections import Counter

N = 14
ALL = (1 << N) - 1
p = lambda x: x.bit_count() & 1
# Vertices 0..6: points represented by nonzero binary vectors 1..7.
# Vertices 7..13: lines with normal vectors 1..7.
neighbor = [set() for _ in range(N)]
for a in range(7):
    for b in range(7):
        if p((a + 1) & (b + 1)) == 0:
            neighbor[a].add(7 + b)
            neighbor[7 + b].add(a)
assert all(len(x) == 3 for x in neighbor)
moves = [(a,b,c) for a in range(N) for b in neighbor[a]
         for c in neighbor[b] if a != c]
assert len(moves) == 84

@lru_cache(None)
def reach(mask):
    r = mask
    for a,b,c in moves:
        if (mask >> a & 1) and (mask >> b & 1) and not (mask >> c & 1):
            r |= reach(mask ^ (1 << a) ^ (1 << b) ^ (1 << c))
    return r

def tup_mask(indices):
    return sum(1 << i for i in indices)

def linear_automorphisms():
    out = set()
    for a in range(1, 8):
        for b in range(1, 8):
            for c in range(1, 8):
                if len({0,a,b,c,a^b,a^c,b^c,a^b^c}) != 8:
                    continue
                def act(x):
                    return (a if x&1 else 0) ^ (b if x&2 else 0) ^ (c if x&4 else 0)
                def dual(x):
                    return next(y for y in range(1,8) if
                                all(p(y & act(e)) == p(x & e)
                                    for e in (1,2,4)))
                first = tuple(act(x)-1 for x in range(1,8))
                second = tuple(6+dual(x) for x in range(1,8))
                out.add(first+second)
                out.add(tuple(x+7 for x in first)+tuple(x-7 for x in second))
    assert len(out) == 336
    for perm in out:
        assert len(set(perm)) == 14
        for x in range(14):
            assert {perm[y] for y in neighbor[x]} == neighbor[perm[x]]
    return sorted(out)

AUTOS = linear_automorphisms()
def orbit(mask):
    return {tup_mask(perm[i] for i in range(N) if mask>>i&1) for perm in AUTOS}

def orbit_decomposition(masks):
    pending = set(masks)
    results = []
    while pending:
        rep = min(pending)
        o = orbit(rep)
        assert o <= pending
        pending -= o
        results.append((rep, len(o)))
    return sorted(results, key=lambda t: (-t[1], t[0]))

def pp(mask):
    return ','.join(('P'+str(i+1)) if i<7 else ('L'+str(i-6))
                    for i in range(N) if mask>>i&1)

sets = [set() for _ in range(N+1)]
full = [set() for _ in range(N+1)]
minimal = [set() for _ in range(N+1)]
for mask in range(1 << N):
    k = mask.bit_count()
    sets[k].add(mask)
    if reach(mask) == ALL:
        full[k].add(mask)
for k in range(1,N+1):
    minimal[k] = {m for m in full[k]
                  if all((m^(1 << i)) not in full[k-1]
                         for i in range(N) if m>>i&1)}

assert [len(x) for x in full] == [0,0,0,0,336,1862,2989,3430,3003,2002,1001,364,91,14,1]
assert [(k,len(x)) for k,x in enumerate(minimal) if x] == [(4,336),(5,434)]
assert all(reach(m)!=ALL for m in sets[3])

# Four-peg structural criterion: two points, two lines, incidences
# form K2+2K1, 2K2, or P4, excluding a two-edge wedge.
def four_criterion(m):
    if (m&127).bit_count()!=2 or (m>>7).bit_count()!=2:
        return False
    chosen_p = [i for i in range(7) if m>>i&1]
    chosen_l = [i for i in range(7,14) if m>>i&1]
    es=[(a,b) for a in chosen_p for b in chosen_l if b in neighbor[a]]
    if len(es) in (1,3):
        return True
    if len(es)==2:
        return es[0][0]!=es[1][0] and es[0][1]!=es[1][1]
    return False
assert all((m in full[4]) == four_criterion(m) for m in sets[4])
assert [count for count in (len(orbit(m)) for m in full[4])]  # evaluated
orbits4 = orbit_decomposition(full[4]); orbits5 = orbit_decomposition(minimal[5])
assert sorted(s for _,s in orbits4) == [84,84,168]
assert sorted(s for _,s in orbits5) == [42,56,168,168]

# Six and seven pegs fail precisely for independent sets.
for k in (6,7):
    assert all((reach(m)!=ALL)==all(not (neighbor[i] & {j for j in range(N) if m>>j&1}) for i in range(N) if m>>i&1)
               for m in sets[k])
# Five-peg failures with an edge: precisely a Fano quadrangle plus a secant
# line, or the point-line dual (84 configurations).
bad5 = sets[5]-full[5]
assert len(bad5)==140
def independent(m):
    return not any((m>>i & 1) and (m>>j & 1)
                   for i in range(N) for j in neighbor[i])
def quadrangle_secant(m):
    pset=[i+1 for i in range(7) if m>>i&1]
    lset=[i-6 for i in range(7,14) if m>>i&1]
    if len(pset)==4 and len(lset)==1:
        base, other=pset,lset[0]
    elif len(lset)==4 and len(pset)==1:
        base, other=lset,pset[0]
    else:
        return False
    return all((a^b^c)!=0 for a,b,c in combinations(base,3)) and sum(p(x & other)==0 for x in base)==2
assert len([m for m in bad5 if quadrangle_secant(m)])==84
assert all((m in bad5)==(independent(m) or quadrangle_secant(m)) for m in sets[5])

print('graph: Fano incidence (14 vertices, 21 edges), 336 verified automorphisms')
print('reach counts:', [len(x) for x in full])
print('minimal counts:', [(k,len(x)) for k,x in enumerate(minimal) if x])
print('optimal 4 representatives (orbit size, vertex set):')
for m,s in orbits4:print(s, pp(m))
print('minimal 5 representatives (orbit size, vertex set):')
for m,s in orbits5:print(s, pp(m))
print('4-set structural criterion: verified for all',len(sets[4]),'sets')
print('maximum non-universally-reaching size:',max(k for k in range(15) if sets[k]-full[k]))
print('PASS')
