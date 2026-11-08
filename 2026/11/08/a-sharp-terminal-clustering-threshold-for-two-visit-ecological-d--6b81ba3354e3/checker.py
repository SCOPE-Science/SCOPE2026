#!/usr/bin/env python3
"""Independent finite checks for a two-occasion colonization-detection design.
Scientific proof is in RESULT.md; this checker is diagnostic only.
No external inputs or packages beyond the Python standard library.
"""
from fractions import Fraction as F
from random import Random
from math import exp, log, sqrt, isclose


def mm(v, mat):
    return [sum(v[i] * mat[i][j] for i in range(2)) for j in range(2)]


def trans(a, w):
    return [[1 - a * (1-w), a * (1-w)], [(1-a)*(1-w), a + (1-a)*w]]


def independent_success(a,d,x,y):
    """Start unoccupied. x=e^(-gamma*t1), y=e^(-gamma*(t2-t1))."""
    v = mm([F(1), F(0)], trans(a,x))
    v = [v[0], v[1]*(1-d)]
    v = mm(v, trans(a,y))
    v = [v[0], v[1]*(1-d)]
    return 1 - sum(v)


def formula(a,d,x,y):
    h=x*y
    return d*a*(2-x-h-d*(1-x)*(a+(1-a)*y))


def test_exact():
    rng=Random(12034)
    assertions=0
    for i in range(2500):
        a=F(rng.randint(1,18),rng.randint(19,50))
        d=F(rng.randint(1,18),rng.randint(19,50))
        x=F(rng.randint(1,18),rng.randint(19,50))
        y=F(rng.randint(1,18),rng.randint(19,50))
        assert independent_success(a,d,x,y)==formula(a,d,x,y)
        assertions+=1
        assert independent_success(a,d,x,y)<=F(1)
        assertions+=1
        assert independent_success(a,d,x,y)>=F(0)
        assertions+=1
    return assertions


def prob(c,e,d,t1,t2):
    g=c+e
    a=c/g
    return float(independent_success(a,d,exp(-float(g)*t1),exp(-float(g)*(t2-t1))))


def test_optimizers():
    rng=Random(7298); passed=0
    for i in range(100):
        c=rng.uniform(.12,2.9); e=rng.uniform(.13,3.2)
        d=rng.uniform(.05,.999); H=rng.uniform(.015,6.0)
        g=c+e; a=c/g
        r=d*(1-a)/(1-d*a)
        hc=-log(r)/g
        t1=H if H<=hc else (H+hc)/2
        pstar=prob(c,e,d,t1,H)
        pterminal=prob(c,e,d,H,H)
        h=exp(-g*H)
        gain=d*a*(1-d*a)*max(0,sqrt(r)-sqrt(h))**2
        assert isclose(pstar-pterminal,gain,abs_tol=2e-13), (i,pstar,pterminal,gain)
        passed+=1
        for i1 in range(21):
            v1=H*i1/20
            for i2 in range(i1,21):
                v2=H*i2/20
                assert pstar+1e-12>=prob(c,e,d,v1,v2),(c,e,d,H,t1,v1,v2)
                passed+=1
        assert prob(c,e,d,t1,H)>0
        passed+=1
    return passed


def example():
    c=e=1.0; d=.5; H=2.0
    a=.5; g=2; r=1/3
    hc=log(3)/2
    t1=(H+hc)/2
    return (hc,t1,prob(c,e,d,t1,H),prob(c,e,d,H,H),prob(c,e,d,t1,H)-prob(c,e,d,H,H))

if __name__=='__main__':
    num=test_exact()+test_optimizers()
    print('exact_and_numeric_checks_passed',num)
    print('example_Hc_t1_Poptimal_Pterminal_gain',example())
