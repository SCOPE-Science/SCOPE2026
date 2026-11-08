#!/usr/bin/env python3
"""Independent exact-rational order-simplex replay for a standard-example order polytope.
Run: python3 checker.py. Python standard library only.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def expected(n):
    nn=F(n); N=nn
    mu=F((n+2)*(n*n+1), 2*n*(n+1)*(2*n+1))
    var=F(n**6+6*n**5+10*n**4+18*n**3+13*n**2-12,12*n*n*(n+1)**2*(2*n+1)**2)
    within=F((n-2)*(n**4+4*n**3+9*n*n+6*n+4),8*n*n*(n+1)**2*(2*n+1)**2)
    matched=F((n-2)*(n-1)*(n+2)*(n*n+2*n+2),8*n*n*(n+1)**2*(2*n+1)**2)
    unmatched=F(n**5+3*n**4+5*n**3+14*n*n+8*n+8,8*n*n*(n+1)**2*(2*n+1)**2)
    spec=(F(1,12),F(n**4+3*n**3+4*n*n-9*n+37,12*(n+1)**2*(2*n+1)**2),
          F(n**3+4*n*n+2*n+2,24*(n+1)**2*(2*n+1)),
          F(n**4+4*n**3+8*n*n+26*n+48,24*n*(n+1)**2*(2*n+1)))
    volume=F(factorial(n-1)*factorial(n+1),factorial(2*n))
    return volume,mu,var,within,matched,unmatched,spec


def enumerate_order_simplices(n):
    size=2*n
    sums={k:F(0) for k in ['mean','square','samelevel','matched','unmatched','bmean','bsquare']}
    num=0
    for order in permutations(range(size)):
        pos=[0]*size
        for k,index in enumerate(order,1):pos[index]=k
        if any(pos[i]>pos[n+j] for i in range(n) for j in range(n) if i!=j):
            continue
        num+=1
        def moment(i,j):
            a,b=sorted((pos[i],pos[j]))
            return F(a*(b+1),(size+1)*(size+2))
        sums['mean']+=F(pos[0],size+1)
        sums['bmean']+=F(pos[n],size+1)
        sums['square']+=moment(0,0)
        sums['bsquare']+=moment(n,n)
        sums['samelevel']+=moment(0,1)
        sums['matched']+=moment(0,n)
        sums['unmatched']+=moment(0,n+1)
    assert num>0
    o={k:v/num for k,v in sums.items()}
    o['volume']=F(num,factorial(size))
    return num,o


def check():
    cells=0
    for n in range(2,5):
        volume,mu,var,within,matched,unmatched,spectrum=expected(n)
        num,m=enumerate_order_simplices(n)
        cells+=num
        assert m['volume']==volume,(n,'volume',m['volume'],volume)
        assert m['mean']==mu and m['bmean']==1-mu
        assert m['square']-mu**2==var and m['bsquare']-(1-mu)**2==var
        assert m['samelevel']-mu**2==within
        assert m['matched']-mu*(1-mu)==matched
        assert m['unmatched']-mu*(1-mu)==unmatched
        diag,off,crossdiag,crossoff=var,within,matched,unmatched
        from_cov=(diag+(n-1)*off+crossdiag+(n-1)*crossoff,
             diag+(n-1)*off-crossdiag-(n-1)*crossoff,
             diag-off+crossdiag-crossoff,
             diag-off-crossdiag+crossoff)
        assert from_cov==spectrum,(n,from_cov,spectrum)
        assert all(x>0 for x in spectrum)
        assert crossoff>crossdiag
        if n==2:assert off==crossdiag==0
        else:assert off>0 and crossdiag>0
        print('n',n,'linear_extensions',num,'volume',volume,'mu',mu,'four_eigenvalues',spectrum)
    print('STANDARD_EXAMPLE_EXACT_CHECKS_PASSED',cells,3)

if __name__=='__main__':check()
