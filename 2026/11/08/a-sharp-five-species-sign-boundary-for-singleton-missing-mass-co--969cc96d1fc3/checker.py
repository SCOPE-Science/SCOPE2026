"""Exact reproducibility checks for singleton count vs unobserved species mass.
Only Python standard library; run with python checker.py.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def algebraic_moments(p, n):
    """Joint moment identity for any normalized finite rational vector."""
    zero = F(0)
    em = sum((x * (1-x)**n for x in p), zero)
    es = n * sum((x*(1-x)**(n-1) for x in p), zero)
    ems = n * sum((p[i]*p[j]*(1-p[i]-p[j])**(n-1)
                   for i in range(len(p)) for j in range(len(p)) if i != j), zero)
    return em, es, ems, ems - em*es


def brute_moments(p, n):
    em=es=ems=F(0)
    for draw in product(range(len(p)), repeat=n):
        probability=F(1)
        count=[0]*len(p)
        for i in draw:
            probability*=p[i]
            count[i]+=1
        unseen=sum((p[i] for i in range(len(p)) if count[i]==0), F(0))
        singletons=sum(c==1 for c in count)
        em+=probability*unseen
        es+=probability*singletons
        ems+=probability*unseen*singletons
    return em,es,ems,ems-em*es


def add(P,Q):
    out=P.copy()
    for k,v in Q.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}


def mul(P,Q):
    out={}
    for a,x in P.items():
        for b,y in Q.items():
            z=tuple(t+u for t,u in zip(a,b))
            out[z]=out.get(z,0)+x*y
    return {k:v for k,v in out.items() if v}


def scale(P,c):return {k:c*v for k,v in P.items() if c*v}

def polynomial_certificate():
    """Coefficientwise exact verification of the four-variable SOS identity."""
    v=[{tuple(int(i==j) for i in range(4)):1} for j in range(4)]
    P={};Q={};R={}
    for x in v:
        P=add(P,x);Q=add(Q,mul(x,x));R=add(R,mul(mul(x,x),x))
    left=add(scale(mul(P,mul(Q,Q)),2),scale(mul(add(mul(P,P),Q),R),-1))
    right={}
    for i in range(4):
        others=[j for j in range(4) if j!=i]
        for j,k in combinations(others,2):
            d=add(v[j],scale(v[k],-1))
            right=add(right,mul(mul(mul(v[i],v[i]),v[i]),mul(d,d)))
    for i,j in combinations(range(4),2):
        for k in range(4):
            if k not in (i,j):
                right=add(right,scale(mul(mul(mul(v[i],v[i]),mul(v[j],v[j])),v[k]),4))
    assert left==right
    assert len(left)>0
    return len(left)


def compositions(s,k):
    if k==1:yield (s,);return
    for a in range(1,s-k+2):
        for tail in compositions(s-a,k-1):yield (a,)+tail


def two_level_moments(a, L, n):
    b=(1-a)/L
    em=a*(1-a)**n+L*b*(1-b)**n
    es=n*(a*(1-a)**(n-1)+L*b*(1-b)**(n-1))
    ems=n*(2*L*a*b*(1-a-b)**(n-1)+L*(L-1)*b*b*(1-2*b)**(n-1))
    return ems-em*es


def main():
    tests=0
    terms=polynomial_certificate()
    tests+=1
    assert terms>=1
    # Exact independent outcome enumeration vs joint identity, not simulations.
    for m in range(2,6):
        for n in range(2,6):
            for d in (m+1,m+2):
                for parts in compositions(d,m):
                    p=tuple(F(t,d) for t in parts)
                    assert algebraic_moments(p,n)==brute_moments(p,n)
                    tests+=1
    # Strict negative covariance for every tested 2--4 species distribution.
    for m in range(2,5):
        for d in range(m,13):
            for parts in compositions(d,m):
                p=[F(t,d) for t in parts]
                assert algebraic_moments(p,2)[3]<0
                tests+=1
    # A five-species rational witness and direct exact outcome replay.
    p=(F(4,5),F(1,20),F(1,20),F(1,20),F(1,20))
    assert algebraic_moments(p,2)==brute_moments(p,2)
    assert algebraic_moments(p,2)==(F(17,80),F(7,10),F(3,20),F(1,800))
    tests+=1
    # For each n, the two-level family approaches an explicit positive limit.
    a=F(3,5)
    for n in range(2,11):
        limit=float(n*a*a*(1-a)**n*(1-(1-a)**(n-1)))
        observed=float(two_level_moments(a,200000,n))
        assert observed>0 and abs(observed-limit) < 0.00015
        assert algebraic_moments((F(1,2),F(1,2)),n)[3] < 0
        tests+=1
    print('PASS',tests,'exact moment, certificate, boundary, and limiting checks; monomials',terms)


if __name__=='__main__':main()
