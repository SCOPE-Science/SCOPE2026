#!/usr/bin/env python3
"""Exhaustive projective-incidence certificate for tangent-filling cubics over F3.

Run: python3 verify_tangent_cubics_f3.py
Only the Python standard library is required. All arithmetic is exact over F3.
"""
from itertools import product
from collections import Counter

Q = 3

def canon(v):
    a = next((x % Q for x in v if x % Q), None)
    if a is None:
        raise ValueError('zero projective vector')
    return tuple((x * (1 if a == 1 else 2)) % Q for x in v)

points = sorted({canon(v) for v in product(range(Q), repeat=3) if any(v)})
assert len(points) == 13
point_id = {v: i for i, v in enumerate(points)}
monomials = [(i, j, 3-i-j) for i in range(4) for j in range(4-i)]
assert len(monomials) == 10

def pow0(a, n):
    return pow(a, n, Q) if n else 1

def mon_value(p, e):
    ans = 1
    for a, t in zip(p, e):
        ans = ans * pow0(a, t) % Q
    return ans

values = [[mon_value(p, e) for e in monomials] for p in points]
gradients = []
for p in points:
    partials = []
    for j in range(3):
        row = []
        for e in monomials:
            if e[j] == 0:
                row.append(0)
            else:
                d = list(e)
                d[j] -= 1
                row.append(e[j] * mon_value(p, d) % Q)
        partials.append(row)
    gradients.append(partials)

line_masks = {}
for line in points:
    mask = 0
    for idx, p in enumerate(points):
        if sum(a*b for a, b in zip(line, p)) % Q == 0:
            mask |= (1 << idx)
    assert mask.bit_count() == 4
    line_masks[line] = mask

all_points_mask = (1 << len(points)) - 1

# Each scalar class of nonzero ternary cubic forms appears once.
# The normal form has its first nonzero coefficient equal to one.
def coefficient_vectors():
    for k in range(1, Q**len(monomials)):
        c = tuple(k // Q**j % Q for j in range(len(monomials)))
        if next(a for a in c if a) == 1:
            yield c


def tangent_data(c):
    tangent_lines = set()
    npoints = 0
    for m, partial in zip(values, gradients):
        if sum(a*b for a,b in zip(c,m)) % Q != 0:
            continue
        npoints += 1
        g = tuple(sum(a*b for a,b in zip(c, row)) % Q for row in partial)
        if any(g):
            tangent_lines.add(canon(g))
    covered = 0
    for line in tangent_lines:
        covered |= line_masks[line]
    return npoints, len(tangent_lines), covered == all_points_mask

candidates = {}
number_of_forms = 0
for c in coefficient_vectors():
    number_of_forms += 1
    n, nt, filling = tangent_data(c)
    if filling:
        candidates[c] = (n, nt)
assert number_of_forms == (3**10 - 1)//2 == 29524
assert Counter(candidates.values()) == {(4,4):936, (6,6):1872, (7,7):936}
assert len(candidates) == 3744

# Evaluation on the 13 rational points is injective on ternary cubics;
# this is also verified exhaustively on all normalized coefficient vectors.
# The only nonzero forms vanishing on all rational points have degree >=4.
weights = tuple(3**j for j in range(len(points)))
def evaluation_key(v):
    v = tuple(int(a) for a in v)
    leading = next(a for a in v if a)
    factor = 1 if leading == 1 else 2
    return sum((a*factor % 3)*b for a,b in zip(v,weights))

def evaluate(c):
    return tuple(sum(a*b for a,b in zip(c,row)) % Q for row in values)

all_evals = {evaluation_key(evaluate(c)) for c in coefficient_vectors()}
assert len(all_evals) == number_of_forms
candidate_keys = {evaluation_key(evaluate(c)): (c, dat) for c,dat in candidates.items()}
assert len(candidate_keys) == len(candidates)

# Enumerate PGL_3(F3) by invertible 3x3 matrices modulo nonzero scalars.
projective_actions = []
for entries in product(range(Q),repeat=9):
    if not any(entries) or next(t for t in entries if t) != 1:
        continue
    a,b,c,d,e,f,g,h,i = entries
    det=(a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)) % 3
    if not det:
        continue
    matrix=(entries[:3],entries[3:6],entries[6:])
    perm=[]
    scale=[]
    for p in points:
        raw=tuple(sum(row[j]*p[j] for j in range(3))%3 for row in matrix)
        t=next(v for v in raw if v)
        perm.append(point_id[canon(raw)])
        scale.append(t) # Homogeneity: degree 3, so t^3=t in F3.
    projective_actions.append((tuple(perm),tuple(scale)))
assert len(projective_actions) == 5616

representatives = [
    ((0,0,0,1,1,0,0,0,2,0),4,936),
    ((0,0,1,0,1,1,0,0,1,0),6,1872),
    ((0,0,0,1,1,0,0,1,2,0),7,936),
]
covered_keys = set()
for rep, expected_points, expected_orbit in representatives:
    assert candidates[rep] == (expected_points,expected_points)
    original_eval=evaluate(rep)
    orbit=set()
    for perm,scale in projective_actions:
        transformed=[original_eval[perm[j]]*scale[j]%3 for j in range(13)]
        orbit.add(evaluation_key(transformed))
    expected={k for k,(form,dat) in candidate_keys.items() if dat[0]==expected_points}
    assert len(orbit)==expected_orbit
    assert orbit==expected
    assert not (orbit & covered_keys)
    covered_keys |= orbit
    print('rational_points=%d forms=%d projective_stabilizer=%d' % (
          expected_points,len(orbit),len(projective_actions)//len(orbit)))
assert covered_keys==set(candidate_keys)

# These three representative cubics are geometrically smooth:
# For the first and third, Fy=-x^2, Fx|_(x=0)=z^2, F|_(x=z=0)=y^3.
# For the middle, Fx,Fy,Fz have no common zero on the cubic: x=0
# is impossible; x=1 forces z=y^2+y and y^3-y=1; then
# F=y^2+y+1=(y-1)^2, incompatible with y^3-y=1.
print('TANGENT_FILLING_CUBICS_F3_CLASSIFICATION_PASS')
