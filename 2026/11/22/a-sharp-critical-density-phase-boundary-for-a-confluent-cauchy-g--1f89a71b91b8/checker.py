#!/usr/bin/env python3
"""Finite consistency checks for a critical-lattice double-pole Cauchy Gabor theorem.
Only standard-library modules are required. Finite checks supplement, not replace, proof.
"""
import cmath
import math

PI = math.pi

def cot(z):
    return cmath.cos(z) / cmath.sin(z)

def zak(x, w, a, lam):
    z = x + 1j*a
    c = cot(PI*z)
    z1 = PI*cmath.exp(1j*PI*z*(2*w-1))/cmath.sin(PI*z)
    return z1*(1 + PI*lam*(c-1j*(2*w-1)))

def threshold(a):
    return math.sqrt(math.expm1(4*PI*a))/(2*PI)

def boundary_x(a):
    lo,hi = .5,1.
    for j in range(75):
        mid = (lo+hi)/2
        if cot(PI*(mid+1j*a)).imag > -1: lo=mid
        else: hi=mid
    return (lo+hi)/2

def bisect_x(a, lam):
    xstar=boundary_x(a)
    goal=-1/(PI*lam)
    lo,hi=.5,xstar
    for j in range(75):
        mid=(lo+hi)/2
        if cot(PI*(mid+1j*a)).real > goal: lo=mid
        else: hi=mid
    return (lo+hi)/2

def min_boundary(a, lam):
    xstar=boundary_x(a)
    lo=max(.5,xstar-.03);hi=min(1,xstar+.03)
    phi=(math.sqrt(5)-1)/2
    u=hi-phi*(hi-lo);v=lo+phi*(hi-lo)
    for _ in range(130):
        if abs(zak(u,0,a,lam))**2 < abs(zak(v,0,a,lam))**2:
            hi=v;v=u;u=hi-phi*(hi-lo)
        else:
            lo=u;u=v;v=lo+phi*(hi-lo)
    x=(hi+lo)/2
    return abs(zak(x,0,a,lam))**2

def test():
    n=0
    for a in [.12,.3,.6,1.]:
        lc=threshold(a)
        C=1/math.tanh(2*PI*a)
        R=1/math.sinh(2*PI*a)
        M=1/(PI*lc)
        assert abs(M*M - 2*(C-1)) < 1e-10; n+=1
        for x in [j/29 for j in range(30)]:
            u=cot(PI*(x+1j*a))
            assert abs(u.real*u.real+(u.imag+C)**2-R**2)<1e-8; n+=1
        xs=boundary_x(a)
        u=cot(PI*(xs+1j*a))
        assert abs(u.imag+1)<1e-10 and abs(u.real+M)<1e-9; n+=1
        assert abs(zak(xs,0,a,lc))<1e-9; n+=1
        for fac in [1.01,1.1,1.4,4.]:
            lam=lc*fac
            x=bisect_x(a,lam)
            y=cot(PI*(x+1j*a)).imag
            w=(1+y)/2
            assert 0<w<.5; n+=1
            assert abs(zak(x,w,a,lam))<1e-8; n+=1
        for ratio in [1e-2,1e-3,3e-4]:
            lam=lc*(1-ratio)
            measured=min_boundary(a,lam)
            expected=4*PI*PI*ratio*ratio
            assert abs(measured/expected-1)<.025, (a,ratio,measured,expected); n+=1
        for x,w,lam in [(.23,.31,.3*lc),(.66,.41,.6*lc),(.34,.72,1.3*lc)]:
            exact=zak(x,w,a,lam)
            z=x+1j*a
            N=10000
            truncated=sum((1/(z+k)+lam/(z+k)**2)*cmath.exp(-2j*PI*k*w)
                          for k in range(-N,N+1))
            assert abs(exact-truncated)<.0002, (a,x,w,exact,truncated);n+=1
    print('PASS',n,'finite formula/circle/root/onset/truncation checks')
    print('Scope: standard-library finite numeric diagnostics; no infinite theorem is inferred.')

if __name__ == '__main__':
    test()
