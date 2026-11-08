"""Reproduce conditional Gram spectra of antipodal Hamming-layer Walsh sampling."""
from itertools import combinations, product
from fractions import Fraction
from math import comb
import numpy as np


def levels(n, s):
    t = s * s
    return (
        Fraction(t, n),
        Fraction(n*n-t, n*(n-1)),
        Fraction(1, 1) + Fraction((t-n)**2, 2*n*(n-1)),
        Fraction(t*(n*n-t), n*(n-1)*(n-2)),
        Fraction((n*n-t)*((n-2)**2-t), n*(n-1)*(n-2)*(n-3)),
    )


def radial_allowed(n):
    return [s for s in range(1, n-3) if (n-s)%2 == 0]


def numerical_matrix(n,s):
    inds=[()]+[(i,) for i in range(n)]+list(combinations(range(n),2))
    shell=[x for x in product((-1,1),repeat=n) if abs(sum(x))==s]
    mat=np.asarray([[np.prod([x[i] for i in idx]) for idx in inds]
                    for x in shell],dtype=float)
    return mat.T@mat/len(shell)


def main():
    asserts=0
    for n in range(5,12):
        for s in radial_allowed(n):
            lam=levels(n,s)
            assert all(t>0 for t in lam); asserts+=1
            mat=numerical_matrix(n,s)
            e=np.linalg.eigvalsh(mat)
            goal=sorted([0.] + sum(([float(v)]*mult for v,mult in zip(lam,
                (1,n-1,1,n-1,n*(n-3)//2))), []))
            assert len(e)==len(goal); asserts+=1
            assert np.max(np.abs(e-np.asarray(goal))) < 2e-11; asserts+=1
            assert np.linalg.matrix_rank(mat,tol=1e-9)==len(goal)-1; asserts+=1
            p=Fraction(2*comb(n,(n-s)//2),2**n)
            assert 0<p<1; asserts+=1
    for m in range(3,501):
        n=m*m
        s=m
        vals=levels(n,s)
        target=Fraction(n*(n-3),(n-1)*(n-4))
        assert max(vals)/min(vals)==target; asserts+=1
        assert target < 1 + Fraction(4,n); asserts+=1
        assert vals[0]==vals[1]==vals[2]==1; asserts+=1
        assert min(vals)==vals[4] and max(vals)==vals[3]; asserts+=1
        for sr in (m-2, m+2):
            if sr<1 or sr>n-4: continue
            lo, hi = min(levels(n,sr)), max(levels(n,sr))
            assert hi/lo>target; asserts+=1
        # Direct 3-wise
        assert Fraction(s*s-n,n*(n-1))==0; asserts+=1
    print(f'ANTIPODAL_TWO_SHELL_CHECKS_PASS {asserts}')


if __name__=='__main__':
    main()
