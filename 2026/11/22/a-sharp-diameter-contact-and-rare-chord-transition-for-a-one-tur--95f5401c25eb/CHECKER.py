"""Reproducibility tests for the one-turn helix diameter and random-chord laws.
Python 3 standard library only. Numerical tests complement analytic arguments.
"""
import math

L = 2.0 * math.pi

def root(f, lo, hi, steps=100):
    fl = f(lo)
    assert fl * f(hi) < 0, (lo, hi, fl, f(hi))
    for _ in range(steps):
        mid = (lo + hi) / 2.0
        if fl * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
            fl = f(mid)
    return (lo + hi) / 2.0

rho = root(lambda d: d*math.cos(d)-math.sin(d), math.pi, 1.5*math.pi)
def bfun(d):
    return 2*(1-math.cos(d)) + (L*L-d*d)*math.sin(d)/d
sstar = root(bfun, math.pi, rho)
astar = 2*(1-math.cos(sstar))/(L*L-sstar*sstar)
cstar = math.sqrt(astar)
J = (L*L-sstar*sstar)/L
Dstar = cstar*L
Cstar = 4*(L-sstar)/(L*L)*math.sqrt(2*Dstar/(-math.cos(sstar)-astar))

def distance(c, d):
    return math.hypot(2*math.sin(d/2), c*d)

def interior(c):
    if c == 0.0:
        return math.pi
    if c <= cstar * 1.00001:
        return root(lambda d: math.sin(d)+c*c*d, math.pi, rho)
    return None

def diameter(c):
    if c<=cstar:
        return distance(c, interior(c))
    return c*L

def coefficient(c):
    d=interior(c)
    m=distance(c,d)
    return 4*(L-d)/(L*L)*math.sqrt(2*m/(-math.cos(d)-c*c))

def prob(c, eps, steps=9000):
    """Direct finite quadrature from the exact triangular separation density.
    Root finding and an exact antiderivative, not asymptotic approximations.
    """
    m=diameter(c)
    cut=m-eps
    def f(d):return distance(c,d)-cut
    # midpoint samples detect short components and end contacts
    res=[]
    x0=0.0
    v0=f(x0)
    inside=v0>=0
    start=x0 if inside else None
    for k in range(1,steps+1):
        x1=L*k/steps
        v1=f(x1)
        now=v1>=0
        if now != inside:
            q=root(f,x0,x1)
            if now:
                start=q
            else:
                res.append((start,q))
                start=None
        if k==steps and now:
            res.append((start,L))
        x0,v0,inside=x1,v1,now
    return sum(((L-a)**2-(L-b)**2)/(L*L) for a,b in res)

n=0
def check(condition, msg):
    global n
    n+=1
    if not condition:
        raise AssertionError(msg)

check(math.pi < sstar < rho < 1.5*math.pi,'critical separation')
check(abs(sstar-3.70067724512362)<1e-10,'critical root')
check(abs(cstar-0.3785867471122712)<1e-12,'critical pitch')
check(abs(bfun(sstar))<1e-12,'stationary critical')
check(abs(distance(cstar,sstar)-distance(cstar,L))<1e-12,'diameter coexistence')
check(abs(Cstar-0.680010892323401)<1e-10,'critical asymptotic constant')
check(abs(J-4.103556440125885)<1e-11,'crossover slope')
for k in range(1,8000):
    d=L*k/8000
    h=2*(1-math.cos(d))/(L*L-d*d)
    check(h <= astar+3e-15, 'ratio envelope')
for c in (0.0,0.08,0.2,0.3,0.37,cstar,0.4,0.48,0.65,1.5):
    m=diameter(c)
    for k in range(2001):
        d=k*L/2000
        check(distance(c,d)<=m+2e-14, 'global diameter')
for c in (0.0,0.2,0.35,cstar):
    for eps in (3e-5,1e-5):
        measured=prob(c,eps)
        predicted=coefficient(c)*math.sqrt(eps)
        check(abs(measured/predicted-1)<0.02, ('interior tail',c,eps,measured,predicted))
for c in (0.4,0.55,1.0):
    for eps in (3e-5,1e-5):
        measured=prob(c,eps)
        predicted=eps*eps/(c*c*L*L)
        check(abs(measured/predicted-1)<0.02, ('endpoint tail',c,eps,measured,predicted))
for lam in (-0.2,0.0,0.08,0.15):
    eps=1e-5
    c=cstar+lam*eps
    measured=prob(c,eps)
    predicted=Cstar*math.sqrt(max(0,1-J*max(lam,0)))*math.sqrt(eps)
    check(abs(measured/predicted-1)<0.03, ('moving crossover',lam,measured,predicted))
# Near the cutoff and past it, the sqrt(epsilon)-rescaled mass vanishes.
for lam in (0.3,0.5):
    eps=1e-5
    measured=prob(cstar+lam*eps,eps)
    check(measured/math.sqrt(eps)<1e-4, ('vanishing crossover',lam,measured))
print(f'PASS: {n} deterministic assertions')
print(f'critical separation {sstar:.15f}, critical pitch {cstar:.15f}')
print(f'critical tail coefficient {Cstar:.15f}, crossover slope {J:.15f}')
