"""Independent finite diagnostics for a two-zone reactive-storage model.

Run: python3 check.py
Uses only the Python standard library; numerical checks supplement, not replace,
the analytic proof in RESULT.md.
"""
import math
import random
from fractions import Fraction

TESTS = 0

def require(pred, description):
    global TESTS
    TESTS += 1
    if not pred:
        raise AssertionError(description)

def coefficients(v, a, b, p, q):
    c = v + p
    A = c + a
    B = b + q
    gap = math.hypot(A - B, 2 * math.sqrt(a*b))
    lo = (A + B - gap)/2
    hi = (A + B + gap)/2
    P = (p*(hi - A) + q*a)/gap
    Q = (p*(A - lo) - q*a)/gap
    return c, lo, hi, P, Q

def uptake(v, a, b, p, q, t):
    c, lo, hi, P, Q = coefficients(v, a, b, p, q)
    return P*(-math.expm1(-lo*t))/lo + Q*(-math.expm1(-hi*t))/hi

def baseline(v, p, t):
    c = v+p
    return (p/c)*(-math.expm1(-c*t))

def ultimate(v, a, b, p, q):
    c = v+p
    return (p*(b+q)+a*q)/(c*(b+q)+a*q)

def uniformized(v, a, b, p, q, t):
    omega = max(v+p+a, b+q)
    Q = [[-v-p-a,a,p,v], [b,-b-q,q,0], [0,0,0,0], [0,0,0,0]]
    transition = [[(1.0 if i==j else 0.0)+Q[i][j]/omega for j in range(4)] for i in range(4)]
    z = omega*t
    prob = math.exp(-z)
    vec=[1.,0.,0.,0.]
    total = 0.
    for k in range(240):
        total += prob*vec[2]
        if k>z+17*math.sqrt(z+1)+10: break
        vec=[sum(vec[i]*transition[i][j] for i in range(4)) for j in range(4)]
        prob *= z/(k+1)
    return total

def crossover(v,a,b,p,q):
    assert 0<q<p
    c,lo,hi,P,Q=coefficients(v,a,b,p,q)
    assert lo<c<hi and P>0 and Q>0
    # Strictly convex density ratio reaches its minimum before one rise through 1.
    tmin=math.log(Q*(hi-c)/(P*(c-lo)))/(hi-lo)
    assert tmin>0
    def F(t): return (P/p)*math.exp((c-lo)*t)+(Q/p)*math.exp(-(hi-c)*t)
    right=max(tmin*2,1.)
    while F(right)<1: right*=2
    left=tmin
    for _ in range(80):
        mid=(left+right)/2
        if F(mid)<1: left=mid
        else: right=mid
    density_cross=(left+right)/2
    def d(t): return uptake(v,a,b,p,q,t)-baseline(v,p,t)
    assert d(density_cross)<0
    left=density_cross
    right=max(2*left,1.)
    while d(right)<0: right*=2
    for _ in range(85):
        mid=(left+right)/2
        if d(mid)<0: left=mid
        else: right=mid
    return (left+right)/2, density_cross

rng=random.Random(349183)
# Exact rational first-step and matrix-inverse identities.
for _ in range(300):
    v,a,b,p,q=[Fraction(rng.randint(1,15),rng.randint(1,15)) for j in range(5)]
    c=v+p
    r=(p*(b+q)+a*q)/(c*(b+q)+a*q)
    s=(q+b*r)/(b+q)
    require((c+a)*r == p+a*s, 'first-step mobile mass balance')
    require((b+q)*s == q+b*r, 'first-step storage mass balance')
    require(r-p/c == a*q*v/(c*(c*(b+q)+a*q)), 'ultimate gain identity')
    require(0<r<1, 'valid absorption probability')

for _ in range(240):
    v,a,b,p=[rng.uniform(.3,2.7) for j in range(4)]
    q=rng.uniform(0.05*p,0.9*p)
    c,lo,hi,P,Q=coefficients(v,a,b,p,q)
    require(0<lo<c<hi, 'eigenvalue interlacing')
    require(P>0 and Q>0 and abs(P+Q-p)<1e-12, 'positive density mixture')
    tstar,td=crossover(v,a,b,p,q)
    require(tstar>td>0, 'cumulative after density crossover')
    for mult in (0.3,0.65,0.95):
        require(uptake(v,a,b,p,q,tstar*mult)<baseline(v,p,tstar*mult)+1e-11,'negative before crossing')
    for mult in (1.05,1.4,2.5):
        require(uptake(v,a,b,p,q,tstar*mult)>baseline(v,p,tstar*mult)-1e-11,'positive after crossing')
    require(abs(uptake(v,a,b,p,q,tstar)-baseline(v,p,tstar))<1e-10, 'crossover equation')
    require(abs(uptake(v,a,b,p,q,1000)-ultimate(v,a,b,p,q))<2e-10, 'ultimate')
    for t in (.1,.5,1.,2.,4.):
        require(abs(uptake(v,a,b,p,q,t)-uniformized(v,a,b,p,q,t))<3e-12,'independent uniformization')

for _ in range(100):
    v,a,b,p=[rng.uniform(.35,3) for j in range(4)]
    for t in (.1,.4,1.,3.,5.):
        require(uptake(v,a,b,p,0,t)<baseline(v,p,t),'inert storage finite delay')
        for q in (p,p*1.2,p*2):
            require(uptake(v,a,b,p,q,t)>baseline(v,p,t),'high-reactivity dominance')
    roots=[crossover(v,a,b,p,p*factor)[0] for factor in (.2,.4,.6,.8)]
    require(all(roots[j]>roots[j+1] for j in range(3)), 'crossover decreases in storage reactivity')

# Near both endpoints, confirm limiting slopes and logarithmic scale with independent values.
v,a,b,p=1.3,1.1,0.8,2.0
c,lo0,hi0,P0,Q0=coefficients(v,a,b,p,0.)
for q in (.0005,.0002,.00008):
    root,_=crossover(v,a,b,p,q)
    predicted=math.log(c*c*b*P0/(a*v*lo0*q))/lo0
    require(abs(root-predicted)<0.08,'weak-storage logarithmic law')
for delta in (.02,.01,.004):
    root,_=crossover(v,a,b,p,p-delta)
    predicted=3*delta/(v*p)
    require(abs(root/predicted-1)<0.08,'near equal-reaction linear law')

print(f'PASS: {TESTS} diagnostic assertions; exact-rational balances, CTMC uniformization, signs, unique crossovers, boundary scales.')
