#!/usr/bin/env python3
"""Independent finite checks of weighted outer-independent Roman domination in rook graphs."""
from itertools import product, combinations
from math import comb, factorial
from collections import Counter
from random import Random

def polynomial_formula(m,n):
    N=m*n
    p=Counter()
    for k in range(min(m,n)+1):
        rooks=comb(m,k)*comb(n,k)*factorial(k)
        for t in range(k+1):
            a=t*(m+n-t-1)
            assert 0<=a<=N-k
            mult=rooks*(-1)**t*comb(k,t)
            for q in range(N-k-a+1):
                p[N-k+q]+=mult*comb(N-k-a,q)
    return {i:c for i,c in p.items() if c}

def min_coefficient(m,n):
    s=min(m,n)
    h=s//2
    R=lambda k:comb(m,k)*comb(n,k)*factorial(k)
    if s%2==0:
        return m*n-h,R(s)*factorial(s)//factorial(h)
    else:
        return m*n-h, (R(s-1)*factorial(s-1)+R(s)*factorial(s)*(m+n-s-1))//factorial(h)

def inspect_labeling(m,n,lab,total=False):
    # Definition checked literally: independent zeros and every zero adjacent to a 2.
    zero=[(i//n,i%n) for i,x in enumerate(lab) if x==0]
    if len(set(r for r,c in zero))!=len(zero) or len(set(c for r,c in zero))!=len(zero):
        return False
    for r,c in zero:
        if not any(lab[i*n+j]==2 for i in range(m) for j in range(n) if (i==r or j==c) and (i,j)!=(r,c)):
            return False
    if total:
        for i,x in enumerate(lab):
            if x and not any(lab[j] for j in range(m*n) if j!=i and (i//n==j//n or i%n==j%n)):
                return False
    return True

def exhaustive(m,n):
    from time import monotonic
    p=Counter(); pt=Counter(); tested=0
    for lab in product((0,1,2),repeat=m*n):
        tested+=1
        if inspect_labeling(m,n,lab):p[sum(lab)]+=1
        if inspect_labeling(m,n,lab,True):pt[sum(lab)]+=1
    p={k:v for k,v in p.items() if v}
    pred=polynomial_formula(m,n)
    assert p==pred,(m,n,p,pred)
    weight,count=min_coefficient(m,n)
    assert min(p)==weight and p[weight]==count,(m,n,weight,count,p)
    if (m,n)!=(2,2):assert pt==p,(m,n,pt,p)
    else:
        assert dict(pt)!={**p}
        diff={k:p.get(k,0)-pt.get(k,0) for k in set(p)|set(pt)}
        assert {k:v for k,v in diff.items() if v}=={3:4,4:2},diff
    print('DIRECT_OK',m,n,'assignments',tested,'valid',sum(p.values()),'min',(weight,count),'total_equiv',pt==p)
    return tested

def sampler(m,n,tries,seed):
    rng=Random(seed)
    # Exact polynomial gives a full baseline; this tests independently labelled functions.
    assert min_coefficient(m,n)[0]==min(polynomial_formula(m,n))
    good=0
    for _ in range(tries):
        f=[rng.randrange(3) for _ in range(m*n)]
        g=inspect_labeling(m,n,f)
        if g:good+=1
        if min(m,n)>=3: assert inspect_labeling(m,n,f,True)==g
    print('SAMPLE_OK',m,n,tries,'valid',good)

if __name__=='__main__':
    tot=0
    for m,n in ((2,2),(2,3),(2,4),(3,3),(3,4)):
        tot+=exhaustive(m,n)
    for m in range(2,10):
        for n in range(m,11):
            p=polynomial_formula(m,n)
            assert all(v>0 for v in p.values())
            assert min_coefficient(m,n)==(min(p),p[min(p)])
    sampler(4,4,30000,18027)
    sampler(4,5,30000,18029)
    print('VERIFY_OK','direct_profiles',5,'direct_labelings',tot,'symbolic_profiles',sum(11-m for m in range(2,10)),'random_labelings',60000,'OIRDF_weight_polynomial=PASS','OITRDF_equivalence_and_boundary=PASS','minimum_multiplicities=PASS')
