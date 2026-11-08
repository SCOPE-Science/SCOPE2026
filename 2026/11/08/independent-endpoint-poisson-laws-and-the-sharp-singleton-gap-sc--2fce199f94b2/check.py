#!/usr/bin/env python3
"""Exact tests for singleton locations in uniformly random set partitions."""
from itertools import combinations
from math import comb, exp, factorial, log
from fractions import Fraction

def lambert_w(x):
    w = log(x) - log(max(log(x), 1.01)) if x > 3 else 0.5
    for _ in range(20):
        t = exp(w)
        w -= (w*t - x)/(t*(w+1))
    return w

def bells(n):
    out = [1]
    for m in range(n):
        out.append(sum(comb(m, j) * out[j] for j in range(m + 1)))
    return out

def rgs(n):
    """Generate all restricted-growth strings, one per set partition."""
    if not n:
        yield ()
        return
    def extend(prefix, largest):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for block in range(largest + 2):
            prefix.append(block)
            yield from extend(prefix, max(block, largest))
            prefix.pop()
    yield from extend([0], 0)

def singleton_mask(rg):
    count = [0] * (max(rg) + 1)
    for x in rg:
        count[x] += 1
    return sum((1 << i) for i, x in enumerate(rg) if count[x] == 1)

def falling(x, k):
    z = 1
    for j in range(k):
        z *= x - j
    return z

def run():
    exact_cases = 0
    bell = bells(600)
    singleton_free = [1]
    for k in range(600):
        singleton_free.append(bell[k]-singleton_free[k])
    for n in range(1, 9):
        masks = [singleton_mask(p) for p in rgs(n)]
        assert len(masks) == bell[n]
        exact_cases += 1
        # Mean terminal-singleton gap: count every partition independently.
        observed = sum(n if not mask else n - mask.bit_length()
                       for mask in masks)
        derived = sum((Fraction(comb(n,s)*singleton_free[n-s],1)
                       * Fraction(n-s,s+1)) for s in range(n+1))
        assert Fraction(observed, bell[n]) == derived/bell[n]
        exact_cases += 1
        # Every prescribed marked set of r distinct labels must be singleton
        # in exactly B(n-r) partitions.
        for r in range(min(n, 4) + 1):
            for subset in combinations(range(n), r):
                q = sum(1 << i for i in subset)
                lhs = sum((m & q) == q for m in masks)
                assert lhs == bell[n-r], (n, subset, lhs, bell[n-r])
                exact_cases += 1
        # Every pair of nonoverlapping test windows has the joint
        # falling-factorial moment given by the Bell ratio identity.
        split = n // 2
        A = list(range(split))
        C = list(range(split, n))
        x = [int((m & sum(1 << i for i in A)).bit_count()) for m in masks]
        y = [int((m & sum(1 << i for i in C)).bit_count()) for m in masks]
        for r in range(min(3, len(A)) + 1):
            for s in range(min(3, len(C)) + 1):
                lhs = sum(falling(u,r)*falling(v,s) for u,v in zip(x,y))
                rhs = falling(len(A),r) * falling(len(C),s) * bell[n-r-s]
                assert lhs == rhs, (n,r,s,lhs,rhs)
                exact_cases += 1

    for n in range(2, 601):
        # Pairwise singleton indicators are strictly positively correlated.
        assert bell[n]*bell[n-2] > bell[n-1]**2
        exact_cases += 1

    for n in (50,100,200,400,600):
        a = bell[n-1]/bell[n]
        assert abs(n*a - lambert_w(n)) < .06
        for r in (2,3,4):
            ratio = (bell[n-r] * bell[n]**(r-1) / bell[n-1]**r)
            assert abs(ratio - 1) < (7*r*r/n)
            exact_cases += 1
        # Exact union-void probability from inclusion-exclusion:
        m = min(n,round(1/a))
        count = sum((-1)**k * comb(m,k) * bell[n-k] for k in range(m+1))
        assert 0 <= count <= bell[n]
        assert abs(count/bell[n] - exp(-1)) < .03
        exact_cases += 1
        m2 = min(n,round(2/a))
        count2 = sum((-1)**k * comb(m2,k) * bell[n-k] for k in range(m2+1))
        assert 0 <= count2 <= bell[n]
        assert abs(count2/bell[n] - exp(-2)) < .03
        exact_cases += 1
    for n in (50,100,200,400,600):
        # Comparison of exact average gap to the predicted Bell-ratio scale.
        numerator = sum((Fraction(comb(n,s)*singleton_free[n-s],1)
                        * Fraction(n-s,s+1)) for s in range(n+1))
        scaled_mean = float(numerator * Fraction(bell[n-1], bell[n]*bell[n]))
        assert .7 < scaled_mean < 1
        if n >= 200:
            assert scaled_mean > .96
        exact_cases += 1
    print(f"PASS: {exact_cases} exact identities/inequalities and finite-scale diagnostics")

if __name__ == "__main__":
    run()
