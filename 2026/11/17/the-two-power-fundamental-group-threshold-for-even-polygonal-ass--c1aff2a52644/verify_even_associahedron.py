#!/usr/bin/env python3
"""Finite verification of dihedral fixed-subspace dimensions for polygon associahedra.

This checker independently counts permutation orbits on the polygon vertices,
subtracts the invariant affine-function dimensions, and compares the result
with the Fourier-coordinate decomposition of the reduced representation.
It corroborates, but does not replace, the general proof.
"""
from math import gcd


def divisors(n):
    return [q for q in range(1, n+1) if n % q == 0]


def orbit_count(n, generators):
    unseen = set(range(n))
    count = 0
    while unseen:
        start = min(unseen)
        stack = [start]
        seen = {start}
        while stack:
            v = stack.pop()
            for f in generators:
                w = f(v) % n
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        unseen -= seen
        count += 1
    return count


def permutation_fixed_dim(n, q, a=None):
    m = n // q
    gens = [lambda i, m=m: i+m]
    if a is not None:
        gens.append(lambda i, a=a: a-i)
    orbits = orbit_count(n, gens)
    # Affine functions on the regular polygon: constants always; the two
    # planar coordinate functions have fixed dimension 2 for trivial action,
    # 1 for one reflection, and 0 for a nontrivial rotation subgroup.
    affine_dim = (2 if a is None else 1) if q == 1 else 0
    return orbits - 1 - affine_dim


def fourier_fixed_dim(n, q, a=None):
    m = n // q
    surviving = sum(1 for k in range(2, n//2) if k % q == 0)
    sign_survives_rotation = (m % 2 == 0)
    if a is None:
        return 2*surviving + int(sign_survives_rotation)
    return surviving + int(sign_survives_rotation and a % 2 == 0)


def predicted_cyclic_pi1_order(n):
    fixed_exponents = [a for a in range(1,n)
                       if permutation_fixed_dim(n,n//gcd(n,a)) > 0]
    g=n
    for a in fixed_exponents:
        g=gcd(g,a)
    return g


def theorem_cyclic_pi1_order(n):
    power_of_two = n & (n-1) == 0
    return 2 if power_of_two else 1


def run():
    comparisons=0
    for n in range(6,101,2):
        for q in divisors(n):
            u=permutation_fixed_dim(n,q)
            v=fourier_fixed_dim(n,q)
            assert u==v, ('cyclic',n,q,u,v)
            comparisons+=1
            for a in range(n//q):
                u=permutation_fixed_dim(n,q,a)
                v=fourier_fixed_dim(n,q,a)
                assert u==v, ('dihedral',n,q,a,u,v)
                # The whole dihedral subgroup may have no common fixed point.
                # Its two generating reflections each have individual fixed points.
                comparisons+=1
        assert all(permutation_fixed_dim(n,1,a)>0 for a in range(n))
        actual=predicted_cyclic_pi1_order(n)
        assert actual == theorem_cyclic_pi1_order(n), ('cyclic pi1',n,actual)
    print('All even polygon sizes 6..100 passed; fixed-subspace comparisons:',comparisons)
    for n in (6,8,10,12,16,18,24,32,64):
        print('n=%d; full-rotation quotient pi1 order=%d; all reflection subgroups have fixed points' %
              (n,predicted_cyclic_pi1_order(n)))

if __name__=='__main__':
    run()
