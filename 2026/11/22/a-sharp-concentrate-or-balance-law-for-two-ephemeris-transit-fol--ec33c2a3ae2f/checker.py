"""Exact-rational diagnostic tests for the two-phase two-transit allocation theorem.

Requires only Python 3 standard library. The analytical proof is in RESULT.md;
finite tests do not prove its all-parameter statements.
"""
from fractions import Fraction
from math import exp


def tail2(n, p):
    if n < 2:
        return Fraction(0)
    q = 1 - p
    return 1 - q**n - n*p*q**(n-1)


def score(n, j, p):
    return tail2(j, p) + tail2(n-j, p)


def critical_polynomial(n, q):
    if n % 2 == 0:
        m = n // 2
        return 2*m*q**(m-1) - sum(q**k for k in range(m))
    m = n // 2
    return sum((k+1)*q**k for k in range(m, 2*m)) - sum((k+1)*q**k for k in range(m-1))


def run():
    passed = 0
    for n in range(4, 75):
        m = n//2
        for den in range(2, 30):
            for num in range(1, den):
                p = Fraction(num, den)
                q = 1-p
                scores = [score(n, j, p) for j in range(n+1)]
                best = max(scores)
                assert best == max(scores[0], scores[m]); passed += 1
                # No interior split except the balanced pair can maximize.
                for j in range(1, n):
                    if j not in {m, n-m}:
                        assert scores[j] < best; passed += 1
                diff = scores[0] - scores[m]
                poly = critical_polynomial(n, q)
                assert (diff > 0) == (poly > 0); passed += 1
                assert (diff < 0) == (poly < 0); passed += 1
                # Strictly unimodal first differences: negativity then positivity.
                diffs = [scores[j+1]-scores[j] for j in range(m)]
                assert diffs[0] < 0; passed += 1
                seen_pos = False
                for d in diffs[1:]:
                    if d > 0:
                        seen_pos = True
                    if seen_pos:
                        assert d >= 0
                    passed += 1
    assert critical_polynomial(4, Fraction(1,3)) == 0; passed += 1
    assert score(4, 0, Fraction(2,3)) == score(4, 2, Fraction(2,3)); passed += 1
    # Root brackets and large-budget limit by bisection (diagnostic only).
    ylo, yhi = 1.25, 1.27
    assert exp(ylo) < 1 + 2*ylo and exp(yhi) > 1 + 2*yhi; passed += 1
    for n in [4,5,6,7,10,21,50,101,400,1000]:
        lo, hi = 0.0, 1.0
        for _ in range(65):
            p = (lo+hi)/2
            q = 1-p
            pol = critical_polynomial(n,q)
            # For all n, sign positive for small p / large q.
            if pol > 0: lo=p
            else: hi=p
        pcrit = (lo+hi)/2
        assert 0<pcrit<1; passed += 1
        if n>=400:
            assert abs(n*pcrit-2.51286241725234) < 0.05; passed += 1
    print(f"PASS: {passed} exact-rational and asymptotic diagnostic assertions")


if __name__ == '__main__':
    run()
