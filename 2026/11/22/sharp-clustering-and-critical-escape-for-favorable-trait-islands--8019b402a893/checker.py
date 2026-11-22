#!/usr/bin/env python3
"""Supplementary arithmetic checks for finite-island mutation-selection theorem.
Run: python3 checker.py (Python 3.9+, standard library only).
Analytic proof, not these finite tests, covers arbitrary finite island configurations.
"""
from fractions import Fraction
from math import sqrt, pi, atan, tan, cos, isclose


def top_eig(matrix):
    n = len(matrix)
    v = [1.0 / sqrt(n)] * n
    for _ in range(25000):
        z = [sum(a * b for a, b in zip(row, v)) for row in matrix]
        norm = sqrt(sum(a*a for a in z))
        vv = [a/norm for a in z]
        if max(abs(a-b) for a,b in zip(v,vv)) < 1e-14:
            v = vv
            break
        v = vv
    return sum(v[i] * sum(matrix[i][j] * v[j] for j in range(n)) for i in range(n))


def theta(k,s):
    assert k>=2
    b = (1+s)/(1-s)
    lo,hi=0.0,pi/k
    for _ in range(85):
        mid=(lo+hi)/2
        if k*mid+2*atan(b*tan(mid/2)) < pi:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def rho_block(k,s):
    if k==1:
        return 1.0
    th=theta(k,s)
    return (1-s*s)/(1+s*s-2*s*cos(th))


def green(t,p,q,j,i):
    discriminant=sqrt(1-4*p*q*t*t)
    plus=(1-discriminant)/(2*q*t)
    minus=(1-discriminant)/(2*p*t)
    return (plus**(j-i) if j>=i else minus**(i-j))/discriminant


def root_t_two(p,q,d,L):
    assert p>q>0 and isclose(p+q,1.0)
    def f(t):
        discr=sqrt(1-4*p*q*t*t)
        r=(1-discr)/(1+discr)
        return (1-d)*(1+r**(L/2))/discr-1
    assert f(1)>0
    low,high=0.0,1.0
    for _ in range(90):
        mid=(low+high)/2
        if f(mid)>0: high=mid
        else: low=mid
    return (high+low)/2


def check():
    for p in (0.55, 0.63, 0.75, 0.88):
        q=1-p
        s=sqrt(q/p)
        # Compare separate positive-matrix power iteration to the inverse-tridiagonal quantization formula.
        for k in range(1,14):
            K=[[s**abs(i-j) for j in range(k)] for i in range(k)]
            exact=rho_block(k,s)
            numeric=top_eig(K)
            assert abs(exact-numeric)<3e-10, (p,k,numeric,exact)
            dcrit=1-(p-q)/exact
            assert 0<dcrit<2*sqrt(p*q)+1e-10
            if k>1:
                assert dcrit > 2*q
        # The k^{-2} coefficient comes from theta = pi/k + O(k^{-2}).
        for k in (512,1024,2048):
            dcrit=1-(p-q)/rho_block(k,s)
            gap=k*k*(2*sqrt(p*q)-dcrit)
            assert abs(gap/(pi*pi*sqrt(p*q))-1)<0.11, (p,k,gap)
        # Verify the unit Green kernel recurrence at several sampled t, sites.
        for t in (.2,.4,.7,.95):
            for j in range(-3,4):
                for i in (-3,0,2):
                    g=green(t,p,q,j,i)
                    rhs=(int(j==i)+t*(p*green(t,p,q,j-1,i)+q*green(t,p,q,j+1,i)))
                    assert abs(g-rhs)<8e-12
    # Exact two-site rescue: p=3/4, q=1/4, mortality d=3/5.
    # At t=1 the two-site condition is 3^{-L/2}>1/4.
    assert Fraction(1,3)>Fraction(1,16)  # L=1, after squaring
    assert Fraction(1,3)>Fraction(1,4)   # L=2
    assert Fraction(1,27)<Fraction(1,16) # L=3
    p,q,d,L,lam=.75,.25,.6,1,2.0
    t=root_t_two(p,q,d,L)
    assert abs(t-0.9237604307034012)<1e-12
    assert 0<t<1<lam
    ratio=(p/q)**(L/2)
    w0=(1-t)/((1-d)*(1+ratio))
    wL=ratio*w0
    w=lambda j:(1-d)*(green(t,p,q,j,0)*w0+green(t,p,q,j,L)*wL)
    assert abs(w(0)-w0)<1e-12 and abs(w(L)-wL)<1e-12
    assert abs(sum(w(j) for j in range(-240,241))-1)<1e-10
    total=1-t/lam
    for j in range(-20,121):
        x=total*w(j)
        mortality=d if j in (0,L) else 1.0
        equilibrium=lam*(1-total)*(p*total*w(j-1)+q*total*w(j+1))-mortality*x
        assert abs(equilibrium)<2e-12
    # Check strict arrangement optimality at equal k and a nonconsecutive set.
    s=sqrt(q/p)
    close=[[s**abs(i-j) for j in range(4)] for i in range(4)]
    spread_sites=[0,1,3,5]
    wide=[[s**abs(i-j) for j in spread_sites] for i in spread_sites]
    assert top_eig(close)>top_eig(wide)
    print('PASS: Green recurrence, eigenvalue quantization, layout ordering, exact rescue, equilibrium residuals, large-block asymptotics')
    print('illustrative t*=%.15f, equilibrium mass=%.15f' % (t,total))

if __name__=='__main__': check()
