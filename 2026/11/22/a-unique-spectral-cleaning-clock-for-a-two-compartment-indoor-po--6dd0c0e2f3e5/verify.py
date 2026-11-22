#!/usr/bin/env python3
"""Independent numerical checks for a two-compartment air/surface cleaning theorem.

No external packages or network calls are used. Analytical arguments, not these
finite checks, establish the claims for all positive model parameters.
"""
import math
import random


def rates(v, a, d):
    disc = math.sqrt((v+a+d)**2-4*v*d)
    return ((v+a+d+disc)/2, (v+a+d-disc)/2)


def f(t, r, s):
    return math.exp(-s*t)*(-math.expm1(-(r-s)*t))


def L(t, r, s):
    return -math.expm1(-s*t)/s + math.expm1(-r*t)/r


def fprime(t, r, s):
    return -s*math.exp(-s*t)+r*math.exp(-r*t)


def reduction(t, T, v, a, d, q, Q=1.):
    r,s=rates(v,a,d)
    return q*Q*a*d/(r-s)**2 * f(t,r,s)*L(T-t,r,s)


def optimal(T, r, s):
    t0=math.log(r/s)/(r-s)
    lo=1.e-12*min(T,1)
    hi=min(T-1.e-12*min(T,1),t0)
    for _ in range(85):
        t=(lo+hi)/2
        score=fprime(t,r,s)/f(t,r,s)-f(T-t,r,s)/L(T-t,r,s)
        if score>0:
            lo=t
        else:
            hi=t
    return (lo+hi)/2


def rk4_exposure(T, tau, v, a, d, q, Q=1., n=4000):
    """Integrate air exposure without using the modal closed formula."""
    def step(y, h):
        def rate(z):
            g,w,ex=z
            return (-(v+a)*g+d*w, a*g-d*w, g)
        k1=rate(y)
        k2=rate(tuple(y[i]+h*k1[i]/2 for i in range(3)))
        k3=rate(tuple(y[i]+h*k2[i]/2 for i in range(3)))
        k4=rate(tuple(y[i]+h*k3[i] for i in range(3)))
        return tuple(y[i]+h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(3))
    def loop(y, duration):
        h=duration/n
        for _ in range(n):
            y=step(y,h)
        return y
    g,w,ex=loop((Q,0.,0.),tau)
    yclean=loop((g,(1-q)*w,ex),T-tau)
    ybase=loop((Q,0.,0.),T)
    return ybase[2]-yclean[2]


def run():
    rng=random.Random(57893)
    checks=0
    # Parameter stress tests: unique stationary point and exact global superiority.
    for j in range(500):
        v=math.exp(rng.uniform(-2,0.5))
        a=math.exp(rng.uniform(-2,0.7))
        d=math.exp(rng.uniform(-2,0.7))
        T=rng.uniform(0.6,9)
        q=rng.uniform(0.05,1)
        r,s=rates(v,a,d)
        assert 0<s<d<r
        tau=optimal(T,r,s)
        assert 0<tau<min(T,math.log(r/s)/(r-s))
        peak=reduction(tau,T,v,a,d,q)
        for k in range(61):
            t=T*k/60
            assert peak+1e-11>=reduction(t,T,v,a,d,q)
            checks+=1
        eps=min(1e-5,T/2000)
        if tau>eps and tau<T-eps:
            assert reduction(tau,T,v,a,d,q)>reduction(tau-eps,T,v,a,d,q)
            assert reduction(tau,T,v,a,d,q)>reduction(tau+eps,T,v,a,d,q)
            checks+=2
        if j<30:
            target=rk4_exposure(T,tau,v,a,d,q,n=2200)
            assert math.isclose(target,peak,rel_tol=4e-8,abs_tol=2e-9), (target,peak)
            checks+=1
    # Spectral invariance: different physical coefficient triples, same eigenmodes.
    s,r=.15,2.4
    triple=[]
    for d in [.3,.8,1.8]:
        v=r*s/d
        a=r+s-v-d
        assert v>0 and a>0
        triple.append((v,a,d))
    vals=[optimal(7,*rates(*p)) for p in triple]
    assert max(vals)-min(vals)<1e-12
    checks+=1
    # Universal 1/3 short-horizon and reservoir-peak long-horizon laws.
    v,a,d=.3,.8,.4
    r,s=rates(v,a,d)
    t0=math.log(r/s)/(r-s)
    small=.007
    tsmall=optimal(small,r,s)
    pred=small/3-(r+s)*small*small/81
    assert abs(tsmall-pred)<2e-7
    checks+=1
    long=40
    tlong=optimal(long,r,s)
    predlong=math.exp(-s*(long-t0))/(r-s)
    assert abs((t0-tlong)/predlong-1)<.04
    checks+=1
    # Reproducible illustration: rates and 12-hour horizon are illustrative,
    # not fitted to any experimental house.
    v,a,d,T,q=.2,1.,.1,12.,.5
    r,s=rates(v,a,d)
    tau=optimal(T,r,s)
    delta=reduction(tau,T,v,a,d,q)
    assert abs(tau-1.95469719567)<3e-8
    assert abs(delta-.23518990568)<3e-8
    assert delta>reduction(6.,T,v,a,d,q)
    checks+=3
    print('PASS',checks,'numerical comparisons; example optimal time:',format(tau,'.12f'),
          'exposure benefit:',format(delta,'.12f'))


if __name__=='__main__':
    run()
