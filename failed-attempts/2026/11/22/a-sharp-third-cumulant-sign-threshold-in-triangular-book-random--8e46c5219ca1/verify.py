"""Independent exact-state checks for FK third cumulants on triangular books."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt, log


def components(edges, mask, n):
    p=list(range(n))
    def root(x):
        while p[x]!=x:
            x=p[x]
        return x
    for k,(a,b) in enumerate(edges):
        if mask>>k&1:
            ra,rb=root(a),root(b)
            if ra!=rb: p[rb]=ra
    return len({root(i) for i in range(n)})


def exact_enumerate(m,q,v):
    edges=[(0,1)] + [(0,i+2) for i in range(m)] + [(1,i+2) for i in range(m)]
    moment=[F(0) for _ in range(4)]
    Z=F(0)
    for mask in range(1<<len(edges)):
        weight=q**components(edges,mask,m+2)*v**mask.bit_count()
        Z+=weight
        for r in range(4):
            if all((mask>>(1+i)&1) and (mask>>(1+m+i)&1) for i in range(r)):
                moment[r]+=weight
    return tuple(x/Z for x in moment)


def theorem(m,q,v):
    A=q+2*v
    B=A+v*v
    den=(q-1)*A**m+(1+v)*B**m
    theta=(1+v)*B**m/den
    p=v*v/B
    return tuple(theta*p**r if r else F(1) for r in range(4))


def run():
    ntests=0
    for m in [3,4,5]:
        for q in [F(3,2),F(2),F(3),F(4)]:
            for v in [F(1,5), F(3,4), F(2)]:
                actual=exact_enumerate(m,q,v)
                predicted=theorem(m,q,v)
                for a,b in zip(actual,predicted):
                    assert a==b,(m,q,v,a,b)
                    ntests+=1
                # all 3-distinct joint cumulants match the derived factorization
                k=actual[3]-3*actual[2]*actual[1]+2*actual[1]**3
                A=q+2*v; B=A+v*v
                theta=(1+v)*B**m/((q-1)*A**m+(1+v)*B**m)
                p=v*v/B
                assert k==theta*(1-theta)*(1-2*theta)*p**3
                ntests+=1
                # positive correlation is retained for any two different pages when q>1
                assert actual[2]>actual[1]**2
                ntests+=1
                # exact sign change test using the algebraic criterion
                expected=(1 if (q-1)*A**m>(1+v)*B**m else -1)  # equality possible at special input; none used
                assert k*expected>=0
                ntests+=1
    # Critical scaling numerical spot-check; not used to prove limit.
    for q in [3.,4.,7.]:
        cutoff=sqrt(q*log(q-1))
        for a in [.7*cutoff,1.3*cutoff]:
            m=4000
            v=a/sqrt(m)
            A=q+2*v; B=A+v*v
            R=(q-1)/(1+v)*(A/B)**m
            theta=1/(1+R)
            p=v*v/B
            k3=theta*(1-theta)*(1-2*theta)*p**3
            assert (k3>0)==(a<cutoff)
            ntests+=1
    print(f"FK_BOOK_EXACT_CHECKS_PASSED {ntests}")

if __name__=='__main__':
    run()
