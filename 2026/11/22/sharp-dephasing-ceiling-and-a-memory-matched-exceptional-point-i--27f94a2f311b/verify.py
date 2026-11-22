"""Reproduce the spectral and finite-time recency-memory statements.

Usage: python3 verify.py. Requires only the Python standard library.
The RK4 integrator is independent of the closed spectral expression.
"""
import cmath
import math


def coefficients(r, gamma, omega):
    delta = cmath.sqrt((r+gamma)**2-omega**2+2j*omega*(r-gamma))
    return delta


def exact(r, gamma, omega, t):
    delta = coefficients(r,gamma,omega)
    mid = -(r+gamma+1j*omega)/2
    first = cmath.cosh(delta*t/2)
    if abs(delta) < 1e-10:
        second = t/2
    else:
        second = cmath.sinh(delta*t/2)/delta
    # initial v=(1,1), (A-mid I)v gives ((gamma-r-i*omega)/2, (gamma-r+i*omega)/2)?
    # A(1,1)=(-i*omega,0), so first entry (gamma+r-i*omega)/2.
    return cmath.exp(mid*t) * (first+(r+gamma-1j*omega)*second)


def rk4(r,gamma,omega,t,steps=9000):
    dt=t/steps
    f,h=1+0j,1+0j
    def rhs(x,y):
        return (-(r+1j*omega)*x+r*y, gamma*(x-y))
    for _ in range(steps):
        u1,v1=rhs(f,h)
        u2,v2=rhs(f+dt*u1/2,h+dt*v1/2)
        u3,v3=rhs(f+dt*u2/2,h+dt*v2/2)
        u4,v4=rhs(f+dt*u3,h+dt*v3)
        f+=dt*(u1+2*u2+2*u3+u4)/6
        h+=dt*(v1+2*v2+2*v3+v4)/6
    return f


def spectral_gap(r,gamma,omega):
    return (r+gamma-coefficients(r,gamma,omega).real)/2


if __name__=='__main__':
    count=0
    for r in [0.3,0.8,2.0]:
        for gamma in [0.2,0.5,0.8,1.4,2.0,3.5]:
            for omega in [0.1,0.6,1.5,3.1,5.0]:
                for t in [0.13,0.73,2.1]:
                    a=exact(r,gamma,omega,t)
                    b=rk4(r,gamma,omega,t,steps=900)
                    assert abs(a-b) < 5e-9, (r,gamma,omega,t,a,b)
                    count+=1
                gap=spectral_gap(r,gamma,omega)
                assert 0<gap<=r+1e-12, (r,gamma,omega,gap)
                if abs(gamma-r)>1e-10:
                    assert gap<r-1e-9
    print('ODE-vs-closed-form comparisons:',count)
    for r in (0.2,1.,2.):
        for omega in (0.4*r,1.1*r,1.95*r,2*r,2.7*r,5*r):
            g=spectral_gap(r,r,omega)
            assert abs(g-r)<1e-12 if omega>=2*r else g<r
            for t in (0.15,0.6,1.9,3.1):
                z=exact(r,r,omega,t)
                d=coefficients(r,r,omega)
                if abs(d)<1e-9:
                    analytic=-r*omega**2*t*t*math.exp(-2*r*t)
                else:
                    analytic=(-2*r*omega*omega*math.exp(-2*r*t)
                              * (cmath.cosh(d*t)-1)/(d*d)).real
                eps=1e-5
                derivative=(abs(exact(r,r,omega,t+eps))**2-abs(exact(r,r,omega,t-eps))**2)/(2*eps)
                assert abs(derivative-analytic) < 2e-8,(r,omega,t,derivative,analytic)
                assert analytic<0
                if abs(omega-2*r)<1e-12:
                    expected=math.exp(-2*r*t)*(1+2*r*t+2*r*r*t*t)
                    assert abs(abs(z)**2-expected)<1e-11
    print('Sharp rate/EP/CP-divisibility checks: passed')
    print('ALL CHECKS PASS')
