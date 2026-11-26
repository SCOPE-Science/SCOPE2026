"""Finite exact and stochastic checks for a Sukhatme-weight Luce fixed-point theorem.

The infinite-size limit is proved separately; these tests only check finite identities.
Requires Python 3.9+ standard library.
"""
from fractions import Fraction
from itertools import permutations
from math import exp, log
from random import Random


def lu_expected(n):
    weights = [n - i for i in range(n)]
    total = Fraction(0)
    for order in permutations(range(1, n + 1)):
        rem = sum(weights)
        prob = Fraction(1)
        for label in order:
            w = weights[label-1]
            prob *= Fraction(w, rem)
            rem -= w
        fixed = sum(pos == label for pos, label in enumerate(order, 1))
        total += fixed * prob
    return total


def clock_expected(n):
    out = Fraction(0)
    for k in range(1, n + 1):
        # A polynomial in z and x.  z records clocks greater than t,
        # x=e^{-t}.  We need the coefficient of z^(k-1).
        pol = [dict() for _ in range(k)]
        pol[0][0] = 1
        for j in range(1, n + 1):
            if j == k:
                continue
            nxt = [dict() for _ in range(k)]
            for d, terms in enumerate(pol):
                for power, coefficient in terms.items():
                    nxt[d][power] = nxt[d].get(power, 0) + coefficient
                    nxt[d][power+j] = nxt[d].get(power+j, 0) - coefficient
                    if d + 1 < k:
                        nxt[d+1][power+j] = nxt[d+1].get(power+j, 0) + coefficient
            pol = nxt
        out += sum((Fraction(k*c, k+power) for power,c in pol[k-1].items()), Fraction(0))
    return out


def bernoulli_G_two_ways(n, t):
    p = [exp(-k*t) for k in range(1,n+1)]
    direct = 0.0
    for k in range(1,n+1):
        # coefficient P(sum_{j!=k}B_j=k-1) by truncated convolution
        coeff = [1.0] + [0.0]*(k-1)
        for j in range(1,n+1):
            if j == k:
                continue
            q = p[j-1]
            for s in range(k-1,0,-1):
                coeff[s] = coeff[s]*(1-q)+coeff[s-1]*q
            coeff[0] *= (1-q)
        direct += k*p[k-1]*coeff[k-1]
    alt = 0.0
    for mask in range(1<<n):
        prob = 1.0
        s = mask.bit_count()
        for j, pj in enumerate(p):
            prob *= pj if mask & (1<<j) else (1-pj)
        if s > 0 and mask & (1<<(s-1)):
            alt += prob * s*p[s-1]
        if s < n and not (mask & (1<<s)):
            alt += prob * (s+1)*p[s]
    return direct,alt


def run():
    checks = 0
    for n in range(1,8):
        a, b = lu_expected(n), clock_expected(n)
        assert a == b, (n,a,b)
        checks += 1
        print(f'n={n}, exact expected fixed points={a}, decimal={float(a):.12f}')
    for n in range(1,9):
        for t in (0.04,0.2,0.7,1.3):
            a,b=bernoulli_G_two_ways(n,t)
            assert abs(a-b)<1e-12*(1+abs(a)), (n,t,a,b)
            checks+=1
    print(f'Exact rational agreements and independent Bernoulli integrand checks: {checks} passed')
    # Diagnostic only: no finite simulation is used as a proof of asymptotics.
    rng=Random(20261029)
    for n, rep in ((500,1200),(2000,600),(8000,250)):
        tot=0
        for _ in range(rep):
            times = [(rng.expovariate(k),k) for k in range(1,n+1)]
            times.sort(reverse=True)
            tot += sum(rank==k for rank,(_,k) in enumerate(times,1))
        avg=tot/rep
        print(f'Monte Carlo n={n}, repeats={rep}, mean={avg:.6f}, mean/log(n)={avg/log(n):.6f}, limit={1/exp(1):.6f}')
    return checks

if __name__=='__main__':
    print('Checks run:',run())
