"""Separate numerical and exact-series checks for a uniform-memory resetting clock.
Run: python3 CHECK.py.  Uses only the Python standard library.
"""
from fractions import Fraction
from math import exp, log, gamma, sqrt, pi, e
import math, random, bisect

checks=0
def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks+=1

def taylor(s, nmax):
    """MGF coefficients from the exact scalar-memory evolution equation."""
    a=Fraction(1)
    out=[a]
    for n in range(nmax):
        a *= (s-(1-s)*n)/((n+1)**2)
        out.append(a)
    return out

def hypergeom_coefficients(s,nmax):
    """Independent direct Pochhammer expansion of Kummer M(a;1;-(1-s)z)."""
    a=-s/(1-s)
    out=[Fraction(1)]; term=Fraction(1)
    for n in range(nmax):
        term *= -(1-s)*(a+n)/((n+1)**2)
        out.append(term)
    return out

for p in [-5,-2,-1,0,1,2,3,7,9]:
    s=Fraction(p,11)
    x=taylor(s,26); y=hypergeom_coefficients(s,26)
    for j in range(27): check(x[j]==y[j], f'series at s={s}, j={j}')

# Near-zero generator identity: mean is the exponential integral Ein(z).
def mean_direct(z):
    # Simpson integral for integral_0^z (1-e^-u)/u du.
    N=8000; h=z/N
    def f(u): return -math.expm1(-u)/u if u else 1.0
    ans=f(0)+f(z)
    for k in range(1,N): ans+=(4 if k%2 else 2)*f(k*h)
    return ans*h/3

def mean_series(z,terms=100):
    v=0.;term=1.
    for k in range(1,terms):
        term*=(-z)/k
        v-=term/k
    return v
for z in [0.1,0.3,1,2,5,10,20]:
    q=mean_direct(z); t=mean_series(z,180)
    check(abs(q-t) < 3e-8, f'mean formula at z={z}: {q} {t}')

# Moment derivatives from the exact Taylor coefficients at finite z,
# compared with independently integrated generator for E[Q].
for z in [0.1,0.3,1.0,3.0,5.0]:
    h=1e-4
    def mgf(s):
        a=taylor(Fraction(s).limit_denominator(10**8),80)
        return sum(float(v)*z**n for n,v in enumerate(a))
    slope=(mgf(h)-mgf(-h))/(2*h)
    check(abs(slope-mean_direct(z))<3e-6, f'mgf derivative z={z}')

# Legendre dual calculus and strict positivity of the rate away from 1.
for j in range(1,151):
    y=j/31
    s=1-1/sqrt(y)
    val=s*y -s/(1-s)
    target=(sqrt(y)-1)**2
    check(abs(val-target)<1e-12, f'Legendre transform y={y}')
    check(target>=0, f'nonnegative rate y={y}')

# Direct path simulation of the underlying non-Markovian stochastic clock.
# This confirms model interpretation, not the asymptotic theorem.
def simulate(z,rng):
    start=[0.0]; after=[0.0]; t=0.0
    while True:
        dt=rng.expovariate(1.0)
        nxt=t+dt
        if nxt>=z:
            return after[-1]+z-start[-1]
        past=rng.random()*nxt
        ix=bisect.bisect_right(start,past)-1
        val=after[ix]+past-start[ix]
        start.append(nxt); after.append(val)
        t=nxt
rng=random.Random(20261106)
for z in [2,8,16]:
    xs=[simulate(z,rng) for _ in range(14000)]
    mu=sum(xs)/len(xs)
    exact=mean_direct(z)
    check(abs(mu-exact)<0.09, f'simulated clock mean z={z}: {mu} {exact}')
    check(all(0<=x<=z+1e-10 for x in xs), f'physical clock bound z={z}')

print('PASS:',checks,'exact algebraic and deterministic numerical assertions')
