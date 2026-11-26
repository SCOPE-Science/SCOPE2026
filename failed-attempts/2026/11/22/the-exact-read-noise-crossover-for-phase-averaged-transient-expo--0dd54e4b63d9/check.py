"""Independent finite checks for the phase-averaged exposure design theorem.
This program verifies examples and formulas; the infinite-domain proof is analytic.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random

checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def squared_overlap(phase, duration, width):
    # A pulse supported on [phase, phase+duration], against the grid width * Z.
    first = int(phase // width)
    last = int((phase + duration) // width)
    return sum(max(0.0, min(phase+duration, (j+1)*width) - max(phase, j*width))**2
               for j in range(first, last+1))

def closed_overlap(duration, width):
    if duration <= width:
        return duration**2-duration**3/(3*width)
    return duration*width-width**2/3

def phase_integral(duration, width, n=8000):
    return sum(squared_overlap((i+0.5)*width/n, duration, width)
               for i in range(n))/n

def optimum_ratio(r):
    if r <= 1:
        return sqrt(r*r+3*r)-r
    return (1+sqrt(1+3*r))/3

def score(x,r):
    if x<=1:
        return (x-x*x/3)/(x+r)
    return (1-1/(3*x))/(x+r)

# Exact rational phase averages and exact junction/derivative factors.
for i in range(1,35):
    for j in range(1,35):
        T=Fraction(i,11); h=Fraction(j,13)
        e=closed_overlap(T,h)
        bound = (T*T-T*T*T/(3*h) if T<=h else T*h-h*h/3)
        check(e==bound, 'rational identity')

# Independently compute phase averages from actual interval intersections.
rng=Random(441917)
for k in range(150):
    T=10**rng.uniform(-1,1)
    h=T*10**rng.uniform(-1.5,1.5)
    a=phase_integral(T,h)
    b=closed_overlap(T,h)
    check(abs(a-b)/b<2e-6, ('quadrature', k, a, b))

# Verify that computed optimizer strictly beats systematic deviations.
for j in range(1,201):
    r=10**(-5+10*j/201)
    x=optimum_ratio(r)
    check(x>0 and ((r<1 and x<1) or (r>1 and x>1)), 'phase condition')
    check(abs((r-(2*r*x+x*x)/3) if x<=1 else (2*x+r-3*x*x))<1e-8*max(1,r), 'derivative root')
    fx=score(x,r)
    for f in (.1,.25,.5,.75,.9,1.1,1.25,2,4,10):
        check(fx>score(x*f,r),('global',r,f))

# Exact junction and asymptotic monotonicity diagnostics.
check(optimum_ratio(1)==1, 'junction')
for r in (1e-8,1e-7,1e-6):
    check(abs(optimum_ratio(r)/sqrt(3*r)-1)<0.01, 'small-r')
for r in (1e5,1e6,1e7):
    check(abs(optimum_ratio(r)/sqrt(r/3)-1)<0.01, 'large-r')
print(f'PASS {checks} assertions')
