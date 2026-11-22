#!/usr/bin/env python3
"""Exact rational checks accompanying the parallel-recycling equilibrium theorem.

Numerical/finite assertions supplement the general analytic proof in RESULT.md.
No external dependencies are needed.
"""
from fractions import Fraction as Q


def rhs(x, loading, removal, components):
    x = Q(x)
    return loading - removal*x + sum((r*x*x/(k*k+x*x) for k,r in components), Q(0))


def polynomial_mul(p, q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j] += a*b
    return out


def polynomial_add(p, q):
    out = [Q(0)]*max(len(p),len(q))
    for i,a in enumerate(p):out[i] += a
    for i,b in enumerate(q):out[i] += b
    return out


def numerator(loading, removal, components):
    terms = [[k*k,Q(0),Q(1)] for k,r in components]
    denominator = [Q(1)]
    for t in terms:denominator=polynomial_mul(denominator,t)
    result=polynomial_mul([loading,-removal],denominator)
    for i,(k,r) in enumerate(components):
        numerator_others=[Q(1)]
        for j,t in enumerate(terms):
            if j != i:numerator_others=polynomial_mul(numerator_others,t)
        result=polynomial_add(result,polynomial_mul([Q(0),Q(0),r],numerator_others))
    return result


def checks():
    count=0
    L=Q(1,10)
    example=[(Q(1),Q(7,4)),(Q(50),Q(300))]
    xvals=[Q(0),Q(1,5),Q(1),Q(2),Q(6),Q(500)]
    exact_expected=[Q(1,10),-Q(906517,32500520),Q(9499,100040),-Q(13,626),Q(7199,117290),-Q(50783079899,252501010)]
    vals=[rhs(x,L,Q(1),example) for x in xvals]
    for v,z in zip(vals,exact_expected):
        assert v==z, (v,z)
        count+=1
    assert all((v>0 if i%2==0 else v<0) for i,v in enumerate(vals))
    count+=1
    p=numerator(L,Q(1),example)
    assert len(p)==6 and p[-1]==-1 and p[0]>0
    count+=1
    for x in xvals:
        d=(1+x*x)*(2500+x*x)
        assert rhs(x,L,Q(1),example)*d==sum(c*x**i for i,c in enumerate(p))
        count+=1

    # Produce exact alternating sign witnesses for m=0,1,2,3,4.
    components=[]
    witnesses=[Q(0),Q(1)]
    for m in range(5):
        values=[rhs(x,L,Q(1),components) for x in witnesses]
        assert len(witnesses)==2*m+2
        count+=1
        for i, val in enumerate(values):
            assert (val>0 if i%2==0 else val<0)
            count+=1
        p=numerator(L,Q(1),components)
        assert len(p)==2*m+2 and p[-1]==-1
        count+=1
        if m==4:break
        k=max(2,int(witnesses[-1])+1,int(L+sum((r for _,r in components),Q(0)))+2)
        while True:
            proposed=components+[(Q(k),Q(3*k))]
            if all((rhs(x,L,Q(1),proposed)>0 if i%2==0 else rhs(x,L,Q(1),proposed)<0) for i,x in enumerate(witnesses)) and rhs(Q(k),L,Q(1),proposed)>0 and rhs(Q(4*k),L,Q(1),proposed)<0:
                break
            k*=2
            assert k<10**50
        witnesses.extend([Q(k),Q(4*k)])
        components=proposed
        count+=1
    return count


if __name__=='__main__':
    print('Exact rational assertions passed:', checks())
