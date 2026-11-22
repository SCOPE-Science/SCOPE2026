#!/usr/bin/env python3
"""Independent algebraic and Laplace-transform checks for radial Brownian exit sensitivity.
Run: python CHECK.py  (requires sympy, mpmath).
"""
import sympy as s
import mpmath as m
D, x, rate = s.symbols('d x r', positive=True)
assertions=0

def verify(flag):
    global assertions
    assert bool(flag)
    assertions += 1

# Radial moment recurrence: Delta(x^j) = 2j(2j+d-2)x^(j-1).
def moments(nmax):
    us = [s.S.One]
    for n in range(1, nmax+1):
        pol = s.Poly(-n*us[-1], x)
        v = sum(c * x**(j+1) / (2*(j+1)*(2*(j+1)+D-2))
                for (j,),c in pol.terms())
        v = s.factor(v-v.subs(x,1))
        verify(v.subs(x,1)==0)
        L = s.expand(4*x*s.diff(v,x,2)+2*D*s.diff(v,x))
        verify(s.simplify(L+n*us[-1])==0)
        us.append(v)
    return us
us=moments(3)
m1,m2,m3=us[1:]
mean_grad=s.factor(m1*m1-m2/2)
var_grad=s.factor(-2*m1**3+3*m1*m2-s.Rational(2,3)*m3)
P=D**2*(1-x)**2+12*D*(1-x)-48*x*(x+1)
verify(s.simplify(mean_grad-(1-x)*(D-(D+4)*x)/(8*D**2*(D+2)))==0)
verify(s.simplify(var_grad-(1-x)*P/(24*D**3*(D+2)*(D+4)))==0)
q=D/(D+4)
verify(s.factor(P.subs(x,q))==-32*D**2/(D+4)**2)
verify(s.factor(P.subs(D,3).subs(x,s.Rational(5,13)))==0)
verify(s.factor(P.subs(D,4).subs(x,s.sqrt(6)-2))==0)
verify(s.factor(s.diff(P,x)).subs(x,0)==-2*D**2-12*D-48)
verify(s.factor(s.diff(P,x)).subs(x,1)==-12*D-144)

m.mp.dps=70
for d in [1,2,3,4,8,20]:
    f=lambda t:d*d*(1-t)**2+12*d*(1-t)-48*t*(t+1)
    root=m.findroot(f,(m.mpf('.1'),m.mpf('.9')),solver='anderson')
    vcrit=m.mpf(d)/(d+4)
    verify(0<root<vcrit<1)
    verify(abs(f(root))<m.mpf('1e-45'))
    for rr in [root/2, (root+vcrit)/2, (vcrit+1)/2]:
        phi=lambda z: m.hyper([],[m.mpf(d)/2], rr*z/4)/m.hyper([],[m.mpf(d)/2], z/4)
        p=m.mpf('0.00001')
        ph=phi(p)
        ph_prime=m.diff(phi,p)
        mean=(1-ph)/(p*ph)
        var=(1-ph**2+2*p*ph_prime)/(p*p*ph**2)
        mu1=m.mpf(str(m1.subs({D:d,x:str(rr)}).evalf(60)))
        mu2=m.mpf(str(m2.subs({D:d,x:str(rr)}).evalf(60)))
        exactmean=m.mpf(str(mean_grad.subs({D:d,x:str(rr)}).evalf(60)))
        exactvar=m.mpf(str(var_grad.subs({D:d,x:str(rr)}).evalf(60)))
        verify(abs(((mean-mu1)/p)-exactmean)<m.mpf('2e-5'))
        verify(abs(((var-(mu2-mu1*mu1))/p)-exactvar)<m.mpf('2e-5'))
        verify((exactvar>0 if rr<root else exactvar<0))
        verify((exactmean>0 if rr<vcrit else exactmean<0))
print(f'PASS {assertions} assertions; all dimension/radius regimes and independent transform computations agree')
