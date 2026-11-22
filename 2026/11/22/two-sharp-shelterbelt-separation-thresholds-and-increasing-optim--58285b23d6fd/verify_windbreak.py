"""Reproducible checks for a three-row exponential wind-recovery benchmark.

The proof is analytic. These finite checks independently compare its optimizer
with the original state evolution, explicit boundaries, and sampled placements.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose
from random import Random

checks = 0

def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def objective(a, E, x, y):
    """Dimensionless integrated wind deficit, 0<E<=y<=x<=1."""
    u2 = 1-a*x
    u3 = 1-a*y-a*u2*y/x
    return a*(1-E)+a*u2*(1-E/x)+a*u3*(1-E/y)

def independent_integral(a, E, x, y):
    """Integrate recovery in the three intervals after the first row."""
    r = 1-a
    total = 0.0
    for attenuation in (x, y/x, E/y):
        total += (1-r)*(1-attenuation)
        r = 1-(1-r)*attenuation
        r *= 1-a
    # Last interval has no subsequent row: avoid multiplying its endpoint.
    # Multiplication after the third interval above changes no integral.
    return total

def second_threshold(a):
    E1=a*(2-a)
    lo,hi=0.,E1
    for _ in range(90):
        m=(lo+hi)/2
        g=sqrt(m/E1)+m*(1-a)/a
        if g<1: lo=m
        else: hi=m
    return (lo+hi)/2

def optimizer(a,E):
    E1=a*(2-a)
    if E >= E1:
        return 1.,1.
    q=E*(1-a)/a
    def optimal_x(y): return min(1.,sqrt(y+q))
    def f(y): return a*y*y*((1-a)+1/optimal_x(y))
    lo,hi=E,1.
    for _ in range(85):
        mid=(lo+hi)/2
        if f(mid)<E: lo=mid
        else: hi=mid
    y=(lo+hi)/2
    return optimal_x(y),y

# Exact independent rational evaluation.
a=F(1,2);E=F(1,9);x=F(2,3);y=F(1,3)
check(objective(a,E,x,y)==F(17,18),"exact optimum 17/18")
check(objective(a,E,F(1),F(1))==F(7,9),"coincident rows 7/9")
check((objective(a,E,x,y)-objective(a,E,F(1),F(1)))/objective(a,E,F(1),F(1))==F(3,14),"exact relative improvement")
check(abs(second_threshold(.5)-1/3)<1e-14,"second threshold E=1/3")
check(abs(.5*(2-.5)-.75)<1e-14,"first threshold E=3/4")
xo,yo=optimizer(.5,1/9)
check(abs(xo-2/3)<1e-13 and abs(yo-1/3)<1e-13,"exact interior placement")

rng=Random(4829)
# Independently integrate state evolution over a broad interior domain.
for _ in range(5000):
    a=.02+.96*rng.random();E=.001+.99*rng.random()
    y=E+(1-E)*rng.random();x=y+(1-y)*rng.random()
    v=objective(a,E,x,y)
    w=independent_integral(a,E,x,y)
    check(abs(v-w)<2e-13,"state-evolution integral")

# Global candidate check, including boundaries and random placements.
for a in (.05,.15,.3,.5,.7,.85,.95):
    E1=a*(2-a);E2=second_threshold(a)
    for E in (.002,.02,.08,.15,.3,.5,.7,.9, E1, min(.999999,E1*1.000001), E2, E2*.999999, min(.999999,E2*1.000001)):
        if not 0<E<1:continue
        x,y=optimizer(a,E)
        v=objective(a,E,x,y)
        check(E-1e-14<=y<=x<=1+1e-14,"feasible optimal location")
        if E >= E1:
            check(abs(x-1)<1e-13 and abs(y-1)<1e-13,"clustered regime")
        elif E>=E2+1e-12:
            check(abs(x-1)<1e-12 and y<1,"partially separated regime")
        elif E<E2-1e-12:
            check(x<1 and y<x,"fully separated regime")
        if y<1-1e-12:
            check(y*y > E*x and x*x>=y,"ordered gaps")
        for _ in range(850):
            z=E+(1-E)*rng.random()
            w=z+(1-z)*rng.random()
            check(objective(a,E,w,z)<=v+4e-13,"global random competitor")
        for xx,yy in ((1,1),(1,E),(E,E),(x,x),(1,y),(y,y),(1,E),(x,E),(x,y)):
            if E<=yy<=xx<=1:
                check(objective(a,E,xx,yy)<=v+4e-13,"boundary competitor")

# The exact example is strictly better than equal logarithmic spacing.
xe=(1/9)**(1/3);ye=(1/9)**(2/3)
check(objective(.5,1/9,2/3,1/3)>objective(.5,1/9,xe,ye),"equal spacing is suboptimal")
print('PASS',checks,'assertions')
print('thresholds at a=1/2:', '.75,',round(second_threshold(.5),15))
print('exact case: J optimum=17/18, J cluster=7/9, relative increase=3/14')
