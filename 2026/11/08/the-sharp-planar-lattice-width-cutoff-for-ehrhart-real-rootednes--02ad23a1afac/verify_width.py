#!/usr/bin/env python3
"""Independent exact-arithmetic checks for a sharp planar Ehrhart width cutoff.

The complete proof for arbitrary lattice polygons is mathematical; this script
checks the exceptional finite normal-form table and the illustrative Ehrhart
coefficients. Requires only the Python standard library.
"""
from math import gcd

EXPECTED = {
    3: {2: (2, (1, -1))},
    5: {2: (2, (1, 0)), 3: (2, (2, -1)), 4: (2, (1, -1))},
    7: {2: (2, (1, 0)), 3: (3, (1, 0)), 4: (2, (2, -1)),
        5: (3, (1, -1)), 6: (2, (1, -1))},
    9: {2: (2, (1, 0)), 5: (2, (2, -1)), 8: (2, (1, -1))},
}

def width(D, r, a, b):
    values = (0, a, r * a + D * b)
    return max(values) - min(values)

def lattice_count(D, r, t):
    # Direct integer-point count for dilated triangle
    total = 0
    for y in range(D * t + 1):
        # Need x >= r*y/D and x <= t+(r-1)*y/D
        low = (r * y + D - 1) // D
        high = t + ((r-1)*y)//D
        total += max(0, high-low+1)
    return total

def run():
    checks = 0
    for D, cases in EXPECTED.items():
        allowed = {r for r in range(D) if gcd(r, D)==1 and gcd(r-1, D)==1}
        assert set(cases)==allowed
        checks += 1
        I = (D-1)//2
        assert 3 + 2*I - 2 == D
        # h* = (1, I, I) for B = 3
        delta = I*(I-4)
        for r,(target, u) in cases.items():
            assert gcd(*u)==1 and width(D,r,*u)==target
            checks += 1
            exhaustive = min(width(D,r,a,b) for a in range(-D,D+1)
                             for b in range(-D,D+1) if (a,b)!=(0,0) and gcd(a,b)==1)
            assert exhaustive == target
            checks += 1
            # Exact Euler/Pick evaluation vs actual points in first six dilates
            for t in range(7):
                predicted = (D*t*t+3*t+2)//2
                assert predicted == lattice_count(D,r,t), (D,r,t,predicted)
                checks += 1
            if target==3:
                assert D==7 and r in {3,5} and delta < 0
            else:
                assert not (D==7 and delta<0 and target>2)
            checks += 1
    # No direction of width <= 2 for T_(3,7) by an exhaustive
    # *a priori bounded* search: |a| <=2, |3a+7b|<=2.
    for a in range(-2,3):
        for b in range(-2,3):
            if (a,b)!=(0,0):
                assert width(7,3,a,b)>2
                checks += 1
    # Integer unimodular equivalence T_(3,7) -> T_(5,7).
    U=((5,-2),(-7,3))
    assert U[0][0]*U[1][1]-U[0][1]*U[1][0] == 1
    assert (U[0][0]*3+U[0][1]*7, U[1][0]*3+U[1][1]*7)==(1,0)
    assert (U[0][0],-U[1][0])==(5,7)
    checks += 3
    print(f'PASS {checks} finite exact arithmetic checks')

if __name__=='__main__':
    run()
