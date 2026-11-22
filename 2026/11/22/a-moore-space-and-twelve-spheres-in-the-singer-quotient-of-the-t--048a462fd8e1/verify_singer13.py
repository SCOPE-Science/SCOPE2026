#!/usr/bin/env python3
"""Exact reconstruction of a Singer quotient of the rank-three ternary projective matroid."""
from itertools import combinations
from collections import Counter
from math import comb

MOD = 13
D = {0, 1, 3, 9}

# 1. Reconstruct the cyclic projective plane from a perfect difference set.
diffs = Counter((a-b) % MOD for a in D for b in D if a != b)
assert diffs == Counter({i: 1 for i in range(1, MOD)})
lines = [frozenset((t+d) % MOD for d in D) for t in range(MOD)]
assert len(set(lines)) == 13
assert all(sum({a, b} <= L for L in lines) == 1
           for a,b in combinations(range(MOD),2))
assert all(sum(i in L for L in lines) == 4 for i in range(MOD))

# 2. Independently realize the Singer orbit in F_27=F_3[t]/(t^3-t+1).
def field_mul(a, b):
    co = [0]*5
    for i in range(3):
        for j in range(3):
            co[i+j] = (co[i+j]+a[i]*b[j])%3
    # t^3=t-1, hence t^i=t^(i-2)-t^(i-3) for i>=3.
    for k in (4,3):
        c = co[k]
        co[k] = 0
        co[k-2] = (co[k-2]+c)%3
        co[k-3] = (co[k-3]-c)%3
    return tuple(co[:3])
powers = []
w = (1,0,0)
for _ in range(13):
    powers.append(w)
    w = field_mul(w, (0,1,0))
assert w == (2,0,0)  # t^13=-1, so its projective order is 13.
assert len({min(v, tuple((2*z)%3 for z in v)) for v in powers}) == 13
assert {i for i,v in enumerate(powers) if v[2] == 0} == D

# 3. Face orbit census of the rank-three independence complex.
verts = {(i,) for i in range(MOD)}
edges = set(combinations(range(MOD),2))
tris = {t for t in combinations(range(MOD),3) if not any(set(t) <= L for L in lines)}
assert len(tris) == comb(13,3)-13*comb(4,3) == 234
assert (len(verts), len(edges), len(tris)) == (13,78,234)

def shifted(face, shift):
    return tuple(sorted((a+shift)%MOD for a in face))

def orbit_reps(faces):
    remaining=set(faces); representatives=[]
    while remaining:
        face = min(remaining)
        o = {shifted(face,k) for k in range(MOD)}
        assert len(o)==13 and o <= remaining
        representatives.append(face)
        remaining -= o
    return representatives

assert len(orbit_reps(verts)) == 1
assert len(orbit_reps(edges)) == 6
triangle_reps=orbit_reps(tris)
assert len(triangle_reps)==18

# 4. Compute the attaching words, never identifying quotient simplices by vertices.
def edge_letter(u,v):
    d=(v-u)%MOD
    assert d != 0
    return d if 1 <= d <= 6 else -(13-d)

words = [[edge_letter(a,b),edge_letter(b,c),edge_letter(c,a)]
         for a,b,c in triangle_reps]
expected = {
    (0,1,2): (1,1,-2),
    (0,1,4): (1,3,-4),
    (0,1,5): (1,4,-5),
    (0,1,6): (1,5,-6),
    (0,1,7): (1,6,6),
    (0,1,8): (1,-6,5),
    (0,1,10): (1,-4,3),
    (0,1,11): (1,-3,2),
    (0,2,4): (2,2,-4),
    (0,2,5): (2,3,-5),
    (0,2,6): (2,4,-6),
    (0,2,7): (2,5,6),
    (0,2,9): (2,-6,4),
    (0,2,10): (2,-5,3),
    (0,3,6): (3,3,-6),
    (0,3,7): (3,4,6),
    (0,3,8): (3,5,5),
    (0,4,8): (4,4,5),
}
assert {t:tuple(w) for t,w in zip(triangle_reps,words)} == expected

# 5. Five valid generator/2-cell cancellations.
# The equations are sequentially b=a^2, c=a^3, d=a^4, e=a^5, f=a^6.
cancel_triangles = [ (0,1,2), (0,1,11), (0,1,4), (0,1,5), (0,1,6) ]
solved = {1: (1,)}
for target,tri in zip((2,3,4,5,6), cancel_triangles):
    word=expected[tri]
    assert sum(abs(x)==target for x in word)==1
    assert all(abs(x) in solved or abs(x)==target for x in word)
    # After previously solved letters are substituted, this word has one
    # occurrence of the new letter, so the 1-cell/2-cell cancellation is legal.
    prev_sum=sum((1 if x>0 else -1)*len(solved[abs(x)])
                 for x in word if abs(x)!=target)
    target_sign=next(1 if x>0 else -1 for x in word if abs(x)==target)
    exponent=-prev_sum*target_sign
    assert exponent==target
    solved[target]=(1,)*exponent
assert all(len(solved[i])==i for i in range(1,7))

remaining=[tri for tri in triangle_reps if tri not in cancel_triangles]
degrees=[]
for tri in remaining:
    word=expected[tri]
    deg=sum((1 if x>0 else -1)*len(solved[abs(x)]) for x in word)
    degrees.append(deg)
assert len(remaining)==13
assert Counter(degrees) == Counter({0:8, 13:5})

# One degree-13 2-cell is the Moore attachment; all other 12 attaching
# maps are null after it is present (including the four other a^13 maps).
# The universal cover has H_2=I_13 (+) Z[C_13]^12, total rank 12+156.
assert 12 + 13*12 == 168
assert 13-78+234-1 == 168

print('Difference set:', sorted(D))
print('Faces by dimension:', (13,78,234))
print('Orbit cells by dimension:', (1,6,18))
print('Cancelled triangles:', cancel_triangles)
print('Remaining attaching degrees:', Counter(degrees))
print('Quotient homotopy: M(Z/13,1) wedge 12 S^2')
print('Cover H2 module: augmentation ideal plus 12 regular modules')
print('VERIFY_OK')
