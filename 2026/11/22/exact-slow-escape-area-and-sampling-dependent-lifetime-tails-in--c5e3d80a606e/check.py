"""Reproduce numerical diagnostics for the harmonic-cubic escape-time theorem.
Requires Python 3 with scipy. These computations support, not replace, the proof.
"""
from math import pi, sin, cos, sqrt, isfinite
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import beta

B = float(beta(0.5, 1.0/6.0))
K = B**3 / (27*pi)

def angular_lifetime(theta):
    c, s = cos(3*theta), abs(sin(3*theta))
    if s < 1e-13:
        return float('inf') if c < 0 else 1.0
    kernel = lambda u: (u*u+s*s)**(-2.0/3.0)
    if c < 0:
        return (B * s**(-1.0/3.0) - quad(kernel, -c, float('inf'), epsabs=1e-11)[0])/3.0
    return quad(kernel, c, float('inf'), epsabs=1e-11)[0]/3.0

def main():
    checks=0
    for k in range(1,141):
        x = 0.03 + k/37.0
        y = -2 + k/49.0
        dx,dy=x*x-y*y,-2*x*y
        u=x**3-3*x*y*y
        v=3*x*x*y-y**3
        du=(3*x*x-3*y*y)*dx-6*x*y*dy
        dv=(6*x*y)*dx+(3*x*x-3*y*y)*dy
        assert abs(du-3*(u*u+v*v)**(2/3)) < 1e-8*(1+abs(du))
        assert abs(dv)<1e-8*(1+abs(u))
        checks+=2
    assert angular_lifetime(0.0)==1.0
    assert angular_lifetime(pi/3)==float('inf')
    checks+=2
    for j in range(2,30):
        angle = pi*j/90
        eps=1e-5
        a = angular_lifetime(angle)
        ap=(angular_lifetime(angle+eps)-angular_lifetime(angle-eps))/(2*eps)
        assert abs(a*cos(3*angle)+ap*sin(3*angle)-1)<3e-3
        checks+=1
    c=B/(3**(4.0/3.0))
    for d in [0.0003,0.0001,0.00003]:
        estimated=angular_lifetime(pi/3-d)*d**(1/3)
        assert abs(estimated/c-1)<0.05
        checks+=1
    ea2=3/pi*quad(lambda th:angular_lifetime(th)**2,0,pi/3,
                  epsabs=1e-6, limit=180)[0]
    assert 4.4<ea2<4.7
    checks+=1
    for a in [50.,100.]:
        delta=brentq(lambda d:angular_lifetime(pi/3-d)-a, 1e-9, 0.3,
                     xtol=1e-13)
        tail=3*delta/pi
        assert abs((a**3*tail)/K-1)<0.20
        checks+=1
    print('PASS',checks,'checks','B=',B,'K=',K,'EA2=',ea2,
          'Gaussian-tail-constant/sigma^2=',ea2/2)
if __name__=='__main__':main()
