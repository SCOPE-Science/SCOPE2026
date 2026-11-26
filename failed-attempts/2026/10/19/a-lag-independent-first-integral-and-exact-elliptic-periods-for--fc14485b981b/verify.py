"""Reproduce finite checks for a four-cycle phase-oscillator theorem.

Run: python3 verify.py ; no third-party packages required.
Numerical checks supplement, and do not replace, the analytic proof.
"""
from math import sin, cos, pi, asin, sqrt, log, isfinite
from random import Random


def flow(theta, alpha):
    return tuple(sin(theta[(j-1)%4]-theta[j]+alpha)
                 + sin(theta[(j+1)%4]-theta[j]+alpha) for j in range(4))


def coords(z):
    return ((z[2]-z[0])/2, (z[3]-z[1])/2,
            (z[1]+z[3]-z[0]-z[2])/2)


def first_integral(z):
    u,v,phi=coords(z)
    return sin(u)*sin(v)/sin(phi)


def rhs_in_coords(u,v,phi,alpha):
    return (-2*cos(v)*cos(phi+alpha)*sin(u),
            -2*cos(u)*cos(alpha-phi)*sin(v),
            -4*cos(alpha)*cos(u)*cos(v)*sin(phi))


def rk4(x,alpha,h):
    a=flow(x,alpha)
    b=flow(tuple(x[i]+h*a[i]/2 for i in range(4)),alpha)
    c=flow(tuple(x[i]+h*b[i]/2 for i in range(4)),alpha)
    d=flow(tuple(x[i]+h*c[i] for i in range(4)),alpha)
    return tuple(x[i]+h*(a[i]+2*b[i]+2*c[i]+d[i])/6 for i in range(4))


def agm(a,b):
    for _ in range(100):
        aa=(a+b)/2; bb=sqrt(a*b)
        a,b=aa,bb
        if abs(a-b)<2e-15*a:
            return a
    raise RuntimeError('AGM failed to converge')


def exact_period(p,phi):
    return pi/(abs(sin(phi))*agm(1,abs(p)))


def check():
    rng=Random(260302135)
    # Analytic cancellation of the derivative of the claimed invariant.
    residuals=[]
    for _ in range(600):
        u=rng.uniform(-2.5,2.5); v=rng.uniform(-2.5,2.5)
        phi=rng.uniform(-2.5,2.5); alpha=rng.uniform(-1.5,1.5)
        if abs(sin(u)*sin(v)*sin(phi))<0.03: continue
        ud,vd,pd=rhs_in_coords(u,v,phi,alpha)
        dlog=cos(u)/sin(u)*ud+cos(v)/sin(v)*vd-cos(phi)/sin(phi)*pd
        residuals.append(abs(dlog))
    assert len(residuals)>350 and max(residuals)<5e-14, (len(residuals),max(residuals))
    # Check original ODE is exactly represented by the reduced ODE.
    for _ in range(400):
        z=tuple(rng.uniform(-2.8,2.8) for _ in range(4))
        alpha=rng.uniform(-2,2)
        f=flow(z,alpha)
        ud=(f[2]-f[0])/2; vd=(f[3]-f[1])/2
        pd=(f[1]+f[3]-f[0]-f[2])/2
        u,v,phi=coords(z); g=rhs_in_coords(u,v,phi,alpha)
        assert max(abs(a-b) for a,b in zip((ud,vd,pd),g))<4e-14
    # Exact return of all four phases, not merely their relative coordinates.
    max_return=0.; count=0
    for p in (0.08,0.2,0.4,0.63,0.85,0.96):
        for phi in (-1.8,-0.9,0.5,1.2):
            u=asin(sqrt(p)); v=u
            z=(-u,phi-v,u,phi+v)
            T=exact_period(p,phi)
            N=4000; h=T/N
            x=z
            for _ in range(N): x=rk4(x,pi/2,h)
            err=max(abs((x[i]-z[i]+pi)%(2*pi)-pi) for i in range(4))
            max_return=max(max_return,err); count+=1
    assert max_return<1e-7,(count,max_return)
    # Period decreases strictly with |p| and has the correct two endpoint limits.
    phi=0.84
    assert all(exact_period(0.1+0.08*i,phi)>exact_period(0.1+0.08*(i+1),phi) for i in range(10))
    near_center=exact_period(1-1e-8,phi)*abs(sin(phi))/pi
    assert abs(near_center-1)<1e-7
    p=1e-7
    log_ratio=exact_period(p,phi)*abs(sin(phi))/(2*log(4/p))
    assert abs(log_ratio-1)<3e-9,(log_ratio,near_center)
    print('PASS: %d first-integral derivative tests, 400 reduction tests, %d full-phase period tests; maximum return error %.3g.'%
          (len(residuals),count,max_return))
    print('PASS: strict sampled period monotonicity and both endpoint asymptotics.')

if __name__=='__main__':
    check()
