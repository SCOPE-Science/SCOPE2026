#!/usr/bin/env python3
"""Exact integer checks for divisor-parabola polygon area and boundary laws.

Independent shoelace formula, lattice-edge gcd count, and divisor-gap formula.
Finite verification supplements the separate analytical argument.
"""
from math import gcd, isqrt, lcm, pi
from fractions import Fraction


def divisors(h):
    ans = set()
    for d in range(1, isqrt(h) + 1):
        if h % d == 0:
            ans.add(d)
            ans.add(h // d)
    return sorted(ans)


def vertices(h):
    ds = divisors(h)
    # Counterclockwise: bottom, ascending positive parabola,
    # top chord, descending negative parabola.
    return [(0, -1)] + [(d, d*d) for d in ds] + [(-d, d*d) for d in reversed(ds)]


def area_shoelace(vs):
    return Fraction(abs(sum(x*y1-x1*y for (x,y),(x1,y1) in
        zip(vs, vs[1:]+vs[:1]))), 2)


def boundary_gcd(vs):
    return sum(gcd(abs(x1-x), abs(y1-y)) for (x,y),(x1,y1) in
               zip(vs, vs[1:]+vs[:1]))


def invariant_formula(h):
    ds = divisors(h)
    gap3 = sum((b-a)**3 for a,b in zip(ds, ds[1:]))
    area3 = 4*h**3 + 2 - gap3
    assert area3 % 3 == 0
    return area3//3, gap3


def is_prime(h):
    return len(divisors(h)) == 2


def check():
    count = 0
    for h in range(2, 801):
        v = vertices(h)
        a = area_shoelace(v)
        b = boundary_gcd(v)
        af,g3 = invariant_formula(h)
        assert a == af and b == 4*h
        assert af-2*h+1 >= 0  # Pick interior lattice points
        assert af >= h**3+h**2-h+1
        assert (af == h**3+h**2-h+1) == is_prime(h)
        assert len(v) == 2*len(divisors(h))+1
        # A full reciprocal mesh is a refinement of actual divisor ratios.
        full = sum((Fraction(1,k)-Fraction(1,k+1))**3
                   for k in range(1,h))
        actual = Fraction(g3, h**3)
        assert full <= actual <= Fraction((h-1)**3,h**3)
        count += 7
    # Check finite reciprocal-mesh identity and its infinite limit
    for n in [10,100]:
        s = sum((Fraction(1,k)-Fraction(1,k+1))**3
                for k in range(1,n+1))
        assert 0 < float((10-pi*pi)-float(s)) < 1/(5*n**5)
        count += 2
    # Test explicit sharpness sequences numerically. This is not their proof.
    def scaled(h):
        a,_ = invariant_formula(h)
        return a/h**3
    upper = (pi*pi-6)/3
    h = 1
    lcm_vals = []
    for n in range(2,17):
        h = lcm(h,n)
        lcm_vals.append((n,h,scaled(h)))
        assert scaled(h) > 1
        count += 1
    assert abs(lcm_vals[-1][-1]-upper) < 0.0002
    # Prime powers approach the predicted intermediate limit.
    for p in (2,3,5,7):
        target = Fraction(4,3) - Fraction((p-1)**3,3*(p**3-1))
        assert abs(scaled(p**12)-float(target)) < .00001
        count += 1
    print(f"PASS {count} exact/numeric independent checks")
    print('Lcm high-order ratio:',lcm_vals[-1], 'upper:',upper)
    print('Prime power p=2 limit:',float(Fraction(9,7)))


if __name__=='__main__':
    check()
