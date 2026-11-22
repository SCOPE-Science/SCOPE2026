"""Reproducibility checks for the fixed-horizon backward-Euler damping theorem.

The symbolic algebra validates identities; finite samples are supplementary and
are not used as a proof of the quantified global optimization theorem.
"""
import itertools
import math
import random
from fractions import Fraction
import sympy as S
from scipy.optimize import brentq

x,y,a,b=S.symbols('x y a b', real=True)
r2=a*a+b*b
q=lambda t:1+2*a*t+r2*t*t
p=x*y
s=x+y
pair=S.expand(q(x)*q(y)-q(s)-2*(a*a-b*b+a*r2*s)*p-r2*r2*p*p)
assert S.simplify(pair)==0
print('symbolic pair identity: PASS')
u=S.symbols('u', real=True)
gppnum=S.expand(r2*q(u)-2*(a+r2*u)**2)
assert S.simplify(gppnum-(b*b-a*a-2*a*r2*u-r2*r2*u*u))==0
print('log curvature identity: PASS')
N=S.factor((a+r2*x)*q(y)-(a+r2*y)*q(x))
assert S.simplify(N-(y-x)*(a*a-b*b+a*r2*(x+y)+r2*r2*x*y))==0
print('derivative comparison identity: PASS')

def scale(a,b,H,n):
    r2=a*a+b*b
    def logq(t):return math.log1p(2*a*t+r2*t*t)
    values=[k*logq(H/k) for k in range(1,n+1)]
    optimum=max(values)
    ks=[i+1 for i,v in enumerate(values) if abs(v-optimum)<1e-10]
    if b<=a:assert ks==[n]
    else:
        def func(t):return 2*t*(a+r2*t)/(1+2*a*t+r2*t*t)-logq(t)
        tlo=1e-8/a
        hi=10/a
        while func(hi)>0:hi*=2
        star=brentq(func,tlo,hi,xtol=1e-14)
        guess=H/star
        expected={max(1,min(n,k)) for k in (math.floor(guess),math.ceil(guess))}
        assert set(ks).issubset(expected),(a,b,H,n,ks,expected)
        if n==3 and a==1 and b==2:
            pass
    return ks,math.exp(-optimum)

rng=random.Random(3502)
for test in range(1500):
    av=10**rng.uniform(-1,1)
    bv=av*rng.choice([0,.2,1,1.02,1.5,2,4,15])
    H=10**rng.uniform(-2,1)/av
    n=rng.randrange(2,9)
    ks,ret=scale(av,bv,H,n)
    for j in range(25):
        times=[rng.expovariate(1) for _ in range(n)]
        z=sum(times)
        times=[H*t/z for t in times]
        product=1.
        for t in times:product*=1+2*av*t+(av*av+bv*bv)*t*t
        assert 1/product >= ret-1e-11
print('1,500 parameter tests x 25 simplex schedules: PASS')

A=Fraction(1);B=Fraction(4);H=Fraction(1,2)
qf=lambda z:1+2*A*z+(A*A+B*B)*z*z
p2=qf(H/2)**2;p4=qf(H/4)**4
assert p2==Fraction(1681,256)
assert p4==Fraction(97,64)**4
print('example n=4, H=1/2, a=1, b=4:')
print('two active steps, retention',Fraction(1,p2),'=',float(1/p2))
print('four equal steps, retention',Fraction(1,p4),'=',float(1/p4))
print('relative reduction', 1-(1/p2)/(1/p4))

av=1.;bv=2.;r2=5.
def f(k,h):return k*math.log1p(2*av*h/k+r2*(h/k)**2)
for k in [1,2]:
    def delta(h):return f(k+1,h)-f(k,h)
    root=brentq(delta,0.2 if k==1 else 0.6,0.6 if k==1 else 1.2)
    print('a=1,b=2, threshold',k,'to',k+1,':',format(root,'.12f'))
print('all checks PASS')
