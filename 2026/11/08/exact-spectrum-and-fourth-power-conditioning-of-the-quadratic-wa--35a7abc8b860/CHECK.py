"""Finite checks for low-weight principal Walsh submatrix spectrum.
Only the algebraic proof establishes all dimensions.
"""
from itertools import combinations
from math import comb, sqrt
import numpy as np

def check(n):
    sets=[tuple()] + [(i,) for i in range(n)] + list(combinations(range(n),2))
    m=len(sets)
    W=np.empty((m,m),dtype=np.float64)
    for i,a in enumerate(sets):
        for j,b in enumerate(sets):
            W[i,j] = (-1)**len(set(a).intersection(b))
    C=comb(n,2)
    R=np.array([[1,sqrt(n),sqrt(C)],
                [sqrt(n),n-2,(n-4)*sqrt((n-1)/2)],
                [sqrt(C),(n-4)*sqrt((n-1)/2),C-4*(n-2)]])
    S=np.array([[-2,-2*sqrt(n-2)],[-2*sqrt(n-2),-2*(n-4)]])
    pred=np.sort(np.concatenate([np.linalg.eigvalsh(R),
                 np.tile(np.linalg.eigvalsh(S),n-1),
                 np.full(n*(n-3)//2,4.0)]))
    actual=np.linalg.eigvalsh(W)
    assert np.max(np.abs(actual-pred)) <1e-7,(n,actual,pred)
    assert sum(actual>1e-8)==1+C
    assert sum(actual< -1e-8)==n
    assert np.linalg.slogdet(W)[0] == (-1)**n
    assert abs(np.linalg.slogdet(W)[1]- n*n*np.log(2)) < 1e-7
    print(f'n={n} order={m} exact spectral sectors agree; positive={1+C}, negative={n}')

if __name__=='__main__':
    for n in range(4,14):
        check(n)
    print('HAMMING_TWO_BALL_WALSH_SPECTRUM_PASS')
