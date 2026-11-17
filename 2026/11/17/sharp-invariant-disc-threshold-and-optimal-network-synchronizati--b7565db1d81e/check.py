#!/usr/bin/env python3
"""Self-contained finite numerical corroboration for a holomorphic tanh network theorem.
This is a finite calculation, not a proof of any universal statement.
"""
import math, cmath

alpha=1.0
beta=0.35
kappa=1.2
R=0.7
N=6
c=math.tan(R)/R
delta=alpha-beta*c
lam2=1.0
mu=alpha-beta+kappa*lam2
C=math.exp(beta*math.tan(R)**2/(2*delta))
assert delta>0
print('R=%.6f  tan(R)/R=%.12f delta=%.12f' %(R,c,delta))
print('lambda_2=%.1f  optimal_exponent=%.12f  prefactor=%.12f' %(lam2,mu,C))
assert abs((alpha-beta+kappa*lam2)-1.85)<1e-12
# Sharp boundary radial derivative at z = iR; equality exactly from tanh(iR)=i tan(R).
assert abs((1j*R).conjugate()*cmath.tanh(1j*R) - R*math.tan(R))<1e-12
# Supremum of Re sech^2 on closed disk is attained at z=iR.
assert abs((1/(cmath.cosh(1j*R)**2)).real-(1/math.cos(R)**2))<1e-12
# Midpoint RK4 for diffusive ring, start with Fiedler-shaped real data.
def f(z):
    return [-alpha*z[i]+beta*cmath.tanh(z[i])-kappa*(2*z[i]-z[(i+1)%N]-z[(i-1)%N]) for i in range(N)]
def add(z,d,h): return [zi+h*di for zi,di in zip(z,d)]
def step(z,h):
    k1=f(z);k2=f(add(z,k1,h/2));k3=f(add(z,k2,h/2));k4=f(add(z,k3,h))
    return [zi+h*(a+2*b+2*c+d)/6 for zi,a,b,c,d in zip(z,k1,k2,k3,k4)]
def disagreement(z):
    zm=sum(z)/N
    return math.sqrt(sum(abs(a-zm)**2 for a in z))
z=[0.16*math.cos(2*math.pi*i/N)+0.03j*math.sin(4*math.pi*i/N) for i in range(N)]
w0=disagreement(z)
h=0.002
for i in range(10001):
    t=i*h
    if i%2500==0:
        w=disagreement(z)
        ratio=(w/w0)*math.exp(mu*t)
        assert ratio <= C*(1+3e-7), (t,ratio,C)
        assert max(abs(zi) for zi in z)<=R*math.exp(-delta*t)+1e-10
        print('t=%.2f  e^(mu*t)*w(t)/w(0)=%.9f  bound=%.9f'%(t,ratio,C))
    if i<10000: z=step(z,h)
print('VERIFY_OK radial_boundary=1 derivative_supremum=1 ring_integrations=10000 upper_bounds=5')
