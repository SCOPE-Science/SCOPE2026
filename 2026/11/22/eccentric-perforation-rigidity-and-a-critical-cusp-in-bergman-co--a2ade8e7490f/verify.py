"""Finite-dimensional checks for a circularly perforated Bergman observation mask.

These checks provide numerical diagnostics, not a proof of operator statements.
Requires NumPy. To run: python verify.py
"""
import math
import numpy as np


def compression(radius_outer, radius_inner, shift, size):
    b = radius_outer**2
    a = radius_inner**2
    out = np.zeros((size, size), complex)
    for n in range(size):
        for ell in range(size):
            moment = sum(
                math.comb(n, k) * math.comb(ell, k)
                * a**(k + 1) / (k + 1)
                * shift**(n - k) * shift.conjugate()**(ell - k)
                for k in range(min(n, ell) + 1)
            )
            out[n, ell] = (b**(n + 1) if n == ell else 0) - math.sqrt((n + 1)*(ell + 1))*moment
    return out


def top(M):
    return float(np.linalg.eigvalsh(M)[-1])


def main():
    tests = 0
    for r, R in [(0.3, 0.7), (0.4, math.sqrt(.84)), (0.6, 0.7)]:
        a, b = r*r, R*R
        m = b-a
        for n in [8, 12, 20]:
            M = compression(R, r, 0j, n)
            diag = [b**(k+1)-a**(k+1) for k in range(n)]
            assert np.allclose(M, np.diag(diag), atol=1e-12)
            tests += 1
            assert abs(top(M) - max(diag)) < 1e-11
            tests += 1
        for t in [0.005,0.02,0.04]:
            if t+r>=R:
                continue
            M = compression(R,r,t+0j,22)
            lb2 = top(M[:2,:2])
            d=b*b-a*a-2*a*t*t
            exact = (m+d + math.sqrt((m-d)**2+8*a*a*t*t))/2
            assert abs(lb2-exact)<1e-12
            tests += 1
            assert top(M)>=lb2-1e-12 and top(M)>m
            tests += 1
    r,R=.3,.7
    a,b=r*r,R*R;m=b-a
    coef=2*a*a/(m*(1-a-b))
    for t in [.004,.008,.016]:
        result=(top(compression(R,r,t+0j,32))-m)/t**2
        assert abs(result/coef-1)<.01
        tests+=1
    r,R=.4,math.sqrt(.84)
    a,b=r*r,R*R;m=b-a
    slope=math.sqrt(2)*a
    for t in [.0008,.0016,.0032]:
        result=(top(compression(R,r,t+0j,32))-m)/t
        assert abs(result/slope-1)<.015
        tests+=1
    assert abs((.3**4*2)/((.7**2-.3**2)*(1-.3**2-.7**2)) - 0.0964285714285714)<1e-12
    tests+=1
    print('PASS:',tests,'independent finite-matrix diagnostics')


if __name__ == '__main__':
    main()
