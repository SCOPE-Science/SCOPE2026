"""Supplementary finite tests of the explicit three-anchor harmonic-extension formula.

Run: python verification/check.py
Requires Python 3 with numpy.
The proof for all cycle lengths is analytic, not based on this finite test.
"""
from fractions import Fraction
from itertools import combinations
from math import sqrt
import numpy as np


def coefficients(g):
    return Fraction(g*(2*g+1), 6*(g+1)), Fraction(g*(g+2), 6*(g+1))


def harmonic_gram(gaps):
    n = 3 + sum(gaps)
    pos = [0, gaps[0]+1, gaps[0]+gaps[1]+2]
    h = np.zeros((n, 3))
    for j, p in enumerate(pos):
        h[p, j] = 1
    for j, g in enumerate(gaps):
        p = pos[j]
        k = (j+1) % 3
        for t in range(1, g+1):
            row = (p+t) % n
            h[row, j] = (g+1-t)/(g+1)
            h[row, k] = t/(g+1)
    return h.T @ h, h


def formula(n):
    q, r = divmod(n-3, 3)
    s, c = map(float, coefficients(q))
    if r == 0:
        return n/3
    if r == 1:
        u, v, d = 1+2*s+c+0.5, 1+2*s, c
    else:
        t, d = map(float, coefficients(q+1))
        u, v = 1+2*t, 1+s+t+c
    return (u+v+sqrt((u-v)**2+8*d*d))/2


def main():
    exact = 0
    for g in range(90):
        s, c = coefficients(g)
        m = g+1
        ss = sum((Fraction(t,m)**2 for t in range(1,g+1)), Fraction(0))
        cc = sum((Fraction(t*(m-t),m*m) for t in range(1,g+1)), Fraction(0))
        assert (s,c)==(ss,cc)
        assert s+c == Fraction(g,2)
        exact += 1
    spectra = 0
    for n in range(3,44):
        best = float('inf')
        winners = []
        for a in range(n-2):
            for b in range(n-2-a):
                g = (a,b,n-3-a-b)
                A, h = harmonic_gram(g)
                v = np.linalg.eigvalsh(A)[-1]
                assert np.max(np.abs(A-h.T@h))<1.e-12
                if v < best-1.e-9:
                    best, winners = v, [g]
                elif abs(v-best)<1.e-9:
                    winners.append(g)
                spectra += 1
        assert abs(best-formula(n))<1.e-9, (n,best,formula(n))
        q,r=divmod(n-3,3)
        assert len(winners)==(1 if r==0 else 3),(n,winners)
        assert all(max(g)-min(g)<=1 for g in winners)
    # A normalized DFT is a Parseval host analysis, checked separately.
    for n in [4,5,6,7,10,13,17]:
        gaps = [((n-3)//3)]*3
        for j in range((n-3)%3):
            gaps[j]+=1
        A,h=harmonic_gram(gaps)
        grid=np.arange(n)
        U=np.exp(-2j*np.pi*np.outer(grid,grid)/n)/sqrt(n)
        assert np.max(np.abs((U@h).conj().T@(U@h)-A))<1.e-11
    print('PASS exact_gap_sums=%d ordered_gap_spectra=%d cycle_range=3..43 dft_checks=7' %(exact,spectra))

if __name__ == '__main__':
    main()
