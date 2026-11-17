#!/usr/bin/env python3
"""Exact stationary identities and finite numerical checks of a critical contagion map."""
import math
import sympy as sp
import mpmath as mp
mp.mp.dps=55
m,B,p,k,d,g,a=sp.symbols('m B p k d g a',positive=True)
e=1-d
P=1-e*sp.exp(-B*a)
q=B*a*P/(m+B*a)
c=1+k*g/d
s0=(1-c*a)*(m+B*a)/(m+(2-p)*B*a)
z=(1-p)*B*a*(1-c*a)/(m+(2-p)*B*a)
w=k*g*a/d
H=B*P*(B*a+p*m)*(1-c*a)/((m+B*a)*(m+(2-p)*B*a))
assert sp.simplify(z-(1-p)*s0*q-z*(1-P))==0
assert sp.simplify(w-e*w-k*g*a)==0
assert sp.simplify(p*s0*q+z*q-k*a-a*(H-k))==0
B0=k*m/(p*d)
R=(d-m*e)/d**2
Q=1-(2+d*R)*p+(1-g-d/k)*p**2
assert sp.simplify(H.subs(a,0).subs(B,B0)-k)==0
assert sp.simplify(sp.diff(H,a).subs(a,0).subs(B,B0)-k*k*Q/(d*p**2))==0

def constants(nu,tau):
    nu=mp.mpf(nu); tau=mp.mpf(tau); m=nu*tau
    d=-mp.expm1(-m);e=1-d; k=-mp.expm1(-(1+nu)*tau);g=1/(1+nu)
    R=(d-m*e)/d**2; q2=1-g-d/k
    lo=mp.mpf('0');hi=mp.mpf('.5')
    for _ in range(190):
        p=(lo+hi)/2
        if 1-(2+d*R)*p+q2*p*p>0:lo=p
        else:hi=p
    p=(lo+hi)/2;B=k*m/(p*d); c=1+k*g/d
    C=k/2*(c*c+B*B*e/d**2+B*B/m**2*(1/p**2-1-(2-p)**2))
    return nu,tau,m,d,k,g,p,B,C

def Hvalue(x,nu,tau,p,B):
    m=nu*tau;d=-mp.expm1(-m);k=-mp.expm1(-(1+nu)*tau);g=1/(1+nu)
    c=1+k*g/d
    return B*(-mp.expm1(-m-B*x))*(B*x+p*m)*(1-c*x)/((m+B*x)*(m+(2-p)*B*x))

cases=[('.005','5.5'),('.5','1'),('1',str(mp.log(2))),('1','10'),('10','.1')]
for nu0,tau0 in cases:
    nu,tau,m,d,k,g,p,B,C=constants(nu0,tau0)
    assert 0<p<mp.mpf('.5') and C>0
    hd=mp.diff(lambda x:Hvalue(x,nu,tau,p,B),mp.mpf('0'),2)
    assert mp.almosteq(-hd/2,C,rel_eps=mp.mpf('1e-38'))
    # Independent cubic coefficient from center-manifold degree-2 invariance.
    e=mp.exp(-m);q1=B*d/m;q2=B*B*(m*e-d)/m**2
    q3=B**3*(d-m*e-m*m*e/2)/m**3
    alpha=(1-p)*q1/d;omega=k*g/d
    z2=((1-p)*(q2-q1*(alpha+1+omega))-alpha*B*e)/d
    center_cubic=p*q3+((1-p)*alpha-p*(1+omega))*q2+(1-p)*z2*q1
    assert mp.almosteq(center_cubic,-C,rel_eps=mp.mpf('1e-38'))
    eta=mp.mpf('1e-8'); approx=mp.sqrt(k*eta/C)
    root=mp.findroot(lambda x:Hvalue(x,nu,tau,p,B*(1+eta))-k,(approx*mp.mpf('.96'),approx*mp.mpf('1.04')))
    assert root>0 and abs(root/approx-1)<mp.mpf('.03')

def iterate_clock(nu,tau,iterations=160000):
    nu,tau,m,d,k,g,p,B,C=constants(nu,tau)
    nu=float(nu);tau=float(tau);m=float(m);d=float(d);k=float(k);g=float(g);p=float(p);B=float(B);C=float(C)
    z=0.;a=.01;w=0.;e=1-d
    for j in range(iterations):
        pp=-math.expm1(-m-B*a)
        q=(B*a/(m+B*a))*pp
        sn=1-z-a-w
        z,a,w=(1-p)*sn*q+z*(1-pp),p*sn*q+z*q+(1-k)*a,e*w+k*g*a
    measured=iterations*a*a;target=1/(2*C)
    assert abs(measured/target-1)<.03,(measured,target)
for nu,tau in [('1',str(mp.log(2))),('.5','1')]:
    iterate_clock(nu,tau)
print('VERIFY_OK cubic_degeneracy=5 stationary_identity=3 critical_relaxation=2')
