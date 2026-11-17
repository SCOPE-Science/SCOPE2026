#!/usr/bin/env python3
"""Exhaustive smooth-cubic census over F3 modulo PGL3(F3).

Requires SymPy. Run from the same directory as verify_tangent_cubics_f3.py:
    python3 verify_all_smooth_cubics_f3.py
The 25 exact orbit representatives are checked by Groebner ideals in
all three affine projective charts. No numerical approximation is used.
"""
from collections import Counter
import sympy as sp
import verify_tangent_cubics_f3 as v

key_to_coeff = {v.evaluation_key(v.evaluate(c)): c for c in v.coefficient_vectors()}
remaining = set(key_to_coeff)
x, y, z = sp.symbols('x y z')
coords = (x, y, z)
monomials = [x**a*y**b*z**c for a,b,c in v.monomials]
counts = Counter()
all_classes = 0
smooth_classes = 0
while remaining:
    key = next(iter(remaining))
    coeff = key_to_coeff[key]
    f_eval = v.evaluate(coeff)
    orbit = {
        v.evaluation_key([f_eval[p[j]]*sc[j]%3 for j in range(13)])
        for p, sc in v.projective_actions
    }
    assert orbit <= remaining
    remaining -= orbit
    all_classes += 1
    poly = sum(int(a)*m for a,m in zip(coeff, monomials))
    equations = [poly] + [sp.diff(poly, w) for w in coords]
    smooth = True
    for chart in coords:
        variables = tuple(w for w in coords if w != chart)
        basis = sp.groebner([e.subs(chart, 1) for e in equations],
                           *variables, modulus=3)
        unit = sp.Poly(1, *variables, modulus=3)
        if basis.polys != [unit]:
            smooth = False
            break
    if smooth:
        smooth_classes += 1
        n, tangent_count, filling = v.tangent_data(coeff)
        counts[(n, filling)] += len(orbit)
assert not remaining
assert all_classes == 25
assert smooth_classes == 10
assert sum(counts.values()) == 16848
assert sum(weight for (n, filling), weight in counts.items() if filling) == 3744
assert counts[(4,True)] == 936 and counts[(6,True)] == 1872 and counts[(7,True)] == 936
assert counts[(4,False)] == 2808 and counts[(6,False)] == 936
print('smooth_classes=10 total_classes=25 smooth_forms=16848')
print('tangent_filling_forms=3744 smooth_conditional_fraction=2/9')
print('SMOOTH_CUBIC_ORBIT_CENSUS_F3_PASS')
