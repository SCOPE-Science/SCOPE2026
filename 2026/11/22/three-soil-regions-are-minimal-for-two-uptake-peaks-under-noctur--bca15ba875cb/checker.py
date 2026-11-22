"""Exact symbolic reproducibility checks for the three-zone uptake witness.
Run: python checker.py   (requires sympy>=1.12,<2)
"""
from fractions import Fraction
from math import exp, log
from random import Random
import sympy as s

q=s.symbols('q', real=True)
w1=s.Rational(1,3)+q/2+q**3/6
w2=(1-q**3)/3
w3=s.Rational(1,3)-q/2+q**3/6
w=[w1,w2,w3]
a=[23,1,7]
K=[s.Integer(1),s.Rational(1,20),s.Rational(1,5)]
U=sum(s.Rational(a[i])*w[i]/(K[i]+w[i]) for i in range(3))
P=(40625*q**14-180000*q**12+188200*q**11+122750*q**10-800*q**9
 +262155*q**8-1120200*q**7+972015*q**6-1652360*q**5+2122305*q**4
 -1078800*q**3+1117802*q**2-1121480*q+321632)
D=(20*q**3-23)**2*(q**3+3*q+8)**2*(5*q**3-15*q+16)**2
n=0
def check(cond,msg):
    global n
    assert bool(cond),msg
    n+=1

check(s.simplify(sum(w)-1)==0,'mass conservation')
for i in range(3):
    check(s.simplify(w[i].subs(q,1)-[1,0,0][i])==0,'initial condition')
    check(s.simplify(w[i].subs(q,0)-s.Rational(1,3))==0,'equilibrium')
    check(s.simplify(s.diff(w[i],q)*(-q)-([w2-w1,w1-2*w2+w3,w2-w3][i]))==0,'ODE')
check(s.factor(s.diff(U,q)-108*P/D)==0,'rational derivative identity')
check(s.gcd(P,s.diff(P,q))==1,'simple roots')
st=s.sturm(P,q)
variations=lambda x: sum(s.sign(a.subs(q,x))*s.sign(b.subs(q,x))==-1 for a,b in zip([v for v in [p.subs(q,x) for p in st] if v!=0],[v for v in [p.subs(q,x) for p in st] if v!=0][1:]))
check(variations(0)==9,'Sturm V(0)')
check(variations(1)==6,'Sturm V(1)')
check(s.polys.polytools.count_roots(P,0,1)==3,'exactly three positive roots')
for v,sgn in [('1/10',1),('7/10',-1),('9/10',1),('19/20',-1)]:
    v=s.Rational(v)
    check(s.sign(P.subs(q,v))==sgn,'sample signs')
for j in range(3):
    check(s.simplify(K[j]+w[j]).subs(q,s.Rational(0))>0,'denominator at 0')
    check(s.simplify(K[j]+w[j]).subs(q,s.Rational(1))>0,'denominator at 1')

# Independently integrate original ODE with RK4, not relying on the eigenformula.
def rk(kappa,steps=5000):
    x=[1.,0.,0.]
    h=1/steps
    def f(y):return [kappa*(y[1]-y[0]),kappa*(y[0]-2*y[1]+y[2]),kappa*(y[1]-y[2])]
    for _ in range(steps):
        z1=f(x)
        z2=f([x[i]+h*z1[i]/2 for i in range(3)])
        z3=f([x[i]+h*z2[i]/2 for i in range(3)])
        z4=f([x[i]+h*z3[i] for i in range(3)])
        x=[x[i]+h*(z1[i]+2*z2[i]+2*z3[i]+z4[i])/6 for i in range(3)]
    return x
for rate in [0.01,0.07,0.19,0.75,1.0,2.0,3.0]:
    z=exp(-rate)
    y=rk(rate)
    for j in range(3):check(abs(y[j]-float(w[j].subs(q,z)))<1e-11,'ODE numeric independent')

# The closed-form two-cell Hessian has strict negative sign for unequal initial states.
t=s.symbols('t',positive=True)
m,delta,aa,bb,k1,k2=s.symbols('m delta aa bb k1 k2',positive=True)
V=aa*(m+delta*t)/(k1+m+delta*t)+bb*(m-delta*t)/(k2+m-delta*t)
wanted=-2*delta**2*(aa*k1/(k1+m+delta*t)**3+bb*k2/(k2+m-delta*t)**3)
check(s.simplify(s.diff(V,t,2)-wanted)==0,'two-region strict concavity')
roots=sorted(float(s.re(z)) for z in s.nroots(P,maxsteps=300) if abs(float(s.im(z)))<1e-10 and 0<float(s.re(z))<1)
check(len(roots)==3,'numerical roots')
fn=s.lambdify(q,U,'math')
print('ASSERTIONS_PASSED',n)
print('STURM_VARIATIONS',variations(0),variations(1),'POLY_DEGREE',s.degree(P))
for z in roots:
    print('STATIONARY_ROOT_Q',format(z,'.15f'),'KAPPA_T',format(-log(z),'.15f'),'U',format(fn(z),'.15f'))
print('U_ZERO_CONDUCTANCE',fn(1.0),'U_INFINITE_CONDUCTANCE',fn(0.0))
