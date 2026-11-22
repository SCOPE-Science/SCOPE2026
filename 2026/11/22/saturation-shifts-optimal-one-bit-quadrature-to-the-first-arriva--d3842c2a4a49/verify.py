"""Numerical checks for one-bit event-count path quadrature (standard library)."""
import math
import random
from statistics import mean


def bit_information_poisson(rate, t):
    if not (rate > 0 and 0 < t <= 1):
        raise ValueError('rate>0 and 0<t<=1 required')
    return rate**2 * (t-t*t/2)**2 / math.expm1(rate*t)


def bit_information_fixed(m, t):
    if not (isinstance(m,int) and m>=1 and 0<t<1):
        raise ValueError('m>=1 and 0<t<1 required')
    q=(1-t)**m
    return (m*m*t*t*q)/(4*(1-q))


def bisect(f, l, r, iterations=100):
    fl=f(l)
    fr=f(r)
    assert fl*fr<0
    for _ in range(iterations):
        mid=(l+r)/2
        fm=f(mid)
        if fm*fl>0:
            l,fl=mid,fm
        else:
            r,fr=mid,fm
    return (l+r)/2


def optimum_poisson(rate):
    def f(t):
        z=rate*t
        return z/(-math.expm1(-z))-2*(1-t)/(1-t/2)
    return bisect(f, 1.e-9,1.0)


def optimum_fixed(m):
    return bisect(lambda t:2*sum((1-t)**k for k in range(1,m+1))-m, 1.e-12,1.0)


def pois_sample(rng, lam):
    p=1.
    k=0
    bound=math.exp(-lam)
    while p>bound:
        p*=rng.random()
        k+=1
    return k-1


def empirical_information(xs, ys):
    mx=mean(xs)
    my=mean(ys)
    cov=mean((x-mx)*(y-my) for x,y in zip(xs,ys))
    vy=mean((y-my)**2 for y in ys)
    return cov**2/vy


def run():
    checks=0
    # All interior extremizers must dominate both endpoints and a dense independent grid.
    for rate in (0.005,0.1,0.5,1.,3.,10.,50.,100.):
        t=optimum_poisson(rate)
        info=bit_information_poisson(rate,t)
        assert 0<t<1
        assert info>bit_information_poisson(rate,1.0)
        for j in range(1,401):
            assert info>=bit_information_poisson(rate,j/401)-1.e-12
            checks+=1
    for m in (1,2,3,4,5,10,20,80,100,500):
        t=optimum_fixed(m)
        info=bit_information_fixed(m,t)
        assert 0<t<1
        for j in range(1,401):
            assert info>=bit_information_fixed(m,j/401)-1.e-12
            checks+=1
    # Large-intensity limit constants and exact count-sensor baselines.
    root=bisect(lambda x:2*(-math.expm1(-x))-x,1.,1.999)
    assert abs(root-1.59362426004004)<1.e-11
    assert abs(3*root*(2-root)-1.9428307136757446)<1.e-11
    assert abs(10000*optimum_poisson(10000)-root)<0.003
    assert abs(10000*optimum_fixed(10000)-root)<0.001
    checks+=4
    assert abs(optimum_fixed(1)-0.5)<1.e-10
    checks+=1
    for m in (1,2,5,10,100):
        prev=optimum_fixed(m)
        following=optimum_fixed(m+1)
        assert following<prev
        checks+=1
    for rate in (0.1,1,10):
        assert optimum_poisson(2*rate)<optimum_poisson(rate)
        checks+=1
    # Independent simulation of Poisson and fixed-count event times.
    rng=random.Random(6743307)
    trials=120000
    for m in (1,3,8):
        t=optimum_fixed(m)
        js=[]; ys=[]
        for _ in range(trials):
            arrivals=[rng.random() for _ in range(m)]
            js.append(sum(1-u for u in arrivals))
            ys.append(int(min(arrivals)<=t))
        theoretical=bit_information_fixed(m,t)
        experimental=empirical_information(js,ys)
        assert abs(experimental-theoretical)/theoretical<0.05, (m,experimental,theoretical)
        checks+=1
    for rate in (0.75,2.5,5.0):
        t=optimum_poisson(rate)
        js=[];ys=[]
        for _ in range(trials):
            n=pois_sample(rng,rate)
            arrivals=[rng.random() for _ in range(n)]
            js.append(sum(1-u for u in arrivals))
            ys.append(int(any(u<=t for u in arrivals)))
        theoretical=bit_information_poisson(rate,t)
        experimental=empirical_information(js,ys)
        assert abs(experimental-theoretical)/theoretical<0.05, (rate,experimental,theoretical)
        checks+=1
    print(f'PASS {checks} independent analytic-grid, asymptotic, monotonicity and simulation checks.')

if __name__=='__main__':
    run()
