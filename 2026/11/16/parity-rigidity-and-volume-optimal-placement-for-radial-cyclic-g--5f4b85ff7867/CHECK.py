#!/usr/bin/env python3
"""Independent finite checks of the radial cyclic two-translation Gabor formulas.
Only Python standard library is required for exact rational tests; optional numpy
checks the unitarily block-diagonalized complete synthesis matrix.
"""
from fractions import Fraction
from itertools import combinations
import math


def fiber(window, m, d, r):
    n = 2*m
    return ((window[r], window[(r-d)%n]),
            (window[r+m], window[(r+m-d)%n]))

def det(b):
    return b[0][0]*b[1][1]-b[1][0]*b[0][1]

def predicted_volume(m,d,q):
    def v(k): return q**(m-k)*(1-q**(2*k))
    return v(d)**(m-d+1)*math.prod(v(k)**2 for k in range(1,d,2))


def run():
    tests = 0
    for m in range(2,13):
        n=2*m
        for q in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
            w=[q**min(j,n-j) for j in range(n)]
            for d in range(1,m+1):
                ds=[det(fiber(w,m,d,r)) for r in range(m)]
                zeros=sum(x==0 for x in ds)
                assert zeros==(1 if d%2==0 else 0),(m,d,q,ds)
                tests += 1
                if d%2:
                    volume=math.prod(abs(x) for x in ds)
                    assert volume==predicted_volume(m,d,q),(m,d,q)
                    tests += 1
                if d+2<=m and d%2:
                    actual=predicted_volume(m,d+2,q)/predicted_volume(m,d,q)
                    def v(k):return q**(m-k)*(1-q**(2*k))
                    asserted=(v(d+2)/v(d))**(m-d-1)
                    assert actual==asserted and actual>1,(m,d,q,actual,asserted)
                    tests += 1
        # Test nongeometric profiles with strict radial decrease.
        for seed in range(1,8):
            radial=[Fraction(1,1)]
            for j in range(1,m+1):
                radial.append(radial[-1]*Fraction(3*j+seed,5*j+seed+1))
            w=[radial[min(j,n-j)] for j in range(n)]
            for d in range(1,m+1):
                assert sum(det(fiber(w,m,d,r))==0 for r in range(m))==(1 if d%2==0 else 0)
                tests+=1
    # Verify full synthesis matrix and fiber eigenvalues on a small exhaustive subset.
    try:
        import numpy as np
    except ImportError:
        print('PASS',tests,'exact rational checks; optional numpy check skipped');return
    for m in range(2,10):
        n=2*m
        q=0.6
        w=np.array([q**min(j,n-j) for j in range(n)])
        for d in range(1,n):
            columns=[]
            for shift in [0,d]:
                for k in range(m):
                    columns.append(np.array([np.exp(2j*np.pi*k*j/m)*w[(j-shift)%n] for j in range(n)]))
            S=np.column_stack(columns)
            spectrum=np.linalg.eigvalsh(S@S.conj().T)
            blocks=[]
            for r in range(m):
                B=np.array(fiber(w,m,d,r),dtype=float)
                blocks.extend(np.linalg.eigvalsh(m*B@B.T))
            assert np.allclose(np.sort(spectrum),np.sort(blocks),rtol=1e-8,atol=1e-9),(m,d)
            rank=np.linalg.matrix_rank(S,tol=1e-7)
            assert rank==n-(d%2==0),(m,d,rank)
            tests+=2
    print('PASS',tests,'checks including rational rank, determinant, strict volume ratios, and numerical complete Fourier matrices')

if __name__=='__main__':run()
