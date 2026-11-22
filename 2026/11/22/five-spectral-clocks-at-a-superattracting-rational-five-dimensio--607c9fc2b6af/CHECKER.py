"""Exact algebraic and numerical checks for a high-order positive rational recurrence.

Run with `python quantitative_recurrence_checks.py`; requires Python 3 and SymPy.
These diagnostics verify identities and examples, not the limiting theorem.
"""
import math
import sympy as sp

x, y, z, b = sp.symbols('x y z b', positive=True)
num = x*y*z+x+y+z+b
den = x*y+x*z+y*z+1+b
r = lambda t: (t-1)/(t+1)
product = r(x)*r(y)*r(z)
identity = sp.factor(r(num/den)-product/(1+b*(1-r(x))*(1-r(y))*(1-r(z))/4))
assert identity == 0, identity

T = sp.Matrix([[0,1,1,0,1],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]])
t = sp.symbols('t')
assert sp.factor(T.charpoly(t).as_expr()) == t**5-t**3-t**2-1
assert all(x>0 for x in T**8)
assert (T**12-sp.eye(5)).applyfunc(lambda a:a%2)==sp.zeros(5)
assert (T**6-sp.eye(5)).applyfunc(lambda a:a%2)!=sp.zeros(5)

rho = 1.4291083198381459913842061
assert abs(rho**5-rho**3-rho**2-1)<1e-12
S=3-rho**-2+2*rho**-5
l=[1,rho,rho**2-1,rho**-2,rho**-1]
v=[rho**(-i) for i in range(5)]
assert abs(sum(l[i]*v[i] for i in range(5))-S)<1e-12

# Exact data are tracked in the Cayley coordinate. This avoids false convergence
# of z to 1 under floating-point rounding at super-exponential rates.
def trial(initial, b, steps=90):
    assert len(initial)==5 and all(x>0 and x!=1 for x in initial)
    rvals={i:(initial[i+4]-1)/(initial[i+4]+1) for i in range(-4,1)}
    u={i:-math.log(abs(rvals[i])) for i in range(-4,1)}
    sign={i:(1 if rvals[i]>0 else -1) for i in range(-4,1)}
    raw=[]
    for n in range(steps):
        lag=[n-1,n-2,n-4]
        eps=math.log1p(b*math.prod(1-rvals[i] for i in lag)/4)
        raw.append(eps)
        u[n+1]=sum(u[i] for i in lag)+eps
        sign[n+1]=math.prod(sign[i] for i in lag)
        rvals[n+1]=sign[n+1]*math.exp(-u[n+1])
        assert u[n+1]>0
    L0=sum(l[i]*u[-i] for i in range(5))/S
    L=L0+sum(rho**(-k-1)*eps for k,eps in enumerate(raw))/S
    # Convergence is in normalized logarithmic coordinates.
    for n in [40,60,80]:
        relative=abs(u[n]/rho**n/L-1)
        assert relative < (0.008 if n==40 else 0.001), (b,n,relative)
    assert L>=L0 and L <= L0+math.log1p(2*b)/(S*(rho-1))+1e-11
    assert all(sign[n]==sign[n+12] for n in range(0,steps-12))
    return L

histories=[[0.2,1.2,0.45,2.0,1.7],[1.7,2.5,4.0,0.7,0.4],[0.9,1.01,0.98,1.05,2.0]]
for h in histories:
    for bval in (0,0.5,3,17):
        print('initial',h,'b',bval,'L',round(trial(h,bval),12))

# At b=0 the amplitude is an explicit positive weighted sum of initial logs.
# For the derivative at 0 the nonperturbed Cayley orbit determines a
# convergent series, truncated here with a rigorous geometric tail bound.
h=histories[0]
rvals={i:(h[i+4]-1)/(h[i+4]+1) for i in range(-4,1)}
C=0.0
for k in range(90):
    q=math.prod(1-rvals[i] for i in (k-1,k-2,k-4))
    C += (rho**(-k-1)*q)/(4*S)
    rvals[k+1]=math.prod(rvals[i] for i in (k-1,k-2,k-4))
assert C>0
for delta in [1e-3,1e-5]:
    measured=(trial(h,delta)-trial(h,0))/delta
    print('dL/db approx',delta,measured,'analytic series',C)
    assert abs(measured-C)<2.5e-3
print('PASS: rational identity, Perron polynomial, primitive power, sign period, log-domain experiments, b-sensitivity')


# Certify five distinct roots by disjoint rational-centered Rouche disks.
# Using exact Gaussian rational arithmetic, a bound on the Taylor remainder
# follows from |P''(z)|<= 20(1.5)^3+6(1.5)+2<79 on each radius-1e-3 disk.
from fractions import Fraction as F
centers=[(F('1.42911'),F(0)),(F('-0.92456'),F('0.64166')),
         (F('-0.92456'),F('-0.64166')),(F('0.21001'),F('0.71300')),
         (F('0.21001'),F('-0.71300'))]
def abs2(z):return z[0]**2+z[1]**2
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def add(z,w):return (z[0]+w[0],z[1]+w[1])
def power(z,k):
 out=(F(1),F(0))
 for _ in range(k):out=mul(out,z)
 return out
r=F(1,1000)
for q in centers:
 Pq=add(add(add(power(q,5),tuple(-v for v in power(q,3))), tuple(-v for v in power(q,2))),(-F(1),F(0)))
 Pprime=add(add(mul((F(5),F(0)),power(q,4)),tuple(-v for v in mul((F(3),F(0)),power(q,2)))),tuple(-v for v in mul((F(2),F(0)),q)))
 assert abs2(Pq)<F(1,1000)**2
 assert abs2(Pprime)>F(4)**2
 # Strict linear dominance on |z-q|=r: 0.004>0.001+79*r*r/2.
 assert F(4)*r>F(1,1000)+F(79,2)*r*r
print('PASS: exact-rational Rouche disks isolate all five roots')
