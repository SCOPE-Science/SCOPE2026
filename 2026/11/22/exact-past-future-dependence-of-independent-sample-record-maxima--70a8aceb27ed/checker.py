"""Independent finite checks for the record-maximum dependence formulas.

Uses only the Python standard library. These checks complement an analytic proof;
finite enumeration and numerical integration do not prove the infinite assertions.
"""
from fractions import Fraction
from itertools import permutations
from math import exp
from random import Random

COUNT = 0


def verify(condition, label):
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1


def beta_exact_for_reciprocal(q):
    r = Fraction(1, q)
    t = (1 - r) ** q
    expected = r + r * (1 - r) * t / (1 + r)
    p_event = r + (1 - r) * t
    q_event = (1 - r) ** (q + 1) / (1 + r)
    overlap = q_event + (1 - r) * (1 - t)
    verify(expected == p_event - q_event, f"Neyman-Pearson event q={q}")
    verify(expected == 1 - overlap, f"overlap q={q}")
    verify(r < expected < 1, f"strict excess q={q}")
    return expected


def beta(r):
    t = (1-r)**(1/r)
    return r + r*(1-r)*t/(1+r)


def numerical_overlap(r, steps=120000):
    # Integrates the analytically derived vertical overlap integrand.
    h = 1.0 / steps
    return h * sum(min((1-r), ((j+0.5)*h)**r) for j in range(steps))


def empirical_beta(n, m, samples=110000):
    r=n/m
    t=(1-r)**(1/r)
    rng=Random(202611190000+n*101+m)
    p_event=q_event=0
    for _ in range(samples):
        observations=[rng.random() for _ in range(m)]
        x=max(observations[:n]); y=max(observations)
        u=x**n; v=y**m
        event=(x==y) or (v<t and u<v**r)
        p_event+=event
        uu=rng.random(); vv=rng.random()
        q_event += vv<t and uu<vv**r
    return (p_event-q_event)/samples


verify(beta_exact_for_reciprocal(2) == Fraction(13,24), "n=1 m=2 exact")
verify(beta_exact_for_reciprocal(3) == Fraction(31,81), "n=1 m=3 exact")
for q in range(2,71):
    beta_exact_for_reciprocal(q)

for m in range(2,9):
    perms=list(permutations(range(m)))
    for n in range(1,m):
        same=sum(p.index(m-1)<n for p in perms)
        verify(Fraction(same,len(perms))==Fraction(n,m),f"singular mass {n}/{m}")

for n,m in [(1,2),(1,3),(2,3),(2,5),(3,7),(5,19),(20,51),(1,201)]:
    r=n/m
    approximate=1-numerical_overlap(r)
    verify(abs(approximate-beta(r))<2e-6,f"integral beta {n}/{m}")

for n,m in [(1,2),(2,5),(5,9)]:
    estimate=empirical_beta(n,m)
    verify(abs(estimate-beta(n/m))<0.016,f"seeded empirical TV test {n}/{m}")

for m in [3,6,13,30]:
    for n in range(1,m):
        r=n/m
        b=beta(r)
        verify(0<r<b<1,f"bounds {n}/{m}")
        verify(1+(1-r)/(1+r)*(1-r)**(1/r) > 1,f"relative excess {n}/{m}")

for n in [1,2,7]:
    for m in [100,1000,10000]:
        r=n/m
        verify(abs(beta(r)/r-(1+exp(-1)))<0.07,f"small-r convergence {n}/{m}")

print(f"PASS: {COUNT} deterministic exact, finite-enumeration, quadrature and seeded checks")
