"""Standalone standard-library verification for a two-option temporal voting theorem.
All computations here are finite checks supplementing the analytic proof.
"""
from itertools import product
from math import comb, lgamma, exp, log, floor, erf, sqrt


def structural(a, b, c, L, count_A):
    n = a + b + c
    lo = L * a // n
    hi = L - (L * b // n)
    return lo <= count_A <= hi


def full_axioms(a, b, c, outcome):
    """Directly implement Definitions 2.1/2.2 (static approvals)."""
    approvals = [{0}] * a + [{1}] * b + [{0, 1}] * c
    n = len(approvals)
    L = len(outcome)
    T = outcome.count(0)
    vals = [sum(1 for choice in outcome if choice in appr) for appr in approvals]
    jr = pjr = ejr = ejrp = True
    for mask in range(1, 1 << n):
        S = [i for i in range(n) if mask >> i & 1]
        union = set().union(*(approvals[i] for i in S))
        intersection = set(approvals[S[0]])
        for i in S[1:]:
            intersection.intersection_update(approvals[i])
        total_satisfaction = sum(choice in union for choice in outcome)
        if intersection:
            # Under static approvals the group agrees on all L rounds.
            q = L * len(S) // n
            jr &= total_satisfaction >= min(1, q)
            pjr &= total_satisfaction >= q
            ejr &= any(vals[i] >= q for i in S)
        # Direct EJR+ condition using all possible (sigma,tau) and round r.
        if intersection:
            max_support = max(sum(candidate in approvals[i] for i in S)
                              for candidate in (0, 1))
            for sigma in range(1, max_support + 1):
                for tau in range(1, L + 1):
                    q = tau * sigma // n
                    if any(vals[i] >= q for i in S):
                        continue
                    if any(choice not in intersection for choice in outcome):
                        ejrp = False
    return jr, pjr, ejr, ejrp


checks = 0
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(3):
            for L in range(1, 8):
                for seq in product((0, 1), repeat=L):
                    jr, pjr, ejr, ejrp = full_axioms(a, b, c, seq)
                    target = structural(a, b, c, L, seq.count(0))
                    assert target == pjr == ejr == ejrp, (a, b, c, L, seq, target, pjr, ejr, ejrp)
                    checks += 1
print('Direct axiom checks:', checks)

# Finite exact event sums, deterministic sequence enumeration, and optimized p.
from fractions import Fraction
for a, b, c in product(range(1, 4), range(1, 4), range(3)):
    for L in range(1, 10):
        low = L * a // (a + b + c)
        high = L - L * b // (a + b + c)
        for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
            v = sum(Fraction(comb(L, j)) * p**j * (1-p)**(L-j)
                    for j in range(low, high+1))
            direct = sum(p**seq.count(0) * (1-p)**(L-seq.count(0))
                         for seq in product((0, 1), repeat=L)
                         if structural(a, b, c, L, seq.count(0)))
            assert v == direct
            checks += 1
        if low > 0 and high < L:
            coef1 = comb(L-1, low-1)
            coef2 = comb(L-1, high)
            pstar = 1/(1+(coef2/coef1)**(1/(high-low+1)))
            def f(p):
                return sum(comb(L,j)*p**j*(1-p)**(L-j) for j in range(low, high+1))
            assert f(pstar) + 1e-12 >= max(f(max(0, pstar-0.03)), f(min(1,pstar+0.03)))
            checks += 1
print('Total enumerative and optimum checks:', checks)

# The one-flexible-voter critical window at L=n^2.
for n in (21, 41, 81, 161):
    assert n % 2
    m=(n-1)//2
    L=n*n
    lo=L*m//n
    hi=L-lo
    # Numerically stable central sum with exact integer bounds.
    prob=sum(exp(lgamma(L+1)-lgamma(j+1)-lgamma(L-j+1)-L*log(2))
             for j in range(lo,hi+1))
    limit=erf(1/sqrt(2))
    assert abs(prob-limit) < 5/sqrt(n), (n,prob,limit)
    print('critical-window n, probability, Gaussian limit:', n, round(prob,8), round(limit,8))
print('VERIFIED: all finite tests passed')
