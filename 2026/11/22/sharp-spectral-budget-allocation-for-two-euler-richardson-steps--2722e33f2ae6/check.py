"""Standalone numerical and exact-rational checks for two-step minimax spectral allocation."""
from math import sqrt
from fractions import Fraction
from random import Random


def thresholds(k):
    a = 2 / (k + 1)
    b = 4 * k / (k*k + 2*k - 1)
    c = 8 * (k+1) / (k*k + 6*k + 1)
    d = 4 / (1 + 2*k - k*k) if k < 1+sqrt(2) else float('inf')
    return a,b,c,d


def q_opt(k,t):
    a,b,c,d = thresholds(k)
    if t <= a:
        return 0.
    if t <= b:
        return (t*(1+k)-2)/(1+k*k)
    if t <= c:
        return (t-2 + sqrt((t-2)**2+t*t))/2
    if t <= d:
        return (t*k-2+sqrt((t*k-2)**2+(t*k)**2))/(2*k*k)
    return (t*(1+k)-2)/(1+k*k)


def norm(k,t,q):
    vals=[1-t+q,1-t*k+q*k*k]
    if q > 0:
        vertex=t/(2*q)
        if 1 < vertex < k:
            vals.append(1-t*vertex+q*vertex*vertex)
    return max(map(abs,vals))


def golden_min(k,t):
    lo,hi=0.,t*t/4
    for _ in range(115):
        x=lo+(hi-lo)*.3819660112501051
        y=lo+(hi-lo)*.6180339887498949
        if norm(k,t,x)>norm(k,t,y):lo=x
        else:hi=y
    return (lo+hi)/2


def run():
    rng=Random(9017)
    cases=0
    for k in (1.0001,1.02,1.2,1.5,1.99,2.,2.01,2.3,1+sqrt(2),2.5,3.,5.,10.,100.):
        a,b,c,d=thresholds(k)
        assert 0<a<b<c
        if d!=float('inf'):assert d>c
        budgets=[a,b,c,2/k,2.,4/k,8/k, .5*a,1.5*a,.8*b,1.3*b,.9*c,1.1*c]
        if d!=float('inf'):budgets.extend([.9*d,d,1.1*d])
        budgets.extend([10**rng.uniform(-3,2) for _ in range(120)])
        for t in budgets:
            q=q_opt(k,t)
            assert -1e-12 <= q <= t*t/4+1e-12,(k,t,q)
            f=norm(k,t,q)
            qb=golden_min(k,t)
            # The branch formula and a completely independent scalar minimization agree in objective.
            assert f <= norm(k,t,qb)+3e-9*max(1.,f), (k,t,q,qb,f)
            assert f <= norm(k,t,0)+1e-9*max(1.,f)
            assert f <= norm(k,t,t*t/4)+1e-9*max(1.,f)
            cases+=1
    # Exact checks with rational data (no floating point).
    for k,t in [(Fraction(5),Fraction(2,5)),(Fraction(5),Fraction(1,2)),
                (Fraction(2),Fraction(8)),(Fraction(3,2),Fraction(6))]:
        q=(t*(1+k)-2)/(1+k*k)
        assert (1-t+q) == -(1-t*k+q*k*k)
    # Sharp stability window, independently checking both sides numerically.
    for k in (1.001,1.2,1.7,2.,2.01,3.,10.,50.):
        tcap=2*k/(k-1) if k<=2 else 8/k
        assert abs(norm(k,tcap,q_opt(k,tcap))-1)<1e-9
        for f in (0.95,0.99,1.01,1.05):
            t=tcap*f
            v=norm(k,t,q_opt(k,t))
            assert (v<1 if f<1 else v>1), (k,t,v)
    print('PASS:',cases,'independent minimax comparisons; four exact-rational endpoint balances; eight sharp stability-boundary tests')

if __name__=='__main__': run()
