#!/usr/bin/env python3
"""Reproduce exact polynomial identities and numeric diagnostics for an
inhomogeneous two-direction velocity-jump process. Standard library only.
The analytic proof is supplied separately; finite tests are diagnostics.
"""
from fractions import Fraction as Q
from math import tanh, atanh, sqrt, log, exp, isclose

def add(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out

def scale(a,c):return [x*c for x in a]

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def deriv(a):return [i*a[i] for i in range(1,len(a))]

def poly(a,z):return sum(float(c)*z**i for i,c in enumerate(a))

checks=0

def ck(pred,msg):
    global checks
    assert pred,msg
    checks+=1

# z=tanh(u*x)^2, g=3u, v0=2,v1=1,gamma0=gamma1=1.
# Triple-angle relation: tanh(3y)/tanh(y)=(3+z)/(1+3z).
N=[Q(7),Q(5)]
V=mul([Q(1),Q(-1)],[Q(1),Q(3)])
W=add(mul(deriv(N),V),scale(mul(N,deriv(V)),Q(-1)))
ck(V==[Q(1),Q(2),Q(-3)],'denominator')
ck(W==[Q(-9),Q(42),Q(15)],'derivative numerator')
ck(W==scale(mul([Q(-1),Q(5)],[Q(3),Q(1)]),Q(3)),'factorization')
ck(Q(7)*Q(1)==Q(7),'origin U value')
ck(Q(8)/(Q(4,5)*Q(8,5))==Q(25,4),'minimum U')

for u in [Q(6),Q(25,4),Q(13,2),Q(7),Q(8),Q(10)]:
    P=add(scale(V,u),scale(N,Q(-1)))
    ck(P==[u-Q(7),Q(2)*u-Q(5),-Q(3)*u],f'polynomial for {u}')

P=add(scale(V,Q(13,2)),scale(N,Q(-1)))
ck(scale(P,Q(-2))==mul([Q(-1),Q(13)],[Q(-1),Q(3)]),'exact rational roots')
for z in [Q(1,13),Q(1,3)]:ck(sum(c*z**i for i,c in enumerate(P))==0,'root exact')
for z,sign in [(Q(1,100),-1),(Q(1,5),1),(Q(3,4),-1)]:
    v=sum(c*z**i for i,c in enumerate(P))
    ck(sign*v>0,'mode slope signs')

def log_density_ratio(u,x):
    z=tanh(u*x)**2
    return (log(4/(4-z)) +log(1-z)/u
            -4*log(1+3*z)/(13*u)-9*log((4-z)/4)/(13*u))

def log_derivative(u,x):
    t=tanh(u*x)
    return 2/(4-t*t)*(u*t*(1-t*t)-t-2*tanh(3*u*x))

def simpson(fun,a,b,Nsteps=4000):
    assert Nsteps%2==0
    h=(b-a)/Nsteps
    return h/3*(fun(a)+fun(b)+4*sum(fun(a+i*h) for i in range(1,Nsteps,2))
                +2*sum(fun(a+i*h) for i in range(2,Nsteps,2)))

u=6.5
x_min=atanh(1/sqrt(13))/u
x_max=atanh(1/sqrt(3))/u
ck(0<x_min<x_max,'extremum order')
for x in [x_min/2,(x_min+x_max)/2,x_max*1.3]:
    ck((log_derivative(u,x)>0)==(x_min<x<x_max),'numerical slope')
for x in [0.01,0.035,0.07,0.13,0.4]:
    h=1e-6
    finite=(log_density_ratio(u,x+h)-log_density_ratio(u,x-h))/(2*h)
    ck(abs(finite-log_derivative(u,x))<2e-8,'differentiation check')
    integral=simpson(lambda t:log_derivative(u,t),0,x,4000)
    ck(abs(integral-log_density_ratio(u,x))<1e-10,'integration check')
ck(log_density_ratio(u,x_min)<0,'side minimum below central')
ck(log_density_ratio(u,x_max)>log_density_ratio(u,x_min),'side maximum above valley')
for uu in [5.0,6.0,6.25]:
    for x in [0.0001,0.005,0.03,0.07,0.13,0.4,1]:
        ck(log_derivative(uu,x)<1e-10,'unimodal regime')
for uu in [7.0,8.0,10.0]:
    ck(log_derivative(uu,0.01)>0,'bimodal origin is minimum')
    ck(log_derivative(uu,0.7)<0,'bimodal outer decay')

print('Exact and numeric diagnostic assertions passed:',checks)
print('At u=13/2, g=39/2: central maximum x=0;')
print('  minima x=+/- %.15f; side maxima x=+/- %.15f'%(x_min,x_max))
print('  p(x_min)/p(0)=%.15f; p(x_max)/p(0)=%.15f'%
      (exp(log_density_ratio(u,x_min)),exp(log_density_ratio(u,x_max))))
print('Thresholds: u_c=25/4; central curvature changes at u=7.')
