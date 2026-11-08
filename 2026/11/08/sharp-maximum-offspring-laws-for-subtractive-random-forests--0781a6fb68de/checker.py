"""Finite exact diagnostics for maximum offspring counts in a subtractive forest.

No finite enumeration is used as proof of the infinite-volume asymptotic theorem.
This checker uses a geometric lag law P(Z=j)=2**(-j) for j>=1.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1


def independent_marginal(n, vertex):
    """Exact Poisson-binomial law for offspring of a fixed positive vertex."""
    law = [Q(1)]
    for j in range(1, n - vertex + 1):
        p = Q(1, 2**j)
        nxt = [Q(0)] * (len(law) + 1)
        for d, a in enumerate(law):
            nxt[d] += a * (1-p)
            nxt[d+1] += a*p
        law = nxt
    return law


def enumerate_forest(n):
    # At vertex t, lag 0 stands for any jump >=t: a nonpositive parent.
    # Common denominator is 2**sum(t-1) over t=1,...,n.
    choices = []
    for t in range(1,n+1):
        ch = [(0, 1)]
        ch.extend((j, 2**(t-1-j)) for j in range(1,t))
        check(sum(w for _, w in ch) == 2**(t-1))
        choices.append(ch)
    den = 2**(n*(n-1)//2)
    maximum = [0]*n
    degrees = [[0]*n for _ in range(n+1)]
    total_weight = 0
    for outcome in product(*choices):
        ds = [0]*(n+1)
        w = 1
        for t,(lag,weight) in enumerate(outcome,1):
            w *= weight
            if lag:
                ds[t-lag] += 1
        total_weight += w
        maximum[max(ds)] += w
        for v in range(1,n+1):
            degrees[v][ds[v]] += w
    check(total_weight == den)
    check(sum(maximum) == den)
    for v in range(1,n+1):
        law = independent_marginal(n,v)
        for d in range(n):
            p = Q(degrees[v][d],den)
            check(p == (law[d] if d < len(law) else 0))
        check(sum(degrees[v]) == den)
    exact_mean_degree = sum((Q(1)-Q(1,2**(t-1))) for t in range(2,n+1))
    enumerated_mean = sum(sum(d*w for d,w in enumerate(degrees[v])) for v in range(1,n+1))
    check(Q(enumerated_mean,den) == exact_mean_degree)
    return maximum, den


def e_k_geo(k):
    # Euler's geometric elementary-symmetric-function identity.
    ans = Q(1,2**(k*(k+1)//2))
    for j in range(1,k+1):
        ans /= (1-Q(1,2**j))
    return ans

for n in range(2,9):
    histogram, den = enumerate_forest(n)
    for k in range(1,n):
        # Uniform marginal upper bound on max, and the first-k-successes lower witness.
        upper = min(Q(1),n*e_k_geo(k))
        lower = Q(1,2**(k*(k+1)//2)) if n >= k+1 else Q(0)
        tail = Q(sum(histogram[k:]),den)
        check(tail <= upper)
        check(tail >= lower)
    print(f'n={n}: exact max-degree probabilities {[str(Q(v,den)) for v in histogram if v]}')

for k in range(1,25):
    p = Q(1, 2**(k*(k+1)//2))
    upper = e_k_geo(k)
    check(p <= upper)
    check(upper/p < 4)

print(f'PASS {checks} exact assertions')
