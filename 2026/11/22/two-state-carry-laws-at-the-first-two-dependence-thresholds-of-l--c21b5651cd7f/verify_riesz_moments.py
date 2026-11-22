#!/usr/bin/env python3
"""Exact finite tests for carry-transfer moment formulae of lacunary Riesz products.

The infinite-in-n and all-order assertions rely on the digit-carry proof, not on these tests.
"""
from fractions import Fraction
from math import comb
from random import Random


def fourier_power(p, amplitude):
    """Coefficients indexed by the nonnegative absolute Fourier frequency."""
    coeffs = {0: Fraction(1)}
    for _ in range(p):
        new = {}
        for freq, val in coeffs.items():
            for shift, weight in ((0, Fraction(1)), (1, amplitude / 2), (-1, amplitude / 2)):
                at = freq + shift
                new[at] = new.get(at, Fraction(0)) + val * weight
        coeffs = new
    return {j: coeffs.get(j, Fraction(0)) for j in range(p + 1)}


def matrices(p, q, amplitudes):
    out = []
    for amplitude in amplitudes:
        a = fourier_power(p, amplitude)
        get = lambda j: a.get(j, Fraction(0))
        out.append(((get(0), 2*get(q)), (get(1), get(q-1)+get(q+1))))
    return out


def predicted(p, q, amplitudes):
    v0, v1 = Fraction(1), Fraction(0)
    for T in matrices(p, q, amplitudes):
        v0, v1 = v0*T[0][0]+v1*T[1][0], v0*T[0][1]+v1*T[1][1]
    return v0


def brute(p, q, amplitudes):
    coeff = {0: Fraction(1)}
    for j, amplitude in enumerate(amplitudes):
        a = fourier_power(p, amplitude)
        next_coeff = {}
        for k, val in coeff.items():
            for d in range(-p, p+1):
                loc = k + d*(q**j)
                next_coeff[loc] = next_coeff.get(loc, Fraction(0)) + val*a[abs(d)]
        coeff = next_coeff
    return coeff.get(0, Fraction(0))


def verify():
    count = 0
    rng = Random(20261117)
    for p in range(4, 9):
        for q in (p-1, p, p+1, p+2):
            for n in range(0, 4):
                amplitudes = [Fraction(1), Fraction(2,3), Fraction(3,5)][:n]
                got, expect = predicted(p,q,amplitudes), brute(p,q,amplitudes)
                assert got == expect, (p,q,n,got,expect)
                count += 1
            for _ in range(4):
                amplitudes = [Fraction(rng.randint(1,9), 10) for _ in range(3)]
                assert predicted(p,q,amplitudes) == brute(p,q,amplitudes)
                count += 1
    for p in range(4, 11):
        for k in range(2,6):
            amps = [Fraction(rng.randint(1,9),10) for _ in range(k)]
            m_lo=predicted(p,p-1,amps)
            m_hi=predicted(p,p,amps)
            m_ind=predicted(p,p+1,amps)
            assert m_lo > m_hi > m_ind
            assert m_ind == __import__('functools').reduce(lambda x,y:x*y,
                            (fourier_power(p,a)[0] for a in amps), Fraction(1))
            count += 2
    for q, expected in ((3, Fraction(1449,64)),(4,Fraction(1253,64)),(5,Fraction(1225,64))):
        assert brute(4,q,[Fraction(1),Fraction(1)]) == expected
        count += 1
    assert fourier_power(4,Fraction(1)) == {0:Fraction(35,8),1:Fraction(7,2),
                  2:Fraction(7,4),3:Fraction(1,2),4:Fraction(1,16)}
    count += 1
    print(f"PASS: {count} independent exact assertions")

if __name__ == '__main__': verify()
