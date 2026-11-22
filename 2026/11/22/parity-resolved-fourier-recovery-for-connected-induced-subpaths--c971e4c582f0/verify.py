#!/usr/bin/env python3
"""Exact integer reproducibility checks for parity-filtered induced-subpath Fourier spectra."""
from math import comb, isqrt

def rank_nullity_by_formula(n, parity):
    N=n+1
    a=(N+1)//2
    b=N//2
    null=0
    for j in range(a):
        X=a-2*j
        for k in range(b+1):
            Y=b-2*k
            eig=(X*X+Y*Y-N)//2 if parity=='even' else X*Y
            if eig==0: null+=comb(a-1,j)*comb(b,k)
    return (1<<n)-null,null

def sum_two_squares(N):
    for x in range(isqrt(N)+1):
        y2=N-x*x
        y=isqrt(y2)
        if y*y==y2:return True
    return False

def brute(n, parity):
    masks=[]
    for left in range(n):
        for right in range(left,n):
            if ((right-left+1)%2==0)==(parity=='even'):
                masks.append(((1<<(right-left+1))-1)<<left)
    nz=0
    for u in range(1<<n):
        brute_sum=sum(-1 if (u & I).bit_count()%2 else 1 for I in masks)
        eps=[1]
        val=0
        for i in range(n):
            val^=(u>>i)&1
            eps.append(-1 if val else 1)
        X=sum(eps[::2]);Y=sum(eps[1::2]);N=n+1
        formula=(X*X+Y*Y-N)//2 if parity=='even' else X*Y
        assert brute_sum==formula,(n,parity,u,brute_sum,formula)
        nz+=bool(brute_sum)
    return nz,(1<<n)-nz

def run():
    for n in range(2,14):
        for p in ('even','odd'):
            a=rank_nullity_by_formula(n,p)
            b=brute(n,p)
            assert a==b,(n,p,a,b)
            if p=='even':
                assert (a[1]>0)==sum_two_squares(n+1),(n,p,a)
            else:
                assert (a[1]==0)==(n%4==1),(n,p,a)
        print(f'n={n:2d} even rank/null={rank_nullity_by_formula(n,"even")}; odd rank/null={rank_nullity_by_formula(n,"odd")}')
    for n in range(14,1000):
        e=rank_nullity_by_formula(n,'even')
        o=rank_nullity_by_formula(n,'odd')
        assert (e[1]>0)==sum_two_squares(n+1),(n,'even')
        assert (o[1]==0)==(n%4==1),(n,'odd')
    print('PASS: independent direct signed-subpath enumeration equals two signed-prefix formulas for all 16380 characters per parity through n=13; arithmetic singularity equivalences checked n=2..999')
if __name__=='__main__':run()
