#!/usr/bin/env python3
"""Direct finite check of dissociation-set enumerator on rook boards.
No external packages required. Python 3.10+."""
from math import factorial
from collections import Counter
from itertools import combinations

def direct(m, n):
    # Rook graph with named squares (i,j); enumerate every subset as a bit mask.
    N=m*n
    nbr=[0]*N
    for i in range(m):
        for j in range(n):
            v=i*n+j
            nbr[v]=sum(1 << (k*n+l) for k in range(m) for l in range(n)
                       if (k==i or l==j) and (k,l)!=(i,j))
    p=Counter()
    for mask in range(1<<N):
        valid=True
        for v in range(N):
            if (mask>>v)&1 and (nbr[v]&mask).bit_count()>1:
                valid=False; break
        if valid: p[mask.bit_count()]+=1
    return p

def formula(m,n):
    p=Counter()
    for a_center in range(m+1):
        for b_center in range(n+1):
            for isolated in range(min(m,n)+1):
                left_rem=m-a_center-2*b_center-isolated
                right_rem=n-b_center-2*a_center-isolated
                if min(left_rem,right_rem)<0: continue
                count=factorial(m)*factorial(n)//(factorial(a_center)*factorial(b_center)
                         *2**(a_center+b_center)*factorial(isolated)
                         *factorial(left_rem)*factorial(right_rem))
                p[2*(a_center+b_center)+isolated]+=count
    return p

def bound(m,n):
    return min(2*m,2*n,2*(m+n)//3)

def witness(m,n):
    # Construct a maximum collection of vertex-disjoint P3 and K2
    if m>n: m,n=n,m
    target=bound(m,n)
    if n>=2*m: return (m,0,0)
    t=(m+n)//3
    a=int((m+n)%3==2)
    p=max(0,2*t+a-m)
    q=t-p
    assert 0<=p and 0<=q and m>=p+2*q+a and n>=q+2*p+a
    assert 2*(p+q)+a==target
    return p,q,a

if __name__=='__main__':
    for m,n in [(1,1),(1,2),(1,5),(2,2),(2,3),(2,5),(3,3),(3,4),
                (3,5),(4,4),(4,5)]:
        p=direct(m,n); q=formula(m,n)
        assert p==q,(m,n,p,q)
        assert max(p)==bound(m,n),(m,n,max(p),bound(m,n))
        print('BRUTE_OK',m,n,'size',sum(p.values()),'degree',max(p),'top_count',p[max(p)])
    assert max(formula(6,6))==8 and formula(6,6)[8]==8100
    print('PUMAC2010_6X6_PRIOR_COMPATIBILITY_OK max=8 count=8100')
    for m in range(1,40):
        for n in range(1,40):
            p=formula(m,n)
            assert max(p)==bound(m,n),(m,n)
            assert witness(m,n) is not None
    print('FORMULA_MAX_AND_CONSTRUCTION_OK m,n=1..39')
    print('VERIFY_OK')
