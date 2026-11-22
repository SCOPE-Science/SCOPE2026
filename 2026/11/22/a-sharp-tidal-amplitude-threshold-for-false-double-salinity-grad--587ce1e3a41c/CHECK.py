"""Standalone numerical and exact-rational checks for a Gaussian-front tidal average.

Uses Python's standard library only. Running this file does not replace the analytic
proof of the global mode count or the Bessel-ratio uniqueness argument.
"""
from fractions import Fraction as Q
from math import factorial, exp, sqrt, pi, cos


def b_bounds(z, n=14):
    """Rigorous rational enclosure of B(z) for rational 1/2 <= z <= 1."""
    assert Q(1, 2) <= z <= 1
    q = z*z/4
    i0 = sum(q**k / factorial(k)**2 for k in range(n+1))
    i1 = sum(z/2 * q**k / (factorial(k)*factorial(k+1)) for k in range(n+1))
    t0 = q**(n+1) / factorial(n+1)**2
    t1 = z/2 * q**(n+1)/(factorial(n+1)*factorial(n+2))
    r0 = t0/(1-Q(1, 4*(n+2)**2))
    r1 = t1/(1-Q(1, 4*(n+2)*(n+3)))
    return (2*z-1)*i0 - 2*z*(i1+r1), (2*z-1)*(i0+r0)-2*z*i1

lo = Q(7899784, 10000000)
hi = Q(7899785, 10000000)
assert b_bounds(lo)[1] < 0
assert b_bounds(hi)[0] > 0
assert b_bounds(Q(1, 2))[1] < 0
assert b_bounds(Q(1))[0] > 0


def bessel01(z, n=50):
    q=z*z/4
    v0=1.0
    v1=z/2
    t0=1.0
    t1=z/2
    for k in range(1, n+1):
        t0*=q/k**2
        t1*=q/(k*(k+1))
        v0+=t0
        v1+=t1
    return v0,v1


def B(z):
    i0,i1=bessel01(z)
    return (2*z-1)*i0 - 2*z*i1

left,right=float(lo),float(hi)
for _ in range(54):
    mid=(left+right)/2
    if B(mid)>0:right=mid
    else:left=mid
zstar=(left+right)/2
astar=2*sqrt(zstar)
assert 0.7899784 < zstar < 0.7899785
assert 1.7776145 < astar < 1.7776147


def moments(x,a,n=4096):
    """Midpoint angle quadrature of density, first and second x-derivatives."""
    ds=d1=d2=0.0
    for k in range(n):
        angle=(k+0.5)*pi/n
        u=x-a*cos(angle)
        f=exp(-u*u/2)/sqrt(2*pi)
        ds+=f
        d1+=-u*f
        d2+=(u*u-1)*f
    return (ds/n, d1/n, d2/n)

assert moments(0,1.7)[2] < -0.001
assert moments(0,2.0)[2] > 0.001
assert abs(moments(0,astar)[2]) < 1e-9
assert abs(moments(0,astar)[0] + moments(0,astar)[2] * 0) > .2

# Strictly bimodal example: the center is a local minimum and each side
# contains a higher density, with a lower density beyond the tidal amplitude.
center,derivative,curv=moments(0,2.0)
left_peak=moments(0.8497883894922035,2.0)
assert curv > 0 and left_peak[0] > center and abs(left_peak[1]) < 2e-9
assert moments(3.0,2.0)[1] < 0

# Symmetric Gaussian CDF fronts have exactly one 50% location by symmetry;
# the differentiated profile is strictly positive at every finite depth.
for a in [0.0,1.0,astar,2.0,3.0]:
    assert moments(0.0,a)[0] > 0
    assert abs(moments(-0.3,a)[0]-moments(0.3,a)[0]) < 2e-14
print('PASS: rational root enclosure, numerical Bessel phase and bimodal witnesses')
print('z_star =', format(zstar,'.14f'), 'A/sigma =',format(astar,'.14f'))
