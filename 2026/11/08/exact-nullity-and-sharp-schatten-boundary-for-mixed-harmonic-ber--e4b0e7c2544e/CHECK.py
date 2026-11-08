#!/usr/bin/env python3
"""Finite diagnostics for mixed harmonic Bergman monomial commutators.

Only standard-library dependencies. Finite numerical checks are NOT infinite proofs.
"""
from math import lgamma, exp, sqrt, isclose

def a(k, alpha):
    return exp(lgamma(alpha + 2) + lgamma(k + 1) - lgamma(k + alpha + 2))

def w(j, k, alpha):
    if j >= 0:
        return sqrt(a(j + k, alpha) / a(j, alpha))
    if j <= -k:
        return sqrt(a(-j, alpha) / a(-j - k, alpha))
    return a(k, alpha) / sqrt(a(-j, alpha) * a(j + k, alpha))

def c(j, m, n, alpha):
    return w(j,n,alpha)*w(j+n-m,m,alpha)-w(j-m,m,alpha)*w(j-m,n,alpha)

def main():
    tested=0
    for alpha in (-0.9, -0.2, 0.0, 0.6, 3.7):
        for m in range(1,8):
            for n in range(1,8):
                if m==n:
                    continue
                for j in range(-max(m,n)-8, max(m,n)+9):
                    x=c(j,m,n,alpha)
                    left=min(0,m-n)
                    right=max(0,m-n)
                    expected=-1 if j<left else (1 if j>right else 0)
                    actual=-1 if x < -1e-9 else (1 if x > 1e-9 else 0)
                    assert actual==expected, (alpha,m,n,j,x,expected)
                    tested+=1
                    assert isclose(x, -c(m-n-j,m,n,alpha),rel_tol=1e-7, abs_tol=1e-9)
                    tested+=1
    for alpha in (-0.8,0.0,1.5):
        for m,n in ((1,2),(2,7),(7,3),(4,5)):
            target=(alpha+1)*m*n
            j=500
            ratio=j*j*c(j,m,n,alpha)/target
            assert abs(ratio-1)<0.08,(alpha,m,n,ratio)
            tested+=1
    print('PASS:',tested,'finite diagnostic assertions (not an infinite proof)')

if __name__=='__main__':
    main()
