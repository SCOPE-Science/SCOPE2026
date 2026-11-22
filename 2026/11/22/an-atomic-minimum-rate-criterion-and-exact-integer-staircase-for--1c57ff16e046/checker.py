"""Reproducible numerical checks for the heterogeneous site-survey theorem.

Only finite-mixture examples are checked numerically. The all-distribution
and all-horizon assertions are established analytically in RESULT.md.
Run with Python 3.10+; no third-party dependencies.
"""
import math
import random

RNG = random.Random(487320)
assertions = 0

def check(condition, message):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(message)

def moments(t, atoms):
    # The smallest atom is factored out to avoid large-exponent underflow.
    low = min(rate for weight, rate in atoms)
    terms = [(weight*math.exp(-(rate-low)*t), rate) for weight,rate in atoms]
    mass = sum(weight for weight,_ in terms)
    weights = [w/mass for w,_ in terms]
    mean = sum(w*rate for w,(_,rate) in zip(weights,terms))
    second = sum(w*(rate-mean)**2 for w,(_,rate) in zip(weights,terms))
    phi = low*t-math.log(mass)
    return phi,mean,second

def score(n, H, c, atoms):
    t = (H-(n-1)*c)/n
    if t < -1e-12:
        raise ValueError('unfeasible')
    return n*moments(max(t,0), atoms)[0]

def root(c, atoms):
    def h(t):
        f,fp,_ = moments(t,atoms)
        return (t+c)*fp-f
    lo,hi = 0.0,1.0
    for j in range(60):
        if h(hi)<0:
            break
        hi *= 2.0
    else:
        return None
    for _ in range(100):
        mid=(lo+hi)/2
        if h(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

# A slowest positive-rate atom yields an exact critical relocation cost.
q, low, high = 0.1, 1.0, 10.0
atoms = [(q,low),(1-q,high)]
threshold = -math.log(q)/low
check(abs(threshold-2.3025850929940455)<1e-13,'critical cost')
tstar = root(1.0,atoms)
check(tstar is not None and abs(tstar-0.5019821049332724)<1e-11,'root')
check(root(3.0,atoms) is None,'no optimum for expensive relocation')
for c in (threshold,threshold*1.00001,3.0,5.0):
    for H in (1.0,3.0,5.0,10.0,24.0):
        candidates=[n for n in range(1,int(H/c)+2) if (n-1)*c<=H+1e-12]
        scores=[score(n,H,c,atoms) for n in candidates]
        check(scores[0]>=max(scores[1:],default=-1)-5e-12,'never rotate')
for H, opt in ((3,3),(4,3),(5,4),(10,7)):
    candidates=[n for n in range(1,int(H)+2) if n-1<=H]
    check(max(candidates,key=lambda n:score(n,H,1,atoms))==opt,'numeric optimum')

# Exact differentiation identities, strict discrete concavity and integer bracketing.
for case in range(350):
    k=RNG.randint(2,5)
    rates=sorted(RNG.uniform(.1,8) for _ in range(k))
    raw=[RNG.random()+.1 for _ in range(k)]
    atoms=list(zip([v/sum(raw) for v in raw],rates))
    c=RNG.uniform(.02,2.5)
    H=RNG.uniform(8,45)
    r=root(c,atoms)
    if r is not None:
        x=(H+c)/(r+c)
        cand=[n for n in range(1,int(H/c)+2) if (n-1)*c<=H+1e-12]
        best=max(cand,key=lambda n:score(n,H,c,atoms))
        floor=math.floor(x)
        ceil=math.ceil(x)
        check(best in {max(1,floor),max(1,ceil)},'continuous integer bracketing')
    available=[n for n in range(1,min(12,int(H/c)+2)) if (n-1)*c<=H]
    for n in available[1:-1]:
        a=score(n-1,H,c,atoms)
        b=score(n,H,c,atoms)
        d=score(n+1,H,c,atoms)
        check(2*b>=a+d-2e-11, f'discrete concavity: case {case}, n {n}, H {H}, c {c}, atoms {atoms}, scores {(a,b,d)}')
    for _ in range(7):
        t=RNG.uniform(.001,15.0)
        f,fp,var=moments(t,atoms)
        check(f>=0 and fp>0 and var>0,'positive intensity and variance')
        eps=2e-5
        num=(moments(t+eps,atoms)[0]-moments(t-eps,atoms)[0])/(2*eps)
        check(abs(num-fp)<1e-6,'first derivative')
        num2=(moments(t+eps,atoms)[1]-moments(t-eps,atoms)[1])/(2*eps)
        check(abs(num2+var)<2e-6,'negative variance identity')

# For uniform[1,3], L(t) = exp(-t) (1-exp(-2t))/(2t).
def uniform_phi(t):
    return t-math.log(-math.expm1(-2*t)/(2*t))
def uniform_phi_deriv(t):
    return 1+1/t-(2/math.expm1(2*t) if t<350 else 0.0)
for c in (0.1,1,3,10):
    def h(t):return (t+c)*uniform_phi_deriv(t)-uniform_phi(t)
    lo,hi=1e-6,1.0
    while h(hi)>0:hi*=2
    for _ in range(100):
        m=(lo+hi)/2
        if h(m)>0:lo=m
        else:hi=m
    rt=(lo+hi)/2
    check(h(rt)<1e-7,'atomless distribution finite optimum')

print('PASS:',assertions,'supplementary assertions')
