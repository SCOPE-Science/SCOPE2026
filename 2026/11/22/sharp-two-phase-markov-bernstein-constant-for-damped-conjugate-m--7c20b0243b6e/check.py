"""Supplementary numerical probes for the two-mode damped Markov--Bernstein formula.

The symbolic proof is in RESULT.md. These finite checks are not used as proof
of the global optimality, uniqueness, or all-parameter statements.
"""
import math
import random

PI = math.pi

def bisect(f, lo, hi, iterations=90):
    assert f(lo) <= 0 < f(hi)
    for _ in range(iterations):
        mid = (lo + hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi)/2

def phase1(r):
    return PI/2 + math.atan(r)

def contact(r):
    return bisect(lambda t: math.exp(r*t)*(r*math.sin(t)-math.cos(t))-1,
                  math.atan(1/r), PI)

def critical():
    return bisect(lambda r: 2*r/math.hypot(1,r)*math.exp(r*phase1(r))-1,
                  0.,1.)

def constant(r):
    u = min(phase1(r), contact(r))
    return (1+r*r)*math.exp(r*u)*math.sin(u), u

def envelope(r,u):
    return (1+r*r)*math.sin(u)/max(abs(math.cos(u)-r*math.sin(u)),math.exp(-r*u))

r_star = critical()
assert abs(r_star-0.2990843801527148) < 5e-13
random.seed(220912250)
count = 0
for r in [.001,.05,r_star,.3,.5,1,2,5,10,50]+[10**random.uniform(-3,1.1) for _ in range(48)]:
    c,u=constant(r)
    assert 0 < u < PI
    assert abs(c-envelope(r,u)) < 1e-9 * max(1,c)
    for j in range(1001):
        theta=PI*j/1000
        assert envelope(r,theta) <= c*(1+2e-10)
        count+=1
    phi=math.atan(r)
    amp=math.hypot(1,r)*math.exp(r*u)
    f=lambda t: amp*math.exp(-r*t)*math.cos(t-(u+phi))
    fp0=amp*(-r*math.cos(u+phi)+math.sin(u+phi))
    assert abs(fp0-c) < 2e-11*max(1,c)
    assert abs(f(u)-1) < 2e-11
    assert abs(f(0)) <= 1+2e-11
    for j in range(2001):
        t=(3*PI)*j/2000
        assert abs(f(t)) <= 1+4e-10
        count+=1
    if r > r_star+1e-9:
        assert abs(f(0)+1) < 3e-11
    if r < r_star-1e-9:
        assert f(0) > -1

q=bisect(lambda q: (q-1)*math.exp(q)-1,1,2)
kappa=q/(q-1)
assert abs(kappa-4.591121476668622) < 1e-4
assert abs(constant(100)[0]/100 -kappa)<.005

# A separate, direct coefficient-space search (no reliance on the
# optimizing-phase formula) for selected damping ratios.
for r in [.05,.2,.5,1.5,5.]:
    c,_=constant(r)
    trial=0.0
    for j in range(1501):
        theta=PI*j/1500
        x,y=math.cos(theta),math.sin(theta)
        ts=theta-math.atan(r)
        if ts<0: ts+=PI
        norm=max(abs(x),math.exp(-r*ts)/math.hypot(1,r))
        trial=max(trial,abs(-r*x+y)/norm)
    assert .99*c < trial <= c*(1+1e-10)

# Check the explicit one-sided second-derivative gap at the contact switch.
r = r_star
R = math.hypot(1,r)
u1 = phase1(r)
W = R*math.exp(r*u1)
predicted_jump = -(R*R)*W*(2/(R*R)+u1/W)**2
h = 1.e-4
v0 = constant(r)[0]
left = (v0-2*constant(r-h)[0]+constant(r-2*h)[0])/(h*h)
right = (constant(r+2*h)[0]-2*constant(r+h)[0]+v0)/(h*h)
assert predicted_jump < -1
assert abs((right-left)-predicted_jump)<.05

print('PASS',count,'phase and trajectory probes; threshold=',r_star,'large-damping slope=',kappa)
