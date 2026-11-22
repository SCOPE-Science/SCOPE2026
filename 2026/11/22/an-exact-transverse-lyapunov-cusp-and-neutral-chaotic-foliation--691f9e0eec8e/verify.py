"""Independent finite diagnostics for the exact chaotic-diagonal spectral theorem.

Uses no optional dependencies. Finite checks supplement the analytic proof.
"""
import math

N = 65536
checks = 0

def close(x, y, eps=2e-12):
    global checks
    assert abs(x-y) <= eps * max(1.0, abs(x), abs(y)), (x,y)
    checks += 1

def F(x, a):
    return tuple(x[i]*(4.0-3.0*(x[i]+a*(sum(x)-x[i]))) for i in range(3))

def exponent(a):
    k=(2.0+a)/(1.0+2.0*a)
    if a < 1.0:
        return math.log(k)
    if a == 1.0:
        return 0.0
    return 2.0*math.log1p(math.sqrt(1.0-k))

for a in (0.1,0.4,0.8,1.0,1.002,1.1,2.0,7.0):
    S=1.0+2.0*a
    k=(2.0+a)/S
    for u in (0.033,0.19,0.401,0.77,0.93):
        t=4.0*u/(3.0*S)
        x=(t,t,t)
        fx=F(x,a)
        close(fx[0],4.0*(4.0*u*(1.0-u))/(3.0*S))
        close(fx[1],fx[0])
        close(fx[2],fx[0])
        d=4.0-3.0*(2.0+2.0*a)*t
        o=-3.0*a*t
        close(d+2.0*o,4.0*(1.0-2.0*u))
        close(d-o,4.0*(1.0-k*u))
        for h in (0,1,2):
            z=list(x)
            eps=1e-7
            z[h]+=eps
            num=(F(z,a)[h]-fx[h])/eps
            assert abs(num-d)<4e-6
            checks+=1
    # Chebyshev arcsine midpoint quadrature for the integrable log singularity.
    # A true integral's value is established separately by Jensen's formula.
    s=0.0
    for j in range(N):
        u=(1.0-math.cos(math.pi*(j+0.5)/N))/2.0
        s+=math.log(abs(4.0*(1.0-k*u)))
    assert abs(s/N-exponent(a))<3e-4, (a,s/N,exponent(a))
    checks+=1

for delta in (1e-5,1e-7):
    left=exponent(1.0-delta)/delta
    right=exponent(1.0+delta)/math.sqrt(delta)
    assert abs(left-1.0/3.0)<0.0001, left
    assert abs(right-2.0/math.sqrt(3.0))<0.006, right
    checks+=2

for p in ((0.2,0.3,0.5), (0.06,0.76,0.18), (1/3,1/3,1/3)):
    u=0.13751235
    for _ in range(24):
        x=tuple(4.0*u*pi/3.0 for pi in p)
        y=F(x,1.0)
        v=4.0*u*(1.0-u)
        for i in range(3):
            close(y[i],4.0*v*p[i]/3.0)
        if sum(y)>0:
            for i in range(3):
                close(y[i]/sum(y),p[i])
        u=v

print('PASS',checks,'finite recurrence/Jacobian/quadrature/cusp/ray checks')
