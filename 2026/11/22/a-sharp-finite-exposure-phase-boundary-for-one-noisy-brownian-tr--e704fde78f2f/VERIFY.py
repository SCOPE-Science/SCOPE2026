"""Exact identities and independent quadrature for sliding-window Brownian design."""
from fractions import Fraction
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
h,t,e,x,s=sp.symbols('h t e x s', positive=True, real=True)
C1=s
C2=t+x-x*x/(2*h)
C3=t+h/2
Nint=sp.integrate(C1*C1,(s,0,t))+sp.integrate(C2*C2,(x,0,h))+(1-t-h)*C3*C3
N= -sp.Rational(2,3)*t**3+(1-h)*t**2+(h-sp.Rational(7,12)*h*h)*t+h*h/sp.Integer(4)-sp.Rational(7,60)*h**3
assert sp.simplify(Nint-N)==0
D=t+h/3+e
p=sp.expand(sp.diff(N,t)*D-N)
assert sp.simplify(sp.diff(p,t)-2*(1-h-2*t)*D)==0
assert sp.simplify(sp.diff(N,t) - (2*t*(1-t-h)+h*(1-sp.Rational(7,12)*h)))==0
assert sp.simplify(p.subs(t,0)-h*(h*(15-14*h)+e*(180-105*h))/180)==0
F=46*h**3-165*h*h+180*h-60
assert sp.simplify(p.subs(t,1-h)-(F+15*h*(12-7*h)*e)/180)==0
etac=-F/(15*h*(12-7*h))
assert sp.simplify(p.subs({t:1-h,e:etac}))==0
assert sp.limit(h*etac,h,0)==sp.Rational(1,3)
assert sp.simplify(sp.diff(F,h)-6*(23*h*h-55*h+30))==0
p0=sp.expand(p.subs(h,0))
assert sp.simplify(p0-(-sp.Rational(2,3)*t*(2*t*t+(3*e-sp.Rational(3,2))*t-3*e)))==0
assert sp.simplify(N.subs(h,0)-(t*t-sp.Rational(2,3)*t**3))==0
hr=sp.polys.polytools.intervals(F,eps=sp.Rational(1,10**8))
roots=[a for (a,m) in hr if a[0]>=0 and a[1]<=1]
assert len(roots)==1
print('root_interval',roots)
for hh in [sp.Rational(1,8),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(9,10)]:
    for ee in [sp.Rational(0),sp.Rational(1,100),sp.Rational(1,10),sp.Integer(1),sp.Integer(100)]:
        hhf=float(hh); ef=float(ee)
        rr=minimize_scalar(lambda tt:-float((N/D).subs({h:hh,e:ee,t:tt})),bounds=(0,1-hhf),method='bounded',options={'xatol':1e-13})
        endpoint=-float((N/D).subs({h:hh,e:ee,t:1-hh}))
        if (hhf>float(sp.nroots(F)[0]) or ef >= float(etac.subs(h,hh))):
            assert -rr.fun <= -endpoint+2e-9
        else:
            assert -rr.fun > -endpoint+1e-10
        for tt in [0.05*(1-hhf),0.5*(1-hhf),0.95*(1-hhf)]:
            def gc(ss):
                if ss<tt: return ss
                if ss<tt+hhf:return tt+(ss-tt)-(ss-tt)**2/(2*hhf)
                return tt+hhf/2
            nquad=quad(lambda ss:gc(ss)**2,0,1,points=[tt,tt+hhf],epsabs=1e-13)[0]
            nalgebra=float(N.subs({h:hh,t:tt}))
            assert abs(nquad-nalgebra) < 3e-12
print('PASS: polynomial, endpoint, root, noise, point-limit and 75 independent quadrature checks')
