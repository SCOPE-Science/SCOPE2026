"""Standalone symbolic and numerical checks of a periodically modulated game fold."""
import sympy as sp
from math import pi, cos
from scipy.integrate import solve_ivp
from scipy.optimize import root

x,t,e=sp.symbols('x t e', real=True)
a=sp.Rational(1,2); b=sp.Rational(3,2); theta=sp.Rational(3,8)
h=1-a; d=b-1
G2=(1-h*x)/2
G3=(1+d*x)**2/3
k=sp.expand(G3-G2)
G=sp.expand(G2+theta*k)
q=sp.expand(G).coeff(x,2)
s=sp.solve(sp.diff(G,x),x)[0]
g0=sp.simplify(G.subs(x,s)); r0=1/g0
P=sp.expand(x*(1-x))
K=sp.simplify(P.subs(x,s)**2*r0**4*q*k.subs(x,s)**2/2)
assert (s,q,g0,r0,k.subs(x,s))==(sp.Rational(1,2),sp.Rational(1,32),sp.Rational(55,128),sp.Rational(128,55),sp.Rational(7,48))
print('EXACT NORMAL FOLD:',s,q,g0,r0,K)
# Check the explicit vanishing-forcing fold.
s0=(-7+sp.sqrt(57))/2
th0=3/sp.sqrt(57)
rstar=(11+sp.sqrt(57))/8
assert sp.simplify(k.subs(x,s0))==0
assert sp.simplify(sp.diff(G2+th0*k,x).subs(x,s0))==0
assert sp.simplify(rstar*(G2+th0*k).subs(x,s0)-1)==0
print('EXACT IMMUNE FOLD:',s0,th0,rstar)

def map_fold(x0,rv,eps,omega):
  def rhs(t,z):
    y,m=z
    p=y*(1-y)
    th=float(theta)+eps*cos(omega*t)
    gn=(1-th)/2*(1-float(h)*y)+th/3*(1+float(d)*y)**2
    gx=-(1-th)*float(h)/2+2*th/3*float(d)*(1+float(d)*y)
    yy=p*(rv*gn-1)
    mm=((1-2*y)*(rv*gn-1)+p*rv*gx)*m
    return (yy,mm)
  sol=solve_ivp(rhs,(0,2*pi/omega),(x0,1.0),atol=1e-12,rtol=1e-12)
  return sol.y[0,-1],sol.y[1,-1]

for omega in (1.,2.):
    kval=float(K)/omega**2
    for eps in (0.08,0.12,0.16):
        rr=root(lambda z:[map_fold(z[0],z[1],eps,omega)[0]-z[0],map_fold(z[0],z[1],eps,omega)[1]-1],
             [float(s),float(r0)-kval*eps*eps],tol=1e-9)
        assert rr.success or max(abs(w) for w in rr.fun)<1e-8,rr.message
        m=map_fold(*rr.x,eps,omega)
        coeff=(float(r0)-rr.x[1])/eps**2
        assert abs(m[0]-rr.x[0])<5e-9 and abs(m[1]-1)<5e-9
        assert abs(coeff/kval-1)<.2,(omega,eps,coeff,kval)
        print('NUMERICAL:',omega,eps,'periodic fold',rr.x,'coefficient',coeff,'predicted',kval)

# Check exact neutral return and unit multiplier for noninfinitesimal forcing.
from math import sqrt, sin
s_pin=(sqrt(57)-7)/2
th_pin=3/sqrt(57)
r_pin=(11+sqrt(57))/8
for omega in (1.0, 2.0):
    for eps in (.10,.30):
        for shape in (0,1):
            def special(t,z):
                y,m=z
                waveform=cos(omega*t)+(0.25*sin(2*omega*t) if shape else 0.0)
                th=th_pin+eps*waveform
                assert 0<th<1
                gn=(1-th)/2*(1-.5*y)+th/3*(1+.5*y)**2
                gx=-(1-th)/4+th/3*(1+.5*y)
                return (y*(1-y)*(r_pin*gn-1),
                        ((1-2*y)*(r_pin*gn-1)+y*(1-y)*r_pin*gx)*m)
            sol=solve_ivp(special,(0,2*pi/omega),(s_pin,1),rtol=1e-11,atol=1e-11)
            assert abs(sol.y[0,-1]-s_pin)<1e-9
            assert abs(sol.y[1,-1]-1)<1e-9
            print('EXACT PIN PERIODIC:',omega,eps,shape,sol.y[0,-1],sol.y[1,-1])
print('all checks passed')
