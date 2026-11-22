"""Independent arithmetic checks for a two-time, two-mode heat sensor design.
Requires only Python 3 standard library. Finite checks supplement the proof.
"""
import math
import random

PI = math.pi
rng = random.Random(20261116)
checks = 0

def check(flag, message):
    global checks
    if not flag:
        raise AssertionError(message)
    checks += 1

def closed_form(k):
    root = math.sqrt((1.0 + 7.0*k*k)**2 - 48.0*k**4)
    w = 4.0*k*k/(1.0 + 7.0*k*k + root)
    s = math.sqrt((1.0-2.0*w)/(2.0-3.0*w))
    t = math.sqrt(w)
    return w,s,t,math.acos(s)/PI,math.acos(-t)/PI

def direct_det(x,y,q):
    a,b = math.sin(PI*x),math.sin(2*PI*x)
    c,d = q*math.sin(PI*y),q**4*math.sin(2*PI*y)
    return a*d-b*c

def target(k,w):
    q = k**(1.0/3.0)
    return 4.0*q*q*(1.0-w)**4/((1.0-2.0*w)*(2.0-3.0*w)**2)

# Three logically distinct calculations: direct physical measurement determinant,
# parameter-equation stationarity, and a closed maximum value.
for k in [1.0,0.9999,0.9,0.7,0.5,0.25,0.125,0.01,1e-4]:
    q=k**(1.0/3.0)
    w,s,t,x,y=closed_form(k)
    check(0.0<w<=1.0/3.0+1e-14, 'quadratic-root domain')
    check(0<x<.5<y<1.0, 'interior physical sites')
    check(abs(k*k*(1-2*w)*(2-3*w)-w)<2e-14, 'parameter identity')
    check(abs(2*s*s+k*s*t-1.0)<2e-14, 'first stationarity equation')
    check(abs(s*t+2*k*t*t-k)<2e-14, 'second stationarity equation')
    observed=direct_det(x,y,q)**2
    check(abs(observed-target(k,w))<3e-14, 'direct Fisher determinant value')
    check(abs(observed-direct_det(1.0-x,1.0-y,q)**2)<3e-14, 'reflection symmetry')
    # The full continuous domain, including equal sites and endpoints, is sampled.
    for a in range(81):
        xx=a/80.0
        for b in range(81):
            yy=b/80.0
            check(direct_det(xx,yy,q)**2 <= observed+1e-11, 'grid dominance')
    for _ in range(10000):
        xx=rng.random();yy=rng.random()
        check(direct_det(xx,yy,q)**2 <= observed+1e-11, 'random unrestricted dominance')

# Asymptotic independent checks; comparisons are finite tolerance validations only.
for k in [1e-2,1e-3,1e-4]:
    w,s,t,x,y=closed_form(k)
    check(abs((x-0.25)/(k*k)-1.0/(2*PI))<3*k*k, 'early-site long-time scaling')
    check(abs((y-0.5)/k-math.sqrt(2.0)/PI)<3*k*k, 'late-site long-time scaling')

# At coincident observation times, the locations are the static pair.
w,s,t,x,y=closed_form(1.0)
check(abs(x-math.acos(1.0/math.sqrt(3.0))/PI)<1e-14, 'static x limit')
check(abs(y-(1.0-x))<1e-14, 'static y limit')

# The static geometry loses a nonzero fraction of the D-optimal information
# as the second measurement is taken at increasingly late time.
q=1e-4; k=q**3
# Avoid explicitly computing a k**2 correction at machine precision.
x0=math.acos(1.0/math.sqrt(3.0))/PI
static=direct_det(x0,1.0-x0,q)**2
asymptotic=(q*q)
check(abs(asymptotic/static-27.0/16.0)<1e-10, 'sharp static-design loss')
print('HEAT_TWO_TIME_DESIGN_PASS',checks)
