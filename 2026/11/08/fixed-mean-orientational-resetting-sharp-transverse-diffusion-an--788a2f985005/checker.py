#!/usr/bin/env python3
"""Deterministic checks of closed cycle integrals and protocol boundaries.
Requires Python >=3.9 standard library only. Numerical checks do not replace proof.
"""
import math, random

D = 1.0
V = 1.0
MU = 1.0

def h(t, d):
    z=d*t
    return t/d + 4*math.expm1(-z)/(3*d*d)-math.expm1(-4*z)/(12*d*d)

def k(t, d):
    z=d*t
    return t/d + 2*math.expm1(-z)/(3*d*d)+math.expm1(-4*z)/(12*d*d)

def a(t,d): return -math.expm1(-d*t)/d

def simpson(fn, upper, n=1200):
    step=upper/n
    return step/3*(fn(0)+fn(upper)+4*sum(fn(step*j) for j in range(1,n,2))+2*sum(fn(step*j) for j in range(2,n,2)))

def independent_cycle_moments(t,d):
    # Integrate E[sin theta_s sin theta_t] and E[cos theta_s cos theta_t]
    # for 0 < s < t using the exact Brownian Fourier covariance kernels.
    f_common=lambda u: (1-math.exp(-d*u))/d
    f_sum=lambda u: math.exp(-d*u)*(1-math.exp(-3*d*u))/(3*d)
    return (simpson(lambda u:f_common(u)-f_sum(u),t),
            simpson(lambda u:f_common(u)+f_sum(u),t))

def protocol(law, d=1.0, v=1.0, diff=0.0):
    mu=sum(p*t for p,t in law)
    a1=sum(p*a(t,d) for p,t in law)
    xsq=sum(p*k(t,d) for p,t in law)*v*v
    ysq=sum(p*h(t,d) for p,t in law)*v*v
    xt=sum(p*t*a(t,d) for p,t in law)*v
    t2=sum(p*t*t for p,t in law)
    u=v*a1/mu
    return (u, diff+(xsq-2*u*xt+u*u*t2)/(2*mu),
            diff+ysq/(2*mu))

def fixed_mean_two_point(low,high,mu):
    p=(mu-low)/(high-low)
    assert 0<p<1
    return [(1-p,low),(p,high)]

count=0
rng=random.Random(409581)
for j in range(150):
    t=0.05+5*rng.random(); d=0.1+3*rng.random()
    hy,kx=independent_cycle_moments(t,d)
    assert abs(hy-h(t,d))<1.e-8*max(1,hy)
    assert abs(kx-k(t,d))<1.e-8*max(1,kx)
    count+=2
for j in range(250):
    d=0.1+3*rng.random();mu=0.1+4*rng.random();v=0.2+3*rng.random(); diff=rng.random()
    det=protocol([(1,mu)],d,v,diff)
    x=math.exp(-d*mu)
    predicted= -v*v*(1-x)**3*(x+3)/(12*mu*d*d)
    assert abs(det[1]-det[2]-predicted)<1.e-9*max(1,abs(predicted))
    low=mu*(.01+.97*rng.random());high=mu*(1.1+10*rng.random())
    law=fixed_mean_two_point(low,high,mu)
    mixed=protocol(law,d,v,diff)
    assert mixed[2]>det[2]
    assert mixed[2]<diff+v*v/(2*d)
    assert math.isclose(sum(p*t for p,t in law),mu,rel_tol=1.e-12)
    count+=4
for j in range(150):
    d=.2+2*rng.random(); v=.2+3*rng.random(); rate=.2+2*rng.random();mu=1/rate
    # Poisson moment transform computed exactly, not approximated by quadrature.
    ph=rate/(rate+d);p4=rate/(rate+4*d);phd=-rate/(rate+d)**2
    u=v*(1-ph)/(d*mu)
    ex2=v*v*(mu/d-2*(1-ph)/(3*d*d)-(1-p4)/(12*d*d))
    ey2=v*v*(mu/d-4*(1-ph)/(3*d*d)+(1-p4)/(12*d*d))
    ext=v/d*(mu+phd)
    dx=(ex2-2*u*ext+u*u*2*mu*mu)/(2*mu)
    dy=ey2/(2*mu)
    published_x=v*v*d*d*(2*d+5*rate)/((d+rate)**3*(4*d+rate))
    published_y=2*v*v*d/((d+rate)*(4*d+rate))
    assert abs(dx-published_x)<1.e-10*max(1,abs(dx))
    assert abs(dy-published_y)<1.e-10*max(1,abs(dy))
    count+=2
# Strong anisotropy reversal with same mean.
det=protocol([(1,1.)]); assert det[1]<det[2];count+=1
long_vals=[]
for n in (16,81,256,1024,4096):
    p=n**(-1.5); b=float(n); a0=(1-p*b)/(1-p)
    law=[(1-p,a0),(p,b)]
    u,dx,dy=protocol(law)
    assert dx>dy
    assert dy<.5
    assert abs(sum(w*t for w,t in law)-1)<1.e-12
    long_vals.append((n,u,dx,dy))
    count+=3
assert all(long_vals[j+1][2]>long_vals[j][2] for j in range(len(long_vals)-1));count+=1
for n in (20,100,1000,5000):
    low=1/(n*n); high=float(n)
    law=fixed_mean_two_point(low,high,1.0)
    _,_,dy=protocol(law)
    assert dy>det[2] and dy<0.5
    count+=2
assert abs(protocol(fixed_mean_two_point(1e-8,100000.,1.))[2]-.5)<.00005
count+=1
print('PASS:',count,'assertion groups; independent numerical cycle integration, exact Poisson benchmark, fixed-mean bounds, anisotropy reversal')
print('deterministic mu=d=v=1: drift, Dx, Dy=',det)
print('rare-event protocols: n, drift, Dx, Dy=',long_vals)
