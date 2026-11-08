"""Independent numerical checks of a symmetric two-choice activation map.

Reproducible with Python 3 standard library: python CHECK.py
The tests are finite sanity checks, not substitutes for the analytic proof.
"""
import math
import random


def h(u, a):
    return u**a - (1-u)**a


def inverse_h_clipped(y, a):
    if y <= -1:
        return 0.0
    if y >= 1:
        return 1.0
    low, high = 0.0, 1.0
    for _ in range(70):
        middle = (low + high)/2
        if h(middle, a) < y:
            low = middle
        else:
            high = middle
    return (low+high)/2


def step(p, q, lam, gamma):
    ua, ub = p+gamma*q, q+gamma*p
    if ua**lam + ub**lam < 1:
        return ua**lam, ub**lam
    u = inverse_h_clipped(ua-ub, 1/lam)
    return u, 1-u


def scalar_step(z, a, c):
    if c*z >= 1:
        return 1.0
    return 2*inverse_h_clipped(c*z, a)-1


def H(z,a):
    return h((1+z)/2,a)


def critical(a,c):
    lo, hi = 1e-8, 1.0
    for _ in range(75):
        m=(lo+hi)/2
        if H(m,a)/m > c:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def test():
    lam=2/3
    a=1/lam
    gamma=41/20
    c=gamma-1
    assert 1 < c < a*2**(1-a)
    s=(21+math.sqrt(41))/20
    zstar=s*math.sqrt(2-s*s)
    z_bisect=critical(a,c)
    assert abs(zstar-z_bisect)<2e-12
    assert abs(H(zstar,a)-c*zstar)<3e-15
    assert 0 < zstar < 1/c < 1
    L=c/((a/2)*(((1+zstar)/2)**(a-1)+((1-zstar)/2)**(a-1)))
    assert L>1

    # Check microscopic choice integration (all agents uniformly distributed by u)
    # against two independent formula implementations.
    rng=random.Random(71943)
    for j in range(160):
        p=rng.random()
        q=(1-p)*rng.random()
        x,y=step(p,q,lam,gamma)
        ua,ub=p+gamma*q,q+gamma*p
        n=10001
        mass_a=mass_b=0
        for k in range(n):
            u=(k+0.5)/n
            ea=ua>=u**a
            eb=ub>=(1-u)**a
            if ea and not eb:
                mass_a+=1
            elif eb and not ea:
                mass_b+=1
            elif ea and eb:
                mass_a+=int(ua-u**a >= ub-(1-u)**a)
                mass_b+=int(ua-u**a < ub-(1-u)**a)
        assert abs(x-mass_a/n)<1.1/n
        assert abs(y-mass_b/n)<1.1/n
        assert -1e-14<=x<=1+1e-14 and -1e-14<=y<=1+1e-14
        assert x+y<=1+1e-14

    # Global finite-time full activation and sharp basin decision from first full iterate.
    for j in range(400):
        p=rng.random()
        q=(1-p)*rng.random()
        if j%7==0:
            scale=10**(-1-7*rng.random())
            p*=scale; q*=scale
        initial_sum=p+q
        bound=math.ceil(math.log2(1/initial_sum))
        t=0
        while abs(p+q-1)>1e-12:
            p,q=step(p,q,lam,gamma)
            t+=1
            assert t<=bound
        z=abs(p-q)
        for k in range(20):
            nxt=step(p,q,lam,gamma)
            zz=abs(nxt[0]-nxt[1])
            assert abs(zz-scalar_step(z,a,c))<2e-12
            if z<zstar-1e-9:
                assert zz<z
            if z>zstar+1e-9 and z<1:
                assert zz>z
            p,q=nxt; z=zz

    # Sharp global dynamics on saturated manifold, with long transient cases.
    for z0 in (0.,0.1,0.3,zstar-0.001,zstar+0.001,0.7,0.92,1.0):
        z=z0
        for _ in range(10000):
            z=scalar_step(z,a,c)
            if z==1.0:
                break
        if z0<zstar:
            assert z<1e-8, (z0,z)
        elif z0>zstar:
            assert z==1, (z0,z)
    # Same committed A:B ratio gives different basins at different turnout.
    p1,q1=4/5,1/5
    p2,q2=2/5,1/10
    assert abs(p1-q1)>zstar
    pp,qq=step(p2,q2,lam,gamma)
    assert abs(pp+qq-1)<1e-14 and abs(pp-qq)<zstar
    assert abs((p2+gamma*q2)-(q2+gamma*p2)+63/200)<1e-14

    # Under-mobilized relative imbalance contracts by k=(gamma-1)/(gamma+1).
    factor=(gamma-1)/(gamma+1)
    for j in range(100):
        p=rng.random()/100
        q=rng.random()/100
        up=p+gamma*q; uq=q+gamma*p
        assert up**lam+uq**lam<1
        x,y=step(p,q,lam,gamma)
        old=abs(p-q)/(p+q)
        new=abs(x-y)/(x+y)
        assert new <= factor*old+1e-14

    # Distinct orbit counts and near separatrix escape scaling.
    def first_full(z):
        t=0
        while z<1 and t<100000:
            z=scalar_step(z,a,c);t+=1
        return t
    ts=[first_full(zstar+10**(-k)) for k in (3,4,5,6)]
    assert ts==sorted(ts),ts
    print('PASS: microscopic choice integration, 160 quadrature samples,')
    print('400 random finite-activation and basin tests, saturation, exact radical cutoff.')
    print('lambda, gamma=',lam,gamma)
    print('zstar, share threshold, unstable derivative=',zstar,(1+zstar)/2,L)
    print('escape steps for 1e-3..1e-6 beyond threshold=',ts)


if __name__=='__main__':
    test()
