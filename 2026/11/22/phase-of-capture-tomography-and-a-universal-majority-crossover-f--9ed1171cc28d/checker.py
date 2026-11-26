"""Finite diagnostics for phase-resolved Brownian search and stochastic returns.

Use: python checker.py. Only Python standard library is needed.
The infinite-dimensional uniqueness and universal monotonicity are proved separately.
"""
import math
import random


def simpson(f, a=0., b=1., n=1200):
    assert n % 2 == 0
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3


def h_drift(y, c):
    return math.expm1(c*y)/math.expm1(c) if c else y


def odds(z,h,n=1200):
    return z*simpson(lambda y: math.sinh(z*(1-y))*h(y),n=n)


def matrix_nullvec(a):
    m = len(a)
    n = len(a[0])
    b = [row[:] for row in a]
    pivots = []
    k = 0
    for j in range(n):
        pivot = max(range(k,m),key=lambda i:abs(b[i][j])) if k<m else None
        if pivot is None or abs(b[pivot][j]) < 1e-12:
            continue
        b[k],b[pivot] = b[pivot],b[k]
        d=b[k][j]
        b[k]=[q/d for q in b[k]]
        for i in range(m):
            if i!=k:
                d=b[i][j]
                b[i]=[b[i][u]-d*b[k][u] for u in range(n)]
        pivots.append(j)
        k+=1
        if k==m:break
    free = next(j for j in range(n) if j not in pivots)
    x=[0.]*n
    x[free]=1.
    for i in reversed(range(len(pivots))):
        j=pivots[i]
        x[j]=-sum(b[i][l]*x[l] for l in range(j+1,n))
    return x


def draw_phase(z, h, rng):
    """Brownian killed at 1 and exponential observation: exact bridge max test."""
    r = z*z
    for _ in range(10000):
        t = rng.expovariate(r)
        x = rng.gauss(0,math.sqrt(2*t))
        p_hit = 1. if x >= 1 else math.exp(-(1-x)/t)
        if rng.random() < p_hit:
            return 0   # capture during exploration
        if 0<x<1 and rng.random() < h(x):
            return 1   # capture during return
    raise RuntimeError('Renewal attempts did not finish')


def main():
    checks=0
    for z in (0.07,0.17,0.5,1.,1.7,2.177318984965307,3.,5.3,7.):
        value=odds(z,lambda y:y)
        analytic=math.sinh(z)/z-1
        assert abs(value-analytic) < 2e-9*max(1,analytic)
        checks+=1
        # Search and return per-cycle probabilities are obtained independently.
        a=math.exp(-z)
        b=z*math.exp(-z)*simpson(lambda y:math.sinh(z*(1-y))*y)
        assert abs(b/a-value) < 2e-9*max(1,value)
        assert abs(b/(a+b)-(1-z/math.sinh(z))) < 2e-9
        checks+=2
    lo, hi = 2., 3.
    for _ in range(54):
        mid = (lo + hi)/2
        if math.sinh(mid) < 2*mid:
            lo = mid
        else:
            hi = mid
    zcrit = (lo + hi)/2
    assert abs(math.sinh(zcrit)-2*zcrit) < 1e-12
    checks+=1
    for c in (0.,0.4,1.7,3.,6.):
        h=lambda y,c=c:h_drift(y,c)
        zz=[0.03+i*0.07 for i in range(90)]
        values=[odds(z,h,n=240) for z in zz]
        assert all(a<b for a,b in zip(values,values[1:]))
        checks+=1
    for z in (0.3,1.0,2.0,3.0,4.5):
        assert odds(z,lambda y:h_drift(y,0.4)) > odds(z,lambda y:h_drift(y,1.7)) > odds(z,lambda y:h_drift(y,3.))
        checks+=1
    # Hausdorff moment coefficients of a neutral return splitting profile.
    for n in range(10):
        numerical=simpson(lambda y:(1-y)**(2*n+1)*y, n=4800)
        exact=1/((2*n+2)*(2*n+3))
        assert abs(numerical-exact) < 2e-12
        checks+=1
    # Exact finite-rate nonidentifiability: one polynomial null direction.
    zs=(0.4,1.1,2.3)
    A=[[z*simpson(lambda y,j=j,z=z:math.sinh(z*(1-y))*y*(1-y)*y**j,n=4000) for j in range(4)] for z in zs]
    coeff=matrix_nullvec(A)
    def poly(y):return y*(1-y)*sum(a*y**j for j,a in enumerate(coeff))
    eps=0.025/max(1,sum(abs(a) for a in coeff))
    base=lambda y:h_drift(y,2.0)
    hp=lambda y:base(y)+eps*poly(y)
    hm=lambda y:base(y)-eps*poly(y)
    for i in range(1,100):
        y=i/100
        assert 0<hp(y)<1 and 0<hm(y)<1
        delta=1e-5
        assert (hp(y+delta)-hp(y-delta))/(2*delta)>0.3
        assert (hm(y+delta)-hm(y-delta))/(2*delta)>0.3
        second_p=(hp(y+delta)-2*hp(y)+hp(y-delta))/delta**2
        second_m=(hm(y+delta)-2*hm(y)+hm(y-delta))/delta**2
        assert second_p>0.3 and second_m>0.3
    assert max(abs(hp(y)-hm(y)) for y in [i/100 for i in range(101)])>1e-8
    for z in zs:
        assert abs(odds(z,hp,n=4000)-odds(z,hm,n=4000))<1e-10
        checks+=1
    # Analytical b=-D h''/h' for constant-inward-drift returns.
    c=2.4
    for y in (0.15,0.38,0.76):
        h1=c*math.exp(c*y)/math.expm1(c)
        h2=c*c*math.exp(c*y)/math.expm1(c)
        assert abs(-h2/h1+c)<1e-14
        checks+=1
    # Event-clock Monte Carlo: sample killed Brownian endpoint by bridge reflection.
    rng=random.Random(260417)
    for z,c,number in ((1.2,0.,18000),(2.4,0.,18000),(2.5,1.5,18000)):
        h=lambda y,c=c:h_drift(y,c)
        samples=sum(draw_phase(z,h,rng) for _ in range(number))
        observed=samples/number
        predicted=odds(z,h)/(1+odds(z,h))
        sigma=math.sqrt(predicted*(1-predicted)/number)
        assert abs(observed-predicted)<6*sigma+0.008,(observed,predicted)
        checks+=1
    print(f'PASS: {checks} independent finite diagnostics (integrals, asymptotic coefficients, order, nullspace, drift, bridge Monte Carlo)')
    print(f'neutral-return capture-majority z = {zcrit:.12f}, r L^2/D = {zcrit**2:.12f}')

if __name__=='__main__':main()
