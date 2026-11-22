#!/usr/bin/env python3
"""Standalone finite checks for neighboring-base repunit gcd classification.

Uses only Python's standard library; all assertions concern finite certificates.
"""
from math import gcd, prod

P = {5: {2, 3}, 7: {3, 5}, 13: {2, 4, 5, 6, 7, 8, 10, 11}}

def mul(f, g):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] += a * b
    return out

def ev(f, n, mod=None):
    y = 0
    for a in f[::-1]:
        y = y * n + a
        if mod is not None:
            y %= mod
    return y

def factors():
    # Factorizations of R_12(X)/Phi_3(X) and R_12(X+1)/Phi_3(X),
    # coefficients in ascending order.
    A = [1]
    for f in ([1, 1], [1, 0, 1], [1, -1, 1], [1, 0, -1, 0, 1]):
        A = mul(A, f)
    B = [1]
    for f in ([2, 1], [3, 3, 1], [2, 2, 1], [1, 2, 5, 4, 1]):
        B = mul(B, f)
    return A, B

def bareiss_det(a):
    a = [row[:] for row in a]
    n = len(a)
    denominator = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k+1, n) if a[j][k] != 0), None)
            assert j is not None
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % denominator == 0
                a[i][j] = num // denominator
            a[i][k] = 0
        denominator = pivot
    return sign * a[-1][-1]

def resultant(f, g):
    # f,g descending, Sylvester matrix
    m, n = len(f)-1, len(g)-1
    S = []
    for i in range(n):
        S.append([0]*i + f + [0]*(n-1-i))
    for i in range(m):
        S.append([0]*i + g + [0]*(m-1-i))
    return bareiss_det(S)

def test():
    # Verify the exact polynomial Bezout certificate for the six-digit case.
    A6 = [1,0,0,1]
    B6 = mul([2,1],[3,3,1])
    left=mul([-16,-15,-4],A6)
    right=mul([5,-5,4],B6)
    assert [left[i]+right[i] for i in range(len(left))] == [14]+[0]*(len(left)-1)
    assert {r for r in range(7) if ev(A6,r,7)==ev(B6,r,7)==0} == {3,5}
    A, B = factors()
    for b in range(0, 25):
        D = b*b+b+1
        assert ev(A,b)*D == sum(b**j for j in range(12))
        assert ev(B,b)*D == sum((b+1)**j for j in range(12))
    res = abs(resultant(A[::-1],B[::-1]))
    assert res == 2**10 * 5**2 * 7**2 * 13**8, res
    assert res == 1023252616422400
    assert not [r for r in range(2) if ev(A,r,2)==ev(B,r,2)==0]
    for p, roots in P.items():
        assert {r for r in range(p) if ev(A,r,p)==ev(B,r,p)==0} == roots
        assert not [r for r in range(p*p) if ev(A,r,p*p)==ev(B,r,p*p)==0]
    residues = []
    count = {d: 0 for d in (1,5,7,13,35,65,91,455)}
    for b in range(455):
        expected=prod(p for p,roots in P.items() if b%p in roots)
        assert gcd(ev(A,b),ev(B,b)) == expected
        count[expected]+=1
    assert count == {1:75, 5:50, 7:30, 13:120, 35:20, 65:80, 91:48, 455:32}, count
    # Integer-value checks beyond one residue period, and adjacent length-six law.
    for b in range(2, 4002):
        six_a=sum(b**j for j in range(6))
        six_b=sum((b+1)**j for j in range(6))
        expect6=(b*b+b+1) * (7 if b%7 in {3,5} else 1)
        assert gcd(six_a,six_b)==expect6
        twelve_a=sum(b**j for j in range(12))
        twelve_b=sum((b+1)**j for j in range(12))
        expect12=(b*b+b+1)*prod(p for p,roots in P.items() if b%p in roots)
        assert gcd(twelve_a,twelve_b)==expect12
    print('PASS resultant, all prime-power obstruction residues, all 455 periodic classes, frequencies, 8000 integer GCD tests')
    print('RESULTANT',res,'COUNT',count)

if __name__ == '__main__':test()
