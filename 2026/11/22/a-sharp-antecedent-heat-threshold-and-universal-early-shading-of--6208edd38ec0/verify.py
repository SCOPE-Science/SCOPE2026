"""Reproduce numerical checks for a one-block thermal-shading theorem.
Requires only Python 3 standard library. The mathematical proof is in RESULT.md.
"""
import math
import random


def quantities(H, d):
    assert H > d > 0
    return math.exp(-d), math.exp(-(H-d))


def cubic(q, m, rho, b, C):
    return ((m-1.0)*q**3
            + (2*C + b*(m-1.0)*C*C)*q
            - rho*(1-b)*C*C)


def critical_load(H, d, rho):
    b,C=quantities(H,d)
    return 1.0 - (2*C-rho*(1-b)*C*C)/(1+b*C*C)


def optimal_start(H,d,m,rho):
    b,C=quantities(H,d)
    if m >= critical_load(H,d,rho):
        return 0.0
    lo,hi=C,1.0
    assert cubic(lo,m,rho,b,C)>0 and cubic(hi,m,rho,b,C)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if cubic(mid,m,rho,b,C)>0: lo=mid
        else: hi=mid
    return -math.log((lo+hi)/2)


def exact_cost(H,d,s,m,rho):
    assert 0<=s<=H-d+1e-12
    b=math.exp(-d);q=math.exp(-s);r=math.exp(-(H-s-d))
    early=(s+2*(m-1)*(1-q)+(m-1)**2*(1-q*q)/2)
    v=1-rho; w=rho+(m-1)*q
    during=v*v*d+2*v*w*(1-b)+w*w*(1-b*b)/2
    A=rho*(1-b)-b*(m-1)*q
    L=H-s-d
    late=L-2*A*(1-r)+A*A*(1-r*r)/2
    return early+during+late


def derivative(H,d,s,m,rho):
    b,C=quantities(H,d);q=math.exp(-s)
    return rho*(1-b)*cubic(q,m,rho,b,C)/q**2


def state(t,H,d,s,m,rho):
    if t <= s: return 1+(m-1)*math.exp(-t)
    start=1+(m-1)*math.exp(-s)
    if t <= s+d: return 1-rho+(start-(1-rho))*math.exp(-(t-s))
    end=1-rho+(start-(1-rho))*math.exp(-d)
    return 1+(end-1)*math.exp(-(t-s-d))


def simpson(H,d,s,m,rho,N=2400):
    step=H/N
    total=state(0,H,d,s,m,rho)**2 + state(H,H,d,s,m,rho)**2
    for k in range(1,N):
        t=k*step
        total+=(4 if k&1 else 2)*state(t,H,d,s,m,rho)**2
    return total*step/3


def run():
    tests=0
    rng=random.Random(20241117)
    # Analytic pieces against direct time-domain numerical integration.
    for _ in range(250):
        H=rng.uniform(1.2,12); d=rng.uniform(.12,.9*H)
        m=rng.uniform(0,1.7);rho=rng.uniform(.05,1)
        s=rng.uniform(.02,H-d-.02) if H-d>.04 else (H-d)/2
        predicted=exact_cost(H,d,s,m,rho)
        measured=simpson(H,d,s,m,rho)
        assert abs(predicted-measured)<1e-5*(1+abs(predicted)),(H,d,s,m,rho,predicted,measured)
        tests+=1
        h=min(.000005,(H-d)/10,s/2,(H-d-s)/2)
        numeric=(exact_cost(H,d,s+h,m,rho)-exact_cost(H,d,s-h,m,rho))/(2*h)
        assert abs(numeric-derivative(H,d,s,m,rho))<1e-6*(1+abs(numeric)),(numeric,derivative(H,d,s,m,rho))
        tests+=1
    # Complete stationary-point classification and global optimality by grid stress tests.
    for _ in range(500):
        H=rng.uniform(.4,12);d=rng.uniform(.05*H,.95*H)
        m=rng.uniform(0,2.0);rho=rng.uniform(.05,1)
        b,C=quantities(H,d)
        assert cubic(C,m,rho,b,C)>0
        assert cubic(1,m,rho,b,C)==cubic(1,m,rho,b,C)
        s=optimal_start(H,d,m,rho)
        assert 0<=s<(H-d)/2+1e-10
        Jmin=exact_cost(H,d,s,m,rho)
        for i in range(101):
            z=(H-d)*i/100
            assert Jmin <= exact_cost(H,d,z,m,rho)+1e-10*(1+Jmin),(H,d,m,rho,s,z)
            tests+=1
        if s>1e-8:
            assert abs(derivative(H,d,s,m,rho))<3e-9
            tests+=1
    # Increase initial load -> shade earlier. Increase shade strength -> shade later.
    for _ in range(200):
        H=rng.uniform(2,11);d=rng.uniform(.2,H*.7)
        rho=rng.uniform(.1,.9)
        a=optimal_start(H,d,0.0,rho)
        z=optimal_start(H,d,.4,rho)
        assert z<=a+1e-10
        tests+=1
        b=optimal_start(H,d,0.0,min(1,rho+.05))
        assert b>=a-1e-10
        tests+=1
    # Asymptotic universal offset in thermal time units.
    for m in (0.,.1,.2,.5,.8):
        for rho in (.2,.5,1.0):
            H,d=40.,1.5
            s=optimal_start(H,d,m,rho)
            target=(H-d)/2-0.5*math.log(2/(1-m))
            assert abs(s-target)<.001,(m,rho,s,target)
            tests+=1
    H,d,m,rho=4,1,0,1
    s0=optimal_start(H,d,m,rho)
    print('checked_assertions',tests)
    print('example',{'H':H,'d':d,'initial':m,'shade_fraction':rho,
                     'critical_initial_load':critical_load(H,d,rho),
                     'optimal_start':s0,
                     'cost_at_optimum':exact_cost(H,d,s0,m,rho),
                     'cost_at_start':exact_cost(H,d,0,m,rho)})

if __name__=='__main__':
    run()
