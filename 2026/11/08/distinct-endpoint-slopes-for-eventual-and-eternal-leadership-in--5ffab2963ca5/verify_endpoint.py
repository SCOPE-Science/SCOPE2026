#!/usr/bin/env python3
"""Independent finite-urn checks for endpoint leadership coefficients.

The analytic infinite-time theorem requires the argument in RESULT.md;
finite dynamic programming here is diagnostic, not an infinite proof.
"""
from fractions import Fraction
from math import log

checks = 0

def check(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def urn_prob(r, steps, ever):
    """Exact Pólya urn with root count r and challenger count one."""
    states = {(r, 1): Fraction(1)}
    hit = Fraction(0)
    for _ in range(steps):
        nxt = {}
        for (a, b), mass in states.items():
            for na, nb, prob in ((a+1, b, Fraction(a, a+b)),
                                 (a, b+1, Fraction(b, a+b))):
                w = mass * prob
                if ever and nb > na:
                    hit += w
                else:
                    nxt[(na, nb)] = nxt.get((na, nb), Fraction(0)) + w
        states = nxt
    if ever:
        return hit
    return sum((mass for (a, b), mass in states.items() if b > a), Fraction())


def g(r):
    # Stable absolutely convergent formula; remaining tail < 2^(-cutoff).
    return 2.0**(-r) + r*sum(2.0**(-k)/k for k in range(r+1, 150))

check(urn_prob(1,1,True) == Fraction(1,2), 'first tie-break')
check(urn_prob(2,2,True) == Fraction(1,6), 'two early challenger wins')
check(urn_prob(1,3,True) == Fraction(7,12), 'three-decision recursion')
check(abs(g(1)-log(2)) < 2e-14, 'beta/gambler integral r=1')

for r in range(1,13):
    check(0 < g(r) < 2.0**(1-r), f'sharp exponential domination {r}')
    check(abs(g(r)-(2.0**(-r) + r*sum(2.0**(-k)/k for k in range(r+1,180)))) < 1e-14,
          f'tail consistency {r}')
    prev = Fraction(0)
    for steps in (0,1,2,4,8,16,32):
        val = urn_prob(r,steps,True)
        check(prev <= val <= 1, f'monotone exact first-passage {r}:{steps}')
        check(float(val) <= g(r)+1e-12, f'finite vs infinite {r}:{steps}')
        prev = val
        last = urn_prob(r,steps,False)
        check(0 <= last <= val, f'fixed-time vs ever {r}:{steps}')

check(abs(sum(g(r) for r in range(1,90))-1.5) < 1e-12, 'sum of ever-overtake weights')
check(abs(sum(2.0**(-r) for r in range(1,90))-1.0) < 1e-12, 'sum of terminal-overtake weights')

# Exact first-order coefficients at a finite observation horizon: at first order
# only a single table opens, at an arrival j in {2,...,n}.
for n in (8, 16, 32):
    ce = sum((urn_prob(j-1,n-j,True) for j in range(2,n+1)),Fraction())
    cf = sum((urn_prob(j-1,n-j,False) for j in range(2,n+1)),Fraction())
    check(0 < cf <= ce < Fraction(3,2),f'finite horizon coefficients n={n}')
    print(f'n={n} derivative coefficients: eternal={float(ce):.10f}, fixed-time={float(cf):.10f}')

for j in (8,12,16,24,32):
    bound=2.0**(1-j)*(1+j/(j/4-1))
    check(bound>0 and bound<1, f'late-challenger bound J={j}')
    if j>8:
        prev=2.0**(1-(j-4))*(1+(j-4)/((j-4)/4-1))
        check(bound<prev,f'tail bound decays {j}')

# Independent model representation: enumerate every parent-choice history of a
# uniform recursive tree. Close exactly one edge and check, at each prefix,
# whether its detached descendant component strictly exceeds the root one.
from itertools import product
from math import factorial

def detached_size(parents, birth, time):
    ans=0
    for v in range(1,time+1):
        u=v
        while u>birth:
            u=parents[u]
        if u==birth:
            ans+=1
    return ans

for n in (4,5,6,7,8):
    choices=[range(1,j) for j in range(2,n+1)]
    ever_total=0
    final_total=0
    histories=0
    for seq in product(*choices):
        histories+=1
        parents=[0,0]+list(seq)
        for birth in range(2,n+1):
            seen=False
            for time in range(birth,n+1):
                if 2*detached_size(parents,birth,time)>time:
                    seen=True
            ever_total += int(seen)
            final_total += int(2*detached_size(parents,birth,n)>n)
    check(histories==factorial(n-1),f'exhaustive tree histories n={n}')
    e=Fraction(ever_total,histories)
    f=Fraction(final_total,histories)
    urn_e=sum((urn_prob(j-1,n-j,True) for j in range(2,n+1)),Fraction())
    urn_f=sum((urn_prob(j-1,n-j,False) for j in range(2,n+1)),Fraction())
    check(e==urn_e,f'original-tree vs Pólya ever loss n={n}')
    check(f==urn_f,f'original-tree vs Pólya terminal loss n={n}')

print(f'PASS {checks} exact/floating checks; limits from the written analytic proof')
