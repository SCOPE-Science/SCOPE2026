"""Checks for the exact two-pulse saturating-response scheduling theorem.

No finite computation substitutes for the analytic uniqueness proof.
"""
import math
import random
import sympy as sp
from scipy.integrate import quad


def objective(a, b, h, t):
    q = math.exp(-h)
    x = math.exp(-t)
    return math.log((1+a)*(1+a*x+b)/((1+a*x)*(1+a*q+b*q/x)))


def optimal_time(a, b, h):
    q = math.exp(-h)
    root = q + math.sqrt(q*q + q*(1+b)/a)
    return -math.log(min(1., root))


def direct_integral(a, b, h, t):
    before = quad(lambda s: a*math.exp(-s)/(1+a*math.exp(-s)), 0., t,
                  epsabs=1e-12)[0]
    after = quad(lambda s: (a*math.exp(-s)+b*math.exp(-(s-t)))/
                 (1+a*math.exp(-s)+b*math.exp(-(s-t))),t,h,
                 epsabs=1e-12)[0]
    return before+after


def run():
    a,b,q,x = sp.symbols('a b q x', positive=True)
    f=(1+a*x+b)/((1+a*x)*(1+a*q+b*q/x))
    signed=sp.factor(sp.diff(f,x))
    expected=-b*(a*x*x-2*a*q*x-q*(1+b))/((1+a*x)**2*(a*q*x+b*q+x)**2)
    assert sp.simplify(signed-expected)==0
    # The derivative numerator has one positive zero, lying above q.
    count=1
    rng=random.Random(410259)
    for j in range(2800):
        aa=10**rng.uniform(-2,2)
        bb=10**rng.uniform(-2,2)
        hh=rng.uniform(0.04,15)
        tt=optimal_time(aa,bb,hh)
        assert -1e-12<=tt<=hh+1e-12
        count+=1
        # Exact logarithmic antiderivative equals two independent numerical integrations.
        chosen=rng.uniform(0,hh)
        assert abs(objective(aa,bb,hh,chosen)-direct_integral(aa,bb,hh,chosen))<1e-9
        count+=1
        best=objective(aa,bb,hh,tt)
        for p in range(9):
            trial=hh*p/8
            assert best>=objective(aa,bb,hh,trial)-2e-11
            count+=1
        boundary=math.log((2*aa+bb+1)/aa)
        if hh<=boundary-1e-9:
            assert abs(tt)<1e-10
        elif hh>boundary+1e-9:
            assert 0<tt<hh
        count+=1
        if aa>1+bb:
            mid=2*math.log(2*aa/(aa-1-bb))
            if hh>max(boundary,mid)+1e-8:
                assert tt>hh/2
                count+=1
            elif boundary+1e-8<hh<mid-1e-8:
                assert 0<tt<hh/2
                count+=1
        else:
            assert tt<hh/2+1e-10
            count+=1
    # Distinct regimes for a large first pulse and smaller later pulse.
    aa,bb=4,1
    h0=math.log((2*aa+bb+1)/aa)
    hm=2*math.log(2*aa/(aa-1-bb))
    assert abs(h0-math.log(2.5))<1e-12;count+=1
    assert abs(hm-math.log(16))<1e-12;count+=1
    assert optimal_time(aa,bb,h0-0.1)==0;count+=1
    assert 0<optimal_time(aa,bb,2)<1;count+=1
    assert optimal_time(aa,bb,4)>2;count+=1
    print('PASS',count,'assertions')
    print('sample', 'h=4, a=4, b=1', 'optimal delay', format(optimal_time(4,1,4),'.12f'),
        'integrated response',format(objective(4,1,4,optimal_time(4,1,4)),'.12f'),
        'synchronous response',format(objective(4,1,4,0),'.12f'))

if __name__=='__main__':run()
