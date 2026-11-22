"""Standalone numerical checks for the two-design lateral-drift crossover theorem.

Run with: python check_crossing.py
Only the Python standard library is required. Tests support but do not replace proof.
"""
import math
import random

SQRT_PI = math.sqrt(math.pi)
SQRT2 = math.sqrt(2.0)

def log_erfc(z):
    """Stable logarithm of the real complementary error function, z>=0."""
    assert z >= 0.0
    if z <= 20.0:
        return math.log(math.erfc(z))
    inv = 1.0/(2.0*z*z)
    # Alternating asymptotic series through relative order z**(-10).
    poly = 1.0 - inv + 3.0*inv**2 - 15.0*inv**3 + 105.0*inv**4 - 945.0*inv**5
    return -z*z - math.log(SQRT_PI*z) + math.log(poly)

def log_prob(L,a,b):
    assert L>0 and a>=0 and b>0
    return -a*L + log_erfc(b/math.sqrt(L)) - math.log(2.0)

def log_ratio(L, a1,b1,a2,b2):
    return log_prob(L,a1,b1)-log_prob(L,a2,b2)

def root(delta,b1,b2):
    assert delta>0 and 0<b1<b2
    lo,hi=1e-8,1.0
    while log_ratio(hi,delta,b1,0,b2)>0:
        hi *= 2.0
        assert hi < 1e10
    assert log_ratio(lo,delta,b1,0,b2)>0
    for _ in range(90):
        mid=(lo+hi)/2
        if log_ratio(mid,delta,b1,0,b2)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def check():
    count=0
    rng=random.Random(3714473)
    for _ in range(1000):
        b1=rng.uniform(.25,1.75)
        b2=b1+rng.uniform(.1,1.75)
        d=10**rng.uniform(-2,1.5)
        x=root(d,b1,b2)
        assert abs(log_ratio(x,d,b1,0,b2))<2e-9
        assert log_ratio(x*.7,d,b1,0,b2)>0
        assert log_ratio(x*1.3,d,b1,0,b2)<0
        # Full strict ranking from upstream to downstream sampled at log-spaced distances.
        xs=[x*10**(-1.2+2.4*k/34) for k in range(35)]
        ys=[log_ratio(v,d,b1,0,b2) for v in xs]
        assert all(ys[k] > ys[k+1] for k in range(34))
        # Increase mortality gap: crossover moves upstream.
        assert root(1.01*d,b1,b2)<x
        count+=38
    for d in [1e-7,1e-6,1e-5,1e-4]:
        x=root(d,1.,2.)
        asym=(2./(SQRT_PI*d))**(2./3.)
        assert abs(x/asym-1)<.08
        count+=1
    for d in [1e3,1e4,1e5,1e6]:
        x=root(d,1.,2.)
        asym=math.sqrt(3./d)
        assert abs(x/asym-1)<.05
        count+=1
    # Numerical example with genuinely nonvanishing access at its crossover.
    xc=root(.4,1,2)
    assert abs(xc-3.265197129)<5e-7
    p1=math.exp(log_prob(xc,.5,1.))
    p2=math.exp(log_prob(xc,.1,2.))
    assert abs(p1-p2)<1e-10 and .035<p1<.06
    print(f"PASS: {count+3} inequalities, crossovers, asymptotic checks, and concrete examples")
    print(f"Example: L*={xc:.12f}; common success probability={p1:.12f}")

if __name__=='__main__': check()
