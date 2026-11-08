#!/usr/bin/env python3
"""Exact finite-arithmetic checks for covariance of edges and isolates in balanced cluster graphs."""
from fractions import Fraction
from itertools import combinations, product
from math import comb

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def formula(r, m, k):
    if k == 0: return Fraction(0)
    n = r*m
    q = Fraction(k*choose((r-1)*m, k-1), choose(n-1,k-1))
    return q * Fraction((m-1)*(k-1)*(m*(k-2*r)+2), 2*((r-1)*m-1)*(n-1))

def occupancy_cov(r, m, k):
    """Independent weighted enumeration of occupancy profiles, not use conditioned-mark proof."""
    weights=[]
    for x in product(range(m+1),repeat=r):
        if sum(x) != k: continue
        w=1
        for c in x: w*=comb(m,c)
        e=sum(c*(c-1)//2 for c in x)
        i=sum(c==1 for c in x)
        weights.append((w,e,i))
    den=comb(r*m,k)
    assert sum(w for w,e,i in weights)==den
    e_num=sum(w*e for w,e,i in weights)
    i_num=sum(w*i for w,e,i in weights)
    ei_num=sum(w*e*i for w,e,i in weights)
    return Fraction(ei_num,den)-Fraction(e_num*i_num,den*den)

def subset_cov(r,m,k):
    """Literal graph enumeration from induced vertex sets."""
    n=r*m
    subsets=list(combinations(range(n),k))
    e_sum=i_sum=ei_sum=0
    for s in subsets:
        e=0;i=0
        for a in range(r):
            block=set(range(a*m,(a+1)*m))
            count=sum(v in block for v in s)
            e+=count*(count-1)//2
            if count==1:i+=1
        e_sum+=e; i_sum+=i; ei_sum+=e*i
    den=len(subsets)
    return Fraction(ei_sum,den)-Fraction(e_sum*i_sum,den*den)

def bernoulli_cov(r,m,p):
    """Independent product across cliques using exact binomial occupancy weights."""
    e1=i1=ei1=Fraction(0)
    for j in range(m+1):
        prob=comb(m,j)*p**j*(1-p)**(m-j)
        e=j*(j-1)//2;i=int(j==1)
        e1+=prob*e;i1+=prob*i;ei1+=prob*e*i
    return r*(ei1-e1*i1)

assertions=0
for r in range(2,7):
    for m in range(2,7):
        if (m+1)**r > 80000:continue
        for k in range(r*m+1):
            actual=occupancy_cov(r,m,k)
            predicted=formula(r,m,k)
            assert actual==predicted,(r,m,k,actual,predicted)
            assertions+=1
            if m>=3:
                expected=(0 if k in (0,1) or k>=(r-1)*m+2 else -1 if k<2*r else +1)
                assert (actual>0)-(actual<0)==expected,(r,m,k,expected,actual)
                assertions+=1
            if r*m<=12:
                assert subset_cov(r,m,k)==actual,(r,m,k)
                assertions+=1
for r in range(2,5):
    for m in range(2,7):
        for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            actual=bernoulli_cov(r,m,p)
            predicted=-r*comb(m,2)*m*p**3*(1-p)**(m-1)
            assert actual==predicted,(r,m,p,actual,predicted)
            assertions+=1
for r in range(2,8):
    k=2*r
    expected=Fraction(2*(2*r-1),r-1)*Fraction(r-1,r)**(2*r-1)
    vals=[m*formula(r,m,k) for m in (50,100,200,500)]
    assert abs(vals[-1]-expected)<abs(vals[-2]-expected)
    assertions+=1
print(f'PASS: {assertions} exact assertions; all tested covariance identities, sign phases, and ensemble contrast agree.')
