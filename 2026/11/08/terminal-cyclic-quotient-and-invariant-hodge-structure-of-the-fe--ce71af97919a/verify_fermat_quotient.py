#!/usr/bin/env python3
"""Exact finite combinatorial checks for a cyclic quotient of a Fermat quartic threefold.

Execute with Python 3 standard library; the all-characteristic geometric statements
are established separately by the written proof, not by these finite checks.
"""
from itertools import product
from math import comb

PRIME = 5
DEGREE = 4

def eigen_checks():
    exceptional = []
    for k in range(PRIME):
        # Eigenline v_k=(1,zeta^k,...,zeta^(4k)).
        # Its Fermat value is sum of characters 4*k*j over j=0..4.
        counts = [sum((DEGREE*k*j) % PRIME == r for j in range(PRIME))
                  for r in range(PRIME)]
        on_hypersurface = len(set(counts)) == 1
        assert on_hypersurface == (k != 0), (k, counts)
        if not on_hypersurface:
            continue
        # In the eigenbasis the tangent derivative in eigen-direction j
        # is nonzero exactly for (j+3*k) divisible by five.
        excluded = (-3*k) % PRIME
        assert excluded != k
        weights = tuple(sorted((j-k) % PRIME for j in range(PRIME)
                               if j not in (k, excluded)))
        # Independently re-select a cyclic-group generator to compare types.
        reduced = tuple(sorted((w*pow(k, -1, PRIME)) % PRIME for w in weights))
        assert reduced == (2, 3, 4), (k, weights, reduced)
        assert all(sum((a*w) % PRIME for w in weights) > PRIME
                   for a in range(1, PRIME)), (k, weights)
        exceptional.append((k, weights))
    assert len(exceptional) == 4
    print('FOUR_TERMINAL_QUOTIENT_POINTS_OK', exceptional)


def hodge_checks():
    # Griffiths residue description for a quartic threefold:
    # H^{2,1} corresponds to degree-three monomials in the Jacobian ring
    # C[x_0,...,x_4]/(x_0^3,...,x_4^3).
    exponents = {v for v in product(range(3), repeat=5) if sum(v) == 3}
    assert len(exponents) == 30
    seen, orbits = set(), []
    for v in sorted(exponents):
        if v in seen:
            continue
        orb = set()
        t = v
        for _ in range(5):
            orb.add(t)
            t = (t[-1],) + t[:-1]
        assert t == v and len(orb) == 5
        seen.update(orb)
        orbits.append(orb)
    assert seen == exponents and len(orbits) == 6
    assert all(sum(tuple(v[(j-i) % 5] for j in range(5)) == v
                   for v in exponents) == 0 for i in range(1,5))
    print('H21_INVARIANT_DIMENSION_OK', len(orbits))


def topology_checks():
    # Euler characteristic c_3(T_X)H^3 for a quartic in P^4.
    c3 = sum(comb(5,3-i)*(-DEGREE)**i for i in range(4))
    assert c3 == -14
    e_x = c3 * DEGREE
    assert e_x == -56
    b3 = 4-e_x
    assert b3 == 60
    e_y = (e_x + 4*4)//5
    assert (e_x + 4*4) % 5 == 0 and e_y == -8
    e_str = (e_x + (25-1)*4)//5
    assert (e_x + (25-1)*4) % 5 == 0 and e_str == 8
    assert (4-2*6) == e_y
    from fractions import Fraction
    assert Fraction(4, 5) == Fraction(DEGREE, PRIME)
    print('QUOTIENT_EULER_AND_VOLUME_OK', e_y, e_str, 'anticanonical_volume=4/5')

if __name__ == '__main__':
    eigen_checks()
    hodge_checks()
    topology_checks()
    print('VERIFY_OK')
