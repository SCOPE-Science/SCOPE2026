"""Independent finite checks for sharp worst-mixture Gabor frame lower bounds.
Only standard Python; diagnostics do not establish infinite mathematical claims.
"""
import cmath
import math
import random


def quantities(a, b, q):
    rho = math.exp(-a/q)
    sig = math.exp(-b/q)
    u = sum(rho**(2*j) for j in range(q))
    v = sum(sig**(2*j) for j in range(q))
    w = sum((rho*sig)**j for j in range(q))
    delta = u-w*w/v
    r = rho**q
    s = sig**q
    bound = rho*rho*delta/(1+r)**2
    cstar = (rho/sig)*(1+s)/(1+r)*w/v
    return bound, cstar, delta, (rho, sig, u, v, w)


def fiber(a, b, q, c, x, theta):
    z = cmath.exp(1j*theta)
    r, s = math.exp(-a), math.exp(-b)
    return sum(abs(math.exp(-a*(x+j/q))/(1-r*z) - c*math.exp(-b*(x+j/q))/(1-s*z))**2 for j in range(q))


def direct_fiber(a, b, q, c, x, theta, steps=120):
    # Independently sum actual samples, not the closed-form geometric Zak series.
    z = cmath.exp(1j*theta)
    return sum(abs(sum((math.exp(-a*(x+j/q+n))-c*math.exp(-b*(x+j/q+n)))*z**n for n in range(steps)))**2 for j in range(q))


def check():
    rng = random.Random(271828)
    cases = [(2.3,0.7,2), (0.8,0.5,3), (4.0,2.0,4), (1.01,1.0,6), (3.0,5.0,7)]
    count = 0
    for a,b,q in cases:
        exact,cstar,delta,(rho,sig,u,v,w)=quantities(a,b,q)
        assert delta>0 and exact>0 and cstar>0
        edge = fiber(a,b,q,cstar,1/q,math.pi)
        assert abs(edge-exact) < 5e-12*max(1,exact)
        for _ in range(190):
            x=rng.random()/q
            theta=2*math.pi*rng.random()
            c=(rng.uniform(-2,2)+1j*rng.uniform(-2,2))*cstar
            val=fiber(a,b,q,c,x,theta)
            assert val >= exact-1e-11, (a,b,q,val,exact)
            if count%19 == 0:
                summation=direct_fiber(a,b,q,c,x,theta)
                assert abs(summation-val)<1e-10*max(1,val)
            count+=1
        for shift in [0.002,0.001,0.0005]:
            aa=b+shift
            bound,_,_,_=quantities(aa,b,q)
            sig=math.exp(-b/q)
            S0=sum(sig**(2*j) for j in range(q))
            S1=sum(j*sig**(2*j) for j in range(q))
            S2=sum(j*j*sig**(2*j) for j in range(q))
            coeff=sig**2/(q*q*(1+math.exp(-b))**2)*(S2-S1*S1/S0)
            assert abs(bound/(shift*shift)/coeff-1)<0.04
    # A single channel can cancel, so oversampling really matters.
    for a,b in [(2.3,.7),(.8,.5)]:
        c=(1+math.exp(-b))/(1+math.exp(-a))
        assert abs(fiber(a,b,1,c,0,math.pi))<1e-25
    print('TWO_DECAY_GABOR_CHECKS_PASS', count, 'grid samples; 5 edge and coalescence parameter cases')

if __name__=='__main__':
    check()
