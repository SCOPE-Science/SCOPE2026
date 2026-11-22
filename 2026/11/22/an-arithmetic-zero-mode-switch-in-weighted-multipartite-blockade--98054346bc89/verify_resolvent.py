"""Independent exact resolvent/Schur verification, with rational sample energies.

Requires Python 3 and sympy. Run: python verify_resolvent.py
"""
from itertools import product
import sympy as S


def from_independent_sets(parts):
    # Build configuration graph by explicit independent set tests.
    length = sum(len(p) for p in parts)
    starts = [sum(len(p) for p in parts[:i]) for i in range(len(parts))]
    allowed = []
    for mask in range(1 << length):
        occupied_parts = sum(any(mask & (1 << (a+j)) for j in range(len(p)))
                             for a, p in zip(starts, parts))
        if occupied_parts <= 1:
            allowed.append(mask)
    idx = {x:i for i,x in enumerate(allowed)}
    H = S.zeros(len(allowed))
    for i, x in enumerate(allowed):
        for a, p in zip(starts, parts):
            for j, w in enumerate(p):
                y = x ^ (1 << (a+j))
                if y in idx:
                    H[i,idx[y]] = S.Rational(w)
    return H


def cube_green(part, z):
    weighted_eigs = [sum(s*w for s,w in zip(signs,part))
                     for signs in product((1,-1), repeat=len(part))]
    return sum((1/(z-e) for e in weighted_eigs), S.Integer(0))/len(weighted_eigs)

CASES = [
 ((1,),(1,),(1,)),
 ((1,1),(1,1),(1,1)),
 ((1,1,2),(1,1),(1,1,1,1)),
 ((1,1,3),(1,1),(1,1,1,1)),
 ((1,2,3),(1,1),(1,1,2)),
 ((1,1),(2,2),(1,2)),
 ((1,2),(2,3),(1,)),
 ((1,1),(1,1),(1,1),(1,)),
]
ENERGIES = (S.Rational(1, 7), S.Rational(5, 13), S.Rational(11, 17))

if __name__=='__main__':
    count = 0
    for parts in CASES:
        H = from_independent_sets(parts)
        for z in ENERGIES:
            green_direct = (z*S.eye(H.rows)-H).inv()[0,0]
            local = [cube_green(part,z) for part in parts]
            green_glued = 1/(sum(1/g for g in local)-(len(parts)-1)*z)
            assert S.cancel(green_direct-green_glued) == 0, (parts,z)
            count += 1
        print('PASS', [list(p) for p in parts], 'three rational resolvent energies')
    print('ALL PASS', count, 'exact resolvent comparisons')
