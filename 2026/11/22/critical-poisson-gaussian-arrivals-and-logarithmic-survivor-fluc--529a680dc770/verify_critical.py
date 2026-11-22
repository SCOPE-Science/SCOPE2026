"""Deterministic consistency checks for marked critical mortal Brownian search.

Run: python verify_critical.py (requires SciPy >=1.8).
These finite checks are not substitutes for the analytic theorem.
"""
import math
from scipy.integrate import quad
from scipy.special import erfcx

SQRT2PI = math.sqrt(2.0 * math.pi)
C_STAR = (1 + 4*math.exp(-1.5))/(2*SQRT2PI)
checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def phi(v):
    return math.exp(-v*v/2)/SQRT2PI

def g(q,v):
    h=1+v/math.sqrt(q)
    if h <= 0:
        return 0.0
    log_pdf=-0.5*math.log(2*math.pi)-1.5*math.log(h)-v*v/(2*h)
    return math.exp(log_pdf) if log_pdf > -740 else 0.0

def H(q,v):
    u=(1+v/math.sqrt(q))/(2*q)
    if u <= 0:
        return 0.0
    a=1/(2*math.sqrt(u))
    b=q*math.sqrt(u)
    return (math.exp(q-1/(4*u)-q*q*u)*erfcx(a+b)+math.erfc(a-b))/2

def integrate_g(q, func):
    # Splitting at the mode reduces any numerical quadrature stiffness.
    return quad(lambda z:func(z)*g(q,z), -math.sqrt(q), 0, epsabs=2e-10,limit=400)[0]+quad(lambda z:func(z)*g(q,z),0, math.inf,epsabs=2e-10,limit=400)[0]

for q in [1,2,4,10,20,50,100,400]:
    check(abs(integrate_g(q,lambda z:1)-1)<3e-9,f'normalization {q}')
    check(abs(integrate_g(q,lambda z:z))<3e-8,f'zero mean {q}')
    check(abs(integrate_g(q,lambda z:z*z)-1)<3e-7,f'unit variance {q}')
    for v in [-2,-1,0,1,2]:
        if v <=-math.sqrt(q):
            continue
        left=quad(lambda z:g(q,z),-math.sqrt(q),v,epsabs=3e-10,limit=400)[0]
        check(abs(left-H(q,v))<2e-8,f'CDF {q},{v}')
    for t in [-0.25,0.15]:
        if 2*t/math.sqrt(q)>=1:
            continue
        right=math.exp(-t*math.sqrt(q)+q-math.sqrt(q*q-2*t*q**1.5))
        left=integrate_g(q,lambda z:math.exp(t*z))
        check(abs(left-right)<1e-7,f'MGF {q},{t}')

for q in [10,20,30,50,100,300,1000]:
    s=math.sqrt(q)
    # Compute the TV integral, retaining the normal mass below -sqrt(q).
    left=quad(lambda v:abs(g(q,v)-phi(v)),-s,0,epsabs=2e-9,limit=700)[0]
    right=quad(lambda v:abs(g(q,v)-phi(v)),0,35,epsabs=2e-9,limit=700)[0]
    missing=0.5*math.erfc(s/math.sqrt(2))
    delta=0.5*(left+right+missing)
    check(abs(s*delta-C_STAR)<0.02,f'TV constant {q}, observed={s*delta}')

for N in [10_000,100_000,10_000_000]:
    for c in [-0.75,0,0.75]:
        q=math.log(N)+c
        m=math.exp(-c)
        p=m/N
        for z in [-1.0,0.0,1.0]:
            h=H(q,z)
            sf=math.exp(N*math.log1p(-p*h))
            approx=math.exp(-m*0.5*math.erfc(-z/math.sqrt(2)))
            # Robust qualitative scaling; the rate follows analytically from TV.
            check(abs(sf-approx)<1.3/math.sqrt(q), f'critical survival {N},{c},{z}')
        check(abs((1-p)**N-math.exp(-m))<3*m*m/N,f'failure atom {N},{c}')

for N in [10_000,100_000,10_000_000,10_000_000_000]:
    for c in [-0.75,0,0.75]:
        q=math.log(N)+c
        for v in [-2.0,-1.0,0,1.0,2.0]:
            u=(1+v/math.sqrt(q))/(2*q)
            if u<=0:
                continue
            F=math.exp(-q)*H(q,v)
            still=math.exp(-q*q*u)*math.erf(1/(2*math.sqrt(u)))
            a_mean=(N-1)*still/(1-F)
            R=(2/math.sqrt(q))*(math.log(a_mean)-math.log(N)+q/2)
            check(abs(R+v)<0.06, f'survivor logarithm {N},{c},{v},{R}')
            check(a_mean>0, f'conditional mean survivor count {N},{c},{v}')

print(f'PASS: {checks} deterministic consistency checks (not an infinite proof)')
print(f'TV leading constant: {C_STAR:.15f}')
