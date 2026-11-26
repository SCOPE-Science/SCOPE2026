"""Exact rational tests for the harmonic sampling rank theorem on cube vertices.

This program is a finite arithmetic consistency check, not a proof for
unbounded dimensions or degrees. The accompanying manuscript supplies that proof.
"""
from fractions import Fraction as Q
from math import factorial, comb


def gegenbauer_values(d, ell_max):
    nu = Q(d - 2, 2)
    out = []
    for negative in range(d + 1):
        x = Q(d - 2 * negative, d)
        seq = [Q(1), 2 * nu * x]
        for ell in range(1, ell_max):
            seq.append((2 * (ell + nu) * x * seq[-1]
                        - (ell + 2 * nu - 1) * seq[-2]) / (ell + 1))
        out.append(seq[:ell_max + 1])
    return out


def eigenvalue_unnormalized(d, ell, s, vals):
    return sum(Q((-1)**a * comb(s, a) * comb(d-s, b))
               * vals[a+b][ell]
               for a in range(s+1) for b in range(d-s+1))


def expected_active(d, ell, s):
    if s > ell or (ell - s) % 2:
        return False
    if (ell, s) in ((2, 0), (d+2, d)):
        return False
    return True


def null_cone_derivative(k, all_sinh):
    # Evaluate the derivative of [t^(2k)] of
    # F(t;1,-1-v,v,0,...); F is the product of three cosh or
    # of three sinh(t sqrt(z))/(t sqrt(z)) factors.
    fact_offset = 1 if all_sinh else 0
    v = Q(0)
    for a in range(k+1):
        b = k-a
        if b >= 1:
            v += Q(-b * (-1)**(b-1), factorial(2*a+fact_offset)
                  * factorial(2*b+fact_offset))
        if b >= 1:
            bb = b-1
            v += Q((-1)**bb, factorial(2*a+fact_offset)
                  * factorial(2*bb+fact_offset) * factorial(2+fact_offset))
    return v


def closed_derivative(k, all_sinh):
    assert k % 2 == 1
    sign = (-1)**((k-1)//2)
    if all_sinh:
        return Q(sign * 2**k * (k-1), 3 * (2*k+1) * factorial(2*k))
    if k == 1:
        return Q(0)
    return Q(sign * 2**(k-2) * (2*k-2), factorial(2*k-1))


def run():
    count = 0
    for d in range(3, 13):
        end = d+12
        vals = gegenbauer_values(d, end)
        for ell in range(end+1):
            rank = 0
            for s in range(d+1):
                lam = eigenvalue_unnormalized(d, ell, s, vals)
                assert lam >= 0, (d, ell, s, lam)
                assert (lam > 0) == expected_active(d, ell, s), (d, ell, s)
                if lam > 0:
                    rank += comb(d, s)
                count += 1
            if ell >= d+3:
                assert rank == 2**(d-1)
            if ell == d+2:
                assert rank == 2**(d-1)-1
        print(f'dimension={d:2d}; resonant degrees=2,{d+2}; eventual full parity rank from degree {d+3}')
    for k in (1,3,5,7,9,11):
        for all_sinh in (False, True):
            got = null_cone_derivative(k, all_sinh)
            want = closed_derivative(k, all_sinh)
            assert got == want, (k, all_sinh, got, want)
    print(f'PASS exact Gegenbauer/Walsh sign and rank checks: {count} eigenvalues')
    print('PASS exact null-cone perturbation formulas at odd indices through 11')


if __name__ == '__main__':
    run()
