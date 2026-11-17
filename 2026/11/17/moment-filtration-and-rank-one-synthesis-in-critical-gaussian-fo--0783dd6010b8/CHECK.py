#!/usr/bin/env python3
"""Exact integer checks of the finite-difference formulas on Gaussian Fock monomials.

The checks are finite corroboration; the general result follows from the algebraic proof.
"""
from math import comb, factorial, prod


def numer(m, j, k):
    """Coefficient numerator of A_{m,j} e_k in normalized monomial basis."""
    if k < j:
        return 0
    return prod(k - j + t for t in range(1, m + 1))


def finite_difference_numer(m, h, q, k):
    return sum((-1)**r * comb(q, r) * numer(m, h + r, k)
               for r in range(q + 1))


def expected_numer(m, h, q, k):
    if k < h:
        return 0
    if q == m + 1:
        return factorial(m) if k == h else 0
    return factorial(m) // factorial(m - q) * prod(
        k - h + t for t in range(1, m - q + 1))


def moments(cs, p):
    return sum(c * j**p for j, c in enumerate(cs))


def poly_numer(m, cs, k):
    return sum(c * prod(k-j+t for t in range(1, m + 1))
               for j, c in enumerate(cs))


def main():
    checks = 0
    for m in range(1, 10):
        for h in range(0, 8):
            for q in range(0, m + 2):
                for k in range(0, 45):
                    assert finite_difference_numer(m, h, q, k) == expected_numer(m, h, q, k), (m,h,q,k)
                    checks += 1
    # The moment filtration is checked through its exact integer high-degree
    # polynomial coefficients, with no floating-point tolerance.
    class_checks=0
    for m in range(1, 9):
        for h in range(0, 6):
            for q in range(0, m + 2):
                cs=[0]*h+[(-1)**r*comb(q,r) for r in range(q+1)]
                for j in range(min(q,m+1)):
                    assert moments(cs,j)==0
                if q<=m:
                    assert abs(moments(cs,q))==factorial(q)
                    L=(-1)**q*comb(m,q)*moments(cs,q)
                    assert L==factorial(m)//factorial(m-q)
                else:
                    assert all(moments(cs,j)==0 for j in range(m+1))
                    assert all(poly_numer(m,cs,k)==0 for k in range(20,25))
                class_checks+=1
    # Exact synthesis: C(z)=(1-z)^(m+1)B(z) gives a finite-rank
    # operator supported precisely on the nonzero coefficients of B.
    synthesis_checks = 0
    for m in range(1, 8):
        for size in range(1, 9):
            bs = [((3*h*h+7*m+h*size)%11)-5 for h in range(size)]
            cs = [0]*(size+m+1)
            for h, b in enumerate(bs):
                for r in range(m+2):
                    cs[h+r] += b * (-1)**r * comb(m+1,r)
            assert all(moments(cs,r)==0 for r in range(m+1))
            for k in range(size+m+8):
                from_terms = sum(c*numer(m,j,k) for j,c in enumerate(cs))
                from_rank_one = factorial(m)*bs[k] if k<size else 0
                assert from_terms == from_rank_one, (m,size,k)
                synthesis_checks+=1
    print(f'PASS exact finite-difference weight numerators: {checks}')
    print(f'PASS moment/degree/finite-rank classification probes: {class_checks}')
    print(f'PASS polynomial quotient finite-rank synthesis probes: {synthesis_checks}')
    print('PASS all stated test families; infinite-dimensional results require the proof')

if __name__=='__main__':
    main()
