#!/usr/bin/env python3
"""Finite consistency checks for random-clock first-passage identities.

Uses only Python 3 standard library.  Finite computations do not prove
an infinite-time or regular-variation assertion.
"""
import math

checks = 0

def close(a,b,tol=3e-10):
    global checks
    checks += 1
    assert abs(a-b) < tol, (a,b,abs(a-b))

def bessel_I(n,a):
    n=abs(n)
    term=(a/2)**n / math.factorial(n)
    total=term
    for j in range(1,100):
        term *= a*a/(4*j*(j+n))
        total += term
        if term < 1e-17*max(1.0,total):
            break
    return total

def h_bessel(x,a):
    return math.exp(-a)*sum(bessel_I(j,a) for j in range(1-x,x+1))

def h_discrete(x,n):
    s=0
    for y in range(1,x+n+1):
        k1=n+y-x
        k2=n+y+x
        t1=math.comb(n,k1//2) if k1%2==0 and 0<=k1//2<=n else 0
        t2=math.comb(n,k2//2) if k2%2==0 and 0<=k2//2<=n else 0
        s+=t1-t2
    return s/(2**n)

def h_poisson(x,a):
    term=math.exp(-a)
    total=term*h_discrete(x,0)
    for n in range(1,85):
        term *= a/n
        total += term*h_discrete(x,n)
    return total

def simpson(f,lo,hi,n=4000):
    assert n%2==0
    h=(hi-lo)/n
    sm=f(lo)+f(hi)
    for j in range(1,n):
        sm+=(4 if j%2 else 2)*f(lo+j*h)
    return h*sm/3

for x in (1,2,3,6):
    for a in (0.0,0.02,0.2,0.9,2.0,4.0,8.0):
        h=h_bessel(x,a)
        close(h,h_poisson(x,a),tol=5e-12)
        close(h>=h_bessel(1,a)-1e-13,True,tol=0.1)
        close(h<=2*x*h_bessel(1,a)+1e-13,True,tol=0.1)

for a in (0.0,0.1,1.2,3.1,8.0):
    spectral=simpson(lambda th:math.exp(-a*(1-math.cos(th)))*(1+math.cos(th)),0,math.pi)/math.pi
    close(spectral,h_bessel(1,a))

tau=0.6
phi=lambda s:(math.exp(-s)+math.exp(-3*s))/2

def direct_survival(m):
    return sum(math.comb(m,k)*h_bessel(1,tau*(m+2*k))/2**m for k in range(m+1))

def spectral_survival(m):
    return simpson(lambda th:(1+math.cos(th))*phi(tau*(1-math.cos(th)))**m,0,math.pi)/math.pi

for m in (0,1,2,3,4,8,12):
    close(direct_survival(m),spectral_survival(m))

for M in (0,1,2,4,10):
    summed=sum(direct_survival(m) for m in range(M+1))
    def kernel(th):
        z=phi(tau*(1-math.cos(th)))
        v=M+1 if abs(1-z)<1e-14 else (1-z**(M+1))/(1-z)
        return (1+math.cos(th))*v
    close(summed,simpson(kernel,0,math.pi)/math.pi)

print('PASS:',checks,'finite deterministic consistency assertions')
