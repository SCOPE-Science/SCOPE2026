#!/usr/bin/env python3
"""Exhaustive exact integer certificate for cuboctahedral Ising one-spin barriers.
Only Python standard library.  All continuum statements reduce to endpoint
inequalities for affine functions of x=h/J.
"""
from collections import Counter, deque
from itertools import product, permutations

# First realization: cuboctahedron as the line graph of the 3-cube.
E = sorted((u, u ^ (1 << axis)) for u in range(8)
           for axis in range(3) if not (u & (1 << axis)))
assert len(E) == 12
A = [set() for _ in E]
for i, (u, v) in enumerate(E):
    for j, (p, q) in enumerate(E):
        if i != j and len({u, v}.intersection((p, q))) == 1:
            A[i].add(j)
assert all(len(nei) == 4 for nei in A)
assert sum(map(len, A)) // 2 == 24

# Second realization: the 12 vectors (0,+/-1,+/-1) and permutations,
# with edges at squared Euclidean distance 2.  Match a cube edge to its
# midpoint in the coordinates of its endpoint vertices.
midpoints = []
for u, v in E:
    xyz = tuple(((1 if u & (1 << k) else -1) +
                 (1 if v & (1 << k) else -1)) // 2 for k in range(3))
    midpoints.append(xyz)
assert len(set(midpoints)) == 12
assert sorted(midpoints) == sorted(tuple((0 if k == axis else sign[k if k < axis else k-1])
                                        for k in range(3))
                                     for axis in range(3)
                                     for sign in product((-1, 1), repeat=2))
B = [set(j for j, w in enumerate(midpoints) if j != i and
         sum((z-t)**2 for z,t in zip(w,v)) == 2)
     for i,v in enumerate(midpoints)]
assert A == B

N = 1 << 12
S = [tuple(1 if mask >> i & 1 else -1 for i in range(12)) for mask in range(N)]
M = [sum(s) for s in S]
E0 = [sum(s[i]*s[j] for i in range(12) for j in A[i] if i < j) for s in S]

def val(mask, x):  # x an integer: all energies are exact integers.
    return E0[mask] - x*M[mask]

def weak(mask, x):
    s=S[mask]
    return all(s[i]*(x-sum(s[j] for j in A[i])) >= 0 for i in range(12))

def strict(mask, x):
    s=S[mask]
    return all(s[i]*(x-sum(s[j] for j in A[i])) > 0 for i in range(12))

# All possible positive threshold fields of a local flip are 2,4;
# zero is also a threshold because every vertex has degree 4.
assert all(abs(sum(S[mask][j] for j in A[i])) in (0,2,4)
           for mask in range(N) for i in range(12))

assert {x: sum(weak(mask,x) for mask in range(N))
        for x in (0,2,4)} == {0:458,2:185,4:108}
assert {x: sum(strict(mask,x) for mask in range(N))
        for x in (0,2,4)} == {0:0,2:9,4:0}

# Ground-state affine lower envelope checked at field endpoints.
ground = [mask for mask in range(N) if E0[mask] == -8 and M[mask] == 4]
assert len(ground) == 9
assert min(E0) == -8
assert min(val(mask,4) for mask in range(N)) == -24
assert all(E0[mask] >= -8 and val(mask,4) >= -24 for mask in range(N))
assert all(val(mask,4) >= val(N-1,4) for mask in range(N))
# At x>4 the all-up state wins since its M=12 is maximal.

low = [mask for mask in range(N) if strict(mask,1)]
high = [mask for mask in range(N) if strict(mask,3)]
assert len(low) == 45 and Counter((E0[q],M[q]) for q in low) == {(-8,2):36,(-8,4):9}
assert len(high) == 17 and Counter((E0[q],M[q]) for q in high) == {(0,6):8,(-8,4):9}
assert len([q for q in range(N) if strict(q,5)]) == 1
low_traps = [q for q in low if q not in ground]
high_traps = [q for q in high if q not in ground]
assert len(low_traps)==36 and len(high_traps)==8

# For each affine barrier branch, *every* lower bound holds on its two
# closed endpoints, and every upper-bound path does too. Therefore they
# hold throughout each open interval; no floating-point interpolation.
intervals = ((0,1,0,2,low_traps),(1,2,2,0,low_traps),
             (2,3,0,2,high_traps),(3,4,2,0,high_traps))
all_paths = {}
for lo, hi, blo, bhi, traps in intervals:
    paths = []
    for start in traps:
        # A path must pay the first flip. Prove that the *minimum* cost
        # of a first flip equals the claimed barrier affine function.
        flipped = [start^(1<<i) for i in range(12)]
        assert all(val(v,lo)-val(start,lo) >= blo for v in flipped)
        assert all(val(v,hi)-val(start,hi) >= bhi for v in flipped)
        assert any(val(v,lo)-val(start,lo)==blo and
                   val(v,hi)-val(start,hi)==bhi for v in flipped)

        # Construct a 3-flip path to a genuine ground configuration with
        # a maximum energy no greater than this same affine barrier.
        good = {v for v in range(N)
                if val(v,lo)-val(start,lo)<=blo and
                   val(v,hi)-val(start,hi)<=bhi}
        queue = deque([start]); prev={start:None}; endpoint=None
        while queue:
            v=queue.popleft()
            if v in ground:
                endpoint=v
                break
            for i in range(12):
                w=v^(1<<i)
                if w in good and w not in prev:
                    prev[w]=v;queue.append(w)
        assert endpoint is not None
        path=[];v=endpoint
        while v is not None:
            path.append(v);v=prev[v]
        path.reverse()
        assert len(path)==4
        paths.append(path)
    all_paths[(lo,hi)] = paths
    print('FIELD',lo,hi,'TRAPS',len(traps),'PATHS_CERTIFIED',len(paths),
          'MAX_FLIPS',max(len(p)-1 for p in paths),'REPRESENTATIVE',paths[0])

# Cubic symmetry orbits for the 36 low-field traps and 8 high-field traps.
automorphisms=[]
for perm in permutations(range(3)):
  for signs in product((-1,1),repeat=3):
    transformed=[tuple(signs[k]*v[perm[k]] for k in range(3)) for v in midpoints]
    automorphisms.append(tuple(midpoints.index(v) for v in transformed))
assert len(set(automorphisms))==48
for trap_set,expected in ((set(low_traps),[12,24]),(set(high_traps),[8])):
    unseen=set(trap_set); orbits=[]
    while unseen:
        q=next(iter(unseen))
        orbit={sum((1<<p[i]) for i in range(12) if q>>i&1)
               for p in automorphisms}
        assert orbit <= trap_set
        orbits.append(len(orbit)); unseen-=orbit
    assert sorted(orbits)==expected
    print('TRAP_ORBIT_SIZES',sorted(orbits))

# 9 ground states correspond to perfect matchings of the 3-cube.
for q in ground:
    minus={i for i,s in enumerate(S[q]) if s==-1}
    assert len(minus)==4 and all(not(minus & A[i]) for i in minus)
for q in high_traps:
    minus={i for i,s in enumerate(S[q]) if s==-1}
    assert len(minus)==3 and all(not(minus & A[i]) for i in minus)
    assert all(A[i]&minus for i in range(12) if i not in minus)
print('CUBOCTAHEDRON_EXACT_CONTINUUM_BARRIER_CERTIFICATE_PASSED',
      'states',N,'endpoint_reachability_checks',sum(map(len,all_paths.values())))
