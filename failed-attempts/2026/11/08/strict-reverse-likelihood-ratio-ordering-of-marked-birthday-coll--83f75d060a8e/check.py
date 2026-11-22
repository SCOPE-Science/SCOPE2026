"""Reproducible exact checks for the marked nonuniform birthday collision theorem.

Execute with Python 3 standard library: python3 check.py
Finite checks supplement, not replace, the proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def elementary_symmetric(xs):
    e = [Fraction(1)] + [Fraction(0)] * len(xs)
    for x in xs:
        for k in range(len(xs), 0, -1):
            e[k] += x * e[k - 1]
    return e


def predicted_joint(p):
    m = len(p)
    ans = {}
    for i, a in enumerate(p):
        e = elementary_symmetric(p[:i] + p[i + 1:])
        for t in range(2, m + 2):
            ans[t, i] = Fraction(factorial(t-1)) * a*a * e[t-2]
    return ans


def direct_joint(p):
    m = len(p)
    result = {(t, i): Fraction(0) for t in range(2, m+2) for i in range(m)}
    for t in range(2, m+2):
        for seq in product(range(m), repeat=t):
            if len(set(seq[:-1])) != t-1 or seq[-1] not in seq[:-1]:
                continue
            mass = Fraction(1)
            for j in seq:
                mass *= p[j]
            result[t, seq[-1]] += mass
    return result


def check(p):
    a = predicted_joint(p)
    m = len(p)
    assert sum(a.values()) == 1
    assertions = 1
    for i in range(m):
        assert all(a[t, i] > 0 for t in range(2, m+2))
        assertions += m
    for i in range(m):
        for j in range(m):
            if i == j: continue
            if p[i] > p[j]:
                # Every time slice respects the ordering of category probabilities.
                for t in range(2, m+2):
                    assert a[t, i] > a[t, j]
                    assertions += 1
                # Reverse total positivity / strict likelihood-ratio order.
                for t in range(2, m+2):
                    for u in range(t+1, m+2):
                        assert a[t, i]*a[u, j] > a[u, i]*a[t, j]
                        assertions += 1
                si = sum(a[t, i] for t in range(2, m+2))
                sj = sum(a[t, j] for t in range(2, m+2))
                # Earlier collision under the higher-probability repeated label.
                for t in range(2, m+1):
                    assert sum(a[u, i] for u in range(2, t+1))/si > sum(a[u, j] for u in range(2,t+1))/sj
                    assertions += 1
            elif p[i] == p[j]:
                for t in range(2, m+2):
                    assert a[t, i] == a[t, j]
                    assertions += 1
    return assertions


def main():
    checks = 0
    for weights in ((3,1), (5,3,2), (5,4,2,1), (5,4,3,2,1)):
        sm = sum(weights)
        p = tuple(Fraction(w, sm) for w in weights)
        assert direct_joint(p) == predicted_joint(p)
        checks += len(p)*len(p)
        checks += check(p)
    # Sweep all positive integer weight vectors of bounded sum, with exact fractions.
    vectors = 0
    for m in range(2,7):
        for weights in product(range(1,5), repeat=m):
            if sum(weights) > m+5: continue
            sm=sum(weights)
            p=tuple(Fraction(w, sm) for w in weights)
            checks += check(p)
            vectors += 1
    # Explicit illustrative case.
    p = (Fraction(1,2), Fraction(1,3), Fraction(1,6))
    a = predicted_joint(p)
    for i in (0,2):
        s=sum(a[t,i] for t in range(2,5))
        print('type',i+1,'joint',[str(a[t,i]) for t in range(2,5)],'conditional',[str(a[t,i]/s) for t in range(2,5)])
    print('PASS:', checks, 'exact assertions over', vectors, 'weight vectors plus 4 independent enumerations')

if __name__ == '__main__':
    main()
