#!/usr/bin/env python3
"""Exact finite checks for reverse-complement-symmetric subsequence universality.
Independent literal subsequence matching is used alongside analytic coefficients.
"""
from itertools import product, permutations
from math import factorial, comb
from collections import Counter

def rc(w):return tuple(x^1 for x in reversed(w))
def idx_greedy(w,q):
    cnt=0; seen=set()
    for x in w:
        seen.add(x)
        if len(seen)==q: cnt+=1;seen.clear()
    return cnt

def idx_literal(w,q):
    for k in range(len(w)//q,0,-1):
        ok=True
        for p in product(range(q),repeat=k):
            t=0
            for a in w:
                if t<k and a==p[t]:t+=1
            if t<k:ok=False;break
        if ok:return k
    return 0

def surj(j,n):
    if j==0:return int(n==0)
    if n<0:return 0
    return sum((-1)**(j-i)*comb(j,i)*(i**n) for i in range(j+1))

def coeff(q,M):
    d=q//2
    A=[q*surj(q-1,l-1) if l>0 else 0 for l in range(M+1)]
    R=[sum(comb(q,j)*surj(j,l) for j in range(q)) for l in range(M+1)]
    U=[sum(comb(d,j-d)*2**(q-j)*surj(j,l) for j in range(d,q)) for l in range(M+1)]
    F=[[0]*(M+1) for _ in range(M+1)]
    B=[[0]*(M+1) for _ in range(M+1)]
    for m in range(M+1):F[0][m]=R[m];B[0][m]=U[m]
    for r in range(1,M+1):
        for m in range(M+1):
            F[r][m]=sum(A[l]*F[r-1][m-l] for l in range(m+1))
            B[r][m]=sum(A[l]*B[r-1][m-l] for l in range(m+1))
    return {m:Counter({**{2*r:F[r][m]-B[r][m] for r in range(M+1)},**{2*r+1:B[r][m] for r in range(M+1)}}) for m in range(M+1)}

def constructed(q,k):
    perms=list(permutations(range(q)))
    m=k//2
    good=set()
    for blocks in product(perms,repeat=m):
        H=tuple(x for p in blocks for x in p)
        if k%2==0:good.add(H+rc(H))
        else:
            d=q//2
            for choice in product(range(2),repeat=d):
                for order in permutations(range(d)):
                    S=tuple(2*i+choice[i] for i in order)
                    left=H+S
                    good.add(left+rc(left))
    return good

def run():
    nwords=0;literal=0;profiles=0;optimal=0
    for q,M in ((2,9),(4,7),(6,5)):
        expect=coeff(q,M)
        for h in range(M+1):
            actual=Counter()
            for H in product(range(q),repeat=h):
                W=H+rc(H)
                val=idx_greedy(W,q)
                if q==2 or (q==4 and h<=5) or (q==6 and h<=3):
                    lit=idx_literal(W,q)
                    assert lit==val,(q,h,W,val,lit)
                    literal+=1
                actual[val]+=1;nwords+=1
            assert actual==+expect[h],(q,h,actual,expect[h])
            assert sum(actual.values())==q**h
            profiles+=1
        for k in (range(1,7) if q==2 else range(1,4) if q==4 else range(1,2)):
            n=q*k
            good=set()
            for H in product(range(q),repeat=n//2):
                W=H+rc(H)
                if idx_greedy(W,q)>=k:good.add(W)
            expected=constructed(q,k)
            assert good==expected,(q,k,len(good),len(expected))
            assert len(good)==factorial(q)**(k//2)*(2**(q//2)*factorial(q//2) if k%2 else 1)
            optimal+=1
    print(f'WC_UNIVERSAL_VERIFY_OK symmetric_hosts={nwords} literal_checks={literal} bivariate_profiles={profiles} shortest_classifications={optimal}')
if __name__=='__main__':run()
