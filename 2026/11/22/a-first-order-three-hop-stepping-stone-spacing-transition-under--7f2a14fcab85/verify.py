#!/usr/bin/env python3
"""Numerical checks for the three-gap independent movement model.

These checks corroborate the analytic constrained-extrema proof; they do not
replace it or establish field validity or historical priority.
"""
import math
import random
from decimal import Decimal, localcontext

def branch(s):
    assert s >= math.sqrt(8)
    x = 2.0 / (s + math.sqrt(s*s - 8.0))
    return x, x, 1.0/x

def logcost(gs):
    return sum(math.log1p(g*g) for g in gs)

def delta(s):
    return logcost(branch(s)) - 3*math.log1p((s/3)**2)

def threshold():
    lo, hi = math.sqrt(8), 3.0
    assert delta(lo) > 0 and delta(hi) < 0
    for _ in range(100):
        mid = (lo + hi)/2
        if delta(mid) > 0: lo = mid
        else: hi = mid
    return (lo+hi)/2

def dc_branch(s):
    with localcontext() as ctx:
        ctx.prec = 65
        sd = Decimal(str(s))
        x = Decimal(2)/(sd + (sd*sd-Decimal(8)).sqrt())
        return 2*(Decimal(1)+x*x).ln() + (Decimal(1)+1/(x*x)).ln() - 3*(Decimal(1)+(sd/3)**2).ln()

def test():
    t = threshold()
    checks=0
    assert 2.8475678593 < t < 2.8475678594
    checks += 1
    assert (Decimal(27)/4) > (Decimal(17)/9)**3
    assert (Decimal(125)/16) < Decimal(8)
    checks+=2
    # Independently compute threshold using high precision decimals.
    with localcontext() as ctx:
        ctx.prec=65
        a,b=Decimal(8).sqrt(),Decimal(3)
        for _ in range(215):
            m=(a+b)/2
            x=Decimal(2)/(m+(m*m-8).sqrt())
            diff=2*(1+x*x).ln() + (1+1/(x*x)).ln()-3*(1+(m/3)**2).ln()
            if diff>0:a=m
            else:b=m
        assert abs((a+b)/2-Decimal('2.84756785934625263821770427496415706639892213848596')) < Decimal('1e-43')
        checks+=1
    rng = random.Random(60414)
    # Uniform and reciprocal-gap candidates, checked against random feasible triples.
    for s in [0.001,0.25,0.5,1,1.99,2,2.1,2.7,2.8,
              math.sqrt(8),2.83,2.84,t-0.001,t,t+0.001,2.86,2.9,2.99,
              3,3.01,3.5,4,6,10,100]:
        uniform = (s/3,)*3
        candidate = uniform if s < t else branch(s)
        best = logcost(candidate)
        assert (s<t or logcost(candidate)<=logcost(uniform)+1e-13)
        checks+=1
        for _ in range(2400):
            a,b,c=[rng.expovariate(1) for j in range(3)]
            z=a+b+c
            v=(a*s/z,b*s/z,c*s/z)
            assert logcost(v)>=best-3e-12,(s,v,best)
            checks+=1
        # Boundary is not globally optimal, including where discontinuous branch wins.
        for a in [0,s/10,s/2,s]:
            assert logcost((a,s-a,0))>best-1e-12
            checks+=1
    # Strict local existence interval: nonuniform minimizer and uniform both stable.
    for s in [2.83,2.84,2.9,2.99]:
        x,_,large=branch(s)
        assert x < 2**-0.5 and large > 1
        assert s/3 < 1
        checks+=3
    # The two-gap optimization is continuous at 2 and has a complete exact identity.
    for s in [0.1,0.5,1.2,1.9,2,2.1,3,4,8]:
        v=(s/2,s/2) if s<=2 else ((s-math.sqrt(s*s-4))/2,(s+math.sqrt(s*s-4))/2)
        q=math.prod(1+y*y for y in v)
        for j in range(901):
            a=s*j/900; b=s-a
            r=(1+a*a)*(1+b*b)
            assert r >= q-1e-10
            assert abs(r-(s*s+(a*b-1)**2))<1e-10
            checks+=2
    return checks,t

if __name__=='__main__':
    c,t=test()
    print('CHECKS_PASSED', c)
    print('THRESHOLD', format(t,'.15f'))
    print('DIMENSIONLESS_SHORT_AND_LONG', *(format(v,'.15f') for v in branch(t)))
