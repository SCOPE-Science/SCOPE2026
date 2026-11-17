#!/usr/bin/env python3
"""Standalone exact certificate for the integral homology of seven-queens on a torus.

Python 3.10+ standard library only. No network, Sage, or external data.
"""
from collections import Counter
from itertools import combinations, permutations
from math import gcd

P = 7

def admissible(face):
    rows = [z // P for z in face]
    cols = [z % P for z in face]
    return (len(set(rows)) == len(face) and len(set(cols)) == len(face)
            and len({(a-b)%P for a,b in zip(rows, cols)}) == len(face)
            and len({(a+b)%P for a,b in zip(rows, cols)}) == len(face))

# Enumeration A: independent permutation enumeration by occupied rows.
F = [set() for _ in range(P + 1)]
F[0].add(())
for k in range(1, P+1):
    for rs in combinations(range(P), k):
        for cs in permutations(range(P), k):
            f = tuple(a*P+b for a,b in zip(rs,cs))
            if admissible(f): F[k].add(f)
assert [len(a) for a in F] == [1,49,588,2156,2450,882,196,28]
assert all(tuple(f[:i]+f[i+1:]) in F[k-1]
           for k in range(1,8) for f in F[k] for i in range(k))
print('face_vector_empty_through_6', [len(a) for a in F])

# Enumeration B: independent flag/clique enumeration in a 49-vertex graph.
# Nonconflicting means differences avoid 4 attack directions.
N = 49
neighbors = [0]*N
for a in range(N):
    for b in range(N):
        if a != b and admissible((min(a,b),max(a,b))):neighbors[a] |= 1 << b
G = [set() for _ in range(8)];G[0].add(())
for k in range(1,8):
    for x in G[k-1]:
        start = x[-1]+1 if x else 0
        candidates = (1<<N)-1
        for v in x:candidates &= neighbors[v]
        for v in range(start,N):
            if (candidates>>v)&1:G[k].add(x+(v,))
assert F == G
assert sum(map(len,F)) == 6350
print('independent_flag_enumeration_agrees', True)

# Integral, unit-pivot algebraic chain cancellation. Rows and columns retain
# integer orientations; each pivot is a unit, so operations preserve homology
# over Z. The sole surviving nonunit boundary is retained and analyzed below.
original_counts = [len(x) for x in F]
unit_pairs = {}
residual = None
for k in range(7,0,-1):
    RD = {r:{} for r in sorted(F[k-1])}
    CD = {}
    for c in sorted(F[k]):
        column = {}
        for i in range(k):
            r = c[:i] + c[i+1:]
            if r in RD:
                coeff = -1 if i&1 else 1
                column[r] = coeff
                RD[r][c] = coeff
        CD[c] = column
    count = 0
    while True:
        best = None
        chosen = None
        for r, entries in RD.items():
            for c, u in entries.items():
                if abs(u) != 1:continue
                score = ((len(entries)-1)*(len(CD[c])-1),
                         len(entries)+len(CD[c]),r,c)
                if best is None or score < best:
                    best = score;chosen = (r,c,u)
        if chosen is None:break
        r,c,u = chosen
        col = CD[c]
        for j,v in list(RD[r].items()):
            if j == c:continue
            assert v%u == 0
            factor = v//u
            cj = CD[j]
            for i,w in col.items():
                new = cj.get(i,0) - factor*w
                if new:
                    cj[i] = new;RD[i][j] = new
                else:
                    cj.pop(i,None);RD[i].pop(j,None)
        for i in list(col):RD[i].pop(c,None)
        del RD[r];del CD[c]
        F[k-1].remove(r);F[k].remove(c)
        count += 1
    unit_pairs[k] = count
    remaining_nonzero = sum(map(len,CD.values()))
    if k == 4:
        assert len(RD) == 541 and len(CD) == 121
        # No further unit exists. The exact remaining boundary must be rank 1,
        # with Smith nonzero diagonal 9; verify without floating point.
        nonzero = [x for x in CD.values() if x]
        assert nonzero
        ref = nonzero[0]
        r0 = next(iter(ref));v0 = ref[r0]
        assert gcd(*ref.values()) == 9
        scalar = []
        for colj in CD.values():
            if not colj:scalar.append(0);continue
            assert all(colj.get(q,0)*v0 == ref.get(q,0)*colj.get(r0,0)
                       for q in set(ref)|set(colj))
            assert colj.get(r0,0)%v0 == 0
            scalar.append(colj[r0]//v0)
        assert gcd(*scalar) == 1
        assert gcd(*[v for colj in CD.values() for v in colj.values()]) == 9
        residual = {r:v//9 for r,v in ref.items()}
        assert gcd(*residual.values()) == 1
        print('nonunit_boundary_rank',1,'smith_invariant',9,
              'nonzero_columns',len(nonzero))
    else:
        assert remaining_nonzero == 0, (k,remaining_nonzero)
    print('boundary_cardinality',k,'unit_pairs',count,
          'remaining_columns',len(CD),'remaining_rows',len(RD))
    if k == 3:
        # Chain identity: the inherited residual C_3 cycle has zero C_2 boundary.
        assert all(sum(residual.get(c,0)*RD[r].get(c,0)
                       for c in residual) == 0 for r in RD)
        surviving = [v for r,v in residual.items() if r in F[3]]
        assert surviving in ([1],[-1]), surviving
        print('primitive_residual_kernel_generator',surviving[0])
assert [len(a) for a in F] == [0,0,0,1,121,0,0,0]
assert unit_pairs == {7:28,6:168,5:714,4:1615,3:540,2:48,1:1}
print('minimal_chain_groups', [len(a) for a in F])
print('integral_reduced_homology', 'H_2=Z/9, H_3=Z^120, others=0')

# Independent modular elimination on ORIGINAL, independently rebuilt faces.
M = G

def modular_rank(k,p):
    index = {f:i for i,f in enumerate(sorted(M[k-1]))}
    pivots = {}
    for c in sorted(M[k]):
        w = {index[c[:i]+c[i+1:]]:((-1)**i)%p for i in range(k)}
        while w:
            first = min(w)
            if first not in pivots:
                inv = pow(w[first], -1, p)
                pivots[first] = {i:(z*inv)%p for i,z in w.items()}
                break
            alpha = w[first]
            for i,z in pivots[first].items():
                val = (w.get(i,0)-alpha*z)%p
                if val:w[i] = val
                else:w.pop(i,None)
    return len(pivots)
for p, expected in [(2,[1,48,540,1616,714,168,28]),
                     (3,[1,48,540,1615,714,168,28]),
                     (5,[1,48,540,1616,714,168,28])]:
    ranks = [modular_rank(k,p) for k in range(1,8)]
    assert ranks == expected, (p,ranks)
    print('modular_boundary_ranks',p,ranks)
print('ALL_CHECKS_PASS')
