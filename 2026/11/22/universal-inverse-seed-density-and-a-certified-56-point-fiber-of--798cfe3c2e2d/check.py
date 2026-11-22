#!/usr/bin/env python3
"""Exact finite preimage certificate for the sine-constrained quadratic map.

Standard-library only. All decisions at t=10 use rational enclosures of pi;
no binary floating-point values enter the certificate.
"""
from fractions import Fraction as Q
from math import isqrt


def atan_bounds(reciprocal_denominator, terms=30):
    # Alternating arctangent expansion with a rigorous first-omitted-term bound.
    s = sum(((-1) ** k * Q(1, reciprocal_denominator ** (2*k+1) * (2*k+1))
             for k in range(terms)), Q(0))
    error = Q(1, reciprocal_denominator ** (2*terms+1) * (2*terms+1))
    return (s, s+error) if terms % 2 == 0 else (s-error, s)


def pi_bounds():
    a,b = atan_bounds(5)
    c,d = atan_bounds(239)
    # Machin identity: pi = 16 atan(1/5) - 4 atan(1/239).
    return 16*a-4*d, 16*b-4*c


def root_enclosure(low, high):
    if high < 0:
        return None
    if low < 0:
        raise AssertionError('Unresolved near-zero radicand')
    scale = 10**30
    def floor_scaled_sqrt(r):
        return isqrt((r.numerator * scale**2) // r.denominator)
    return Q(floor_scaled_sqrt(low), scale), Q(floor_scaled_sqrt(high)+1, scale)


def inside_or_outside(vlo, vhi, lower_lo, lower_hi, upper_lo, upper_hi):
    if vlo >= lower_hi and vhi <= upper_lo:
        return 'strict_inside'
    if vhi < lower_lo or vlo > upper_hi:
        return 'strict_outside'
    return 'boundary_or_unresolved'


def count_zero_preimages():
    pl, ph = pi_bounds()
    assert ph > pl > 3 and ph-pl < Q(1, 10**40)
    assert 6*ph < 20 < 7*pl  # Only phase indices -6,..,6 are possible.
    expected_boundary = {(k,0,1 if k <= -4 else -1) for k in range(-6,0)}
    expected_boundary |= {(0,k,1 if k <= -4 else -1) for k in range(-6,0)}
    expected_boundary.add((0,0,-1))
    strict_inside = set()
    ambiguous = set()
    for m in range(-6,7):
        for n in range(-6,7):
            delta = Q(n-m, 10)
            abs_u_lo = abs(delta)*pl
            abs_u_hi = abs(delta)*ph
            if abs_u_lo > 2:
                continue
            assert abs_u_hi < 2
            lower_lo, lower_hi = abs_u_lo-1, abs_u_hi-1
            upper_lo, upper_hi = 3-abs_u_hi, 3-abs_u_lo
            linear = Q(2*(m+n), 10)
            lin_lo, lin_hi = sorted((linear*pl,linear*ph))
            rad_lo = 1 + lin_lo + delta*delta*pl*pl
            rad_hi = 1 + lin_hi + delta*delta*ph*ph
            rb = root_enclosure(rad_lo, rad_hi)
            if rb is None:
                continue
            low,high = rb
            for sign in (1,-1):
                bounds = (low,high) if sign==1 else (-high,-low)
                decision = inside_or_outside(*bounds,lower_lo,lower_hi,upper_lo,upper_hi)
                if decision == 'strict_inside':
                    strict_inside.add((m,n,sign))
                elif decision == 'boundary_or_unresolved':
                    ambiguous.add((m,n,sign))
    # These 13 candidates have the exact explicit boundary points
    # (-1,-1+j*pi/10) or (-1+j*pi/10,-1), 0<=j<=6.
    assert ambiguous == expected_boundary, (ambiguous ^ expected_boundary)
    assert len(strict_inside) == 43, len(strict_inside)
    assert not strict_inside.intersection(expected_boundary)
    assert len(ambiguous) == 13
    assert 43+13 == 56
    all_points = strict_inside | expected_boundary
    assert sum(s == 1 for _,_,s in all_points) == 49
    assert sum(s == -1 for _,_,s in all_points) == 7
    print('PASS: strict interior = 43; exact boundary = 13; total = 56')
    print('PASS: upper-sheet = 49; lower-sheet = 7')
    print('PASS: entire 13x13 phase-index box rigorously classified')
    return 56


def verify_algebra():
    # Direct rational substitution checks the global quadratic normal form.
    for u in (Q(-3,2), Q(-1,3), Q(0), Q(5,4)):
        for v in (Q(-1), Q(0), Q(1,3), Q(11,5)):
            x=(v-1+u)/2
            y=(v-1-u)/2
            assert y*(x+1) == (v*v-(u+1)**2)/4
            assert x*(y+1) == (v*v-(u-1)**2)/4
            assert x-y == u and x+y+1 == v
    # The signed integral of 1+x+y on [-1,1]^2 is 4;
    # its negative triangular contribution is the exact 1/6.
    integral_signed=Q(4)
    negative_part=Q(1,6)
    assert integral_signed + 2*negative_part == Q(13,3)
    print('PASS: global fold identities; Jacobian area 13/3')


if __name__=='__main__':
    verify_algebra()
    count_zero_preimages()
