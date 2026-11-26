"""Reproduce exact finite-alphabet identities and direct Fourier checks.

Requirements: Python 3 standard library. Run: python verify_sharp_triple_stability.py
"""
import cmath
from fractions import Fraction
from itertools import product, combinations
from math import factorial, pi


def moment_by_word(p):
    q = len(p)
    total = Fraction(0)
    for seq in product(range(q), repeat=3):
        counts = {k: seq.count(k) for k in set(seq)}
        rearrangements = factorial(3)
        for c in counts.values():
            rearrangements //= factorial(c)
        total += rearrangements * p[seq[0]] * p[seq[1]] * p[seq[2]]
    return total


def verify_exact(p):
    q = len(p)
    assert sum(p) == 1
    s2 = sum(x*x for x in p)
    s3 = sum(x*x*x for x in p)
    F = 6 - 9*s2 + 4*s3
    assert F == moment_by_word(p)
    A = 6 - Fraction(9, q) + Fraction(4, q*q)
    V = s2 - Fraction(1, q)
    R = sum((p[i]-p[j])**2 * (1-p[i]-p[j])
            for i,j in combinations(range(q),2))
    assert A-F == (5-Fraction(4,q))*V + Fraction(4,q)*R
    assert R >= 0 and A-F >= 0
    if p == [Fraction(1,q)]*q or 1 in p:
        assert R == 0
    else:
        assert R > 0
    return A,F,V,R


def verify_extension(q, values):
    assert any(abs(z)>0 for z in values)
    N = sum(abs(z)**2 for z in values)/q
    p = [abs(z)**2/(q*N) for z in values]
    target = N**3 * (6-9*sum(z*z for z in p)+4*sum(z*z*z for z in p))
    direct = 0.0
    for x0,x1,x2 in product(range(q), repeat=3):
        ext = sum(values[j] * cmath.exp(2j*pi*((x0*j+x1*j*j+x2*j*j*j)%q)/q)
                  for j in range(q))/q
        direct += abs(ext)**6
    assert abs(direct-target)<4e-10*max(1,abs(target)), (q,direct,target)
    return direct


def main():
    cases=0
    for q in (5,7,11):
        candidates=[
            [Fraction(1,q)]*q,
            [Fraction(1)]+[Fraction(0)]*(q-1),
            [Fraction(1,2)]*2+[Fraction(0)]*(q-2),
            [Fraction(1,3)]*3+[Fraction(0)]*(q-3),
            [Fraction(k+1,(q*(q+1))//2) for k in range(q)],
            [Fraction(2,q+1)]+[Fraction(1,q+1)]*(q-1)
        ]
        for p in candidates:
            verify_exact(p)
            cases += 1
    for z in product(range(7),repeat=5):
        if sum(z)==6:
            verify_exact([Fraction(x,6) for x in z])
            cases += 1
    assert cases == 228
    fourier_cases=0
    for q in (5,7):
        for offset in (0,1,2,3):
            values=[complex((3*j+1+offset)%9-4, (5*j+2+offset)%7-3)
                    for j in range(q)]
            verify_extension(q,values)
            fourier_cases += 1
    assert fourier_cases == 8
    print('VERIFY_OK','exact_prob_cases=',cases,'independent_fourier_cases=',fourier_cases)


if __name__=='__main__':
    main()
