"""Exact rational tests for shuffling convex-order frontier.

Runs by `python verify.py` with Python 3.9+; no external packages.
These tests support the general algebraic proof but do not replace it.
"""
from fractions import Fraction as F
from itertools import permutations, product


def random_epoch(a, b, eta):
    outcomes = []
    for perm in permutations(range(len(a))):
        q, s = F(1), F(0)
        for j in perm:
            s = (1 - eta * a[j]) * s + eta * b[j]
            q = (1 - eta * a[j]) * q
        outcomes.append((q, s))
    assert all(q == outcomes[0][0] for q, _ in outcomes)
    return outcomes[0][0], tuple(s for _, s in outcomes)


def distribution(B, A, K, reshuffle):
    coeff = [A ** j for j in range(K)]
    S = sum(coeff, F(0))
    if reshuffle:
        return [sum((coeff[j] * bs[j] for j in range(K)), F(0)) for bs in product(B, repeat=K)]
    return [S * b for b in B]


def mean(xs):
    return sum(xs, F(0)) / len(xs)


def second_central(xs):
    m = mean(xs)
    return mean([(x - m) ** 2 for x in xs])


def convex_order(lhs, rhs):
    assert mean(lhs) == mean(rhs)
    thresholds = set(lhs) | set(rhs)
    for t in thresholds:
        a = mean([max(F(0), x - t) for x in lhs])
        b = mean([max(F(0), y - t) for y in rhs])
        if a > b:
            return False
    return True


def check():
    cases = 0
    a = (F(2), F(1))
    b = (F(2), F(-1))
    for eta in (F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(4, 5), F(5, 4)):
        A, B = random_epoch(a, b, eta)
        assert abs(A) < 1
        assert len(set(B)) > 1
        for k in range(1, 8):
            rr = distribution(B, A, k, True)
            so = distribution(B, A, k, False)
            assert mean(rr) == mean(so)
            if k == 1 or A == 0:
                assert convex_order(rr, so) and convex_order(so, rr)
            elif A > 0:
                assert convex_order(rr, so)
                assert second_central(rr) < second_central(so)
            else:
                assert convex_order(so, rr)
                assert second_central(so) < second_central(rr)
            cases += 1
    A, B = random_epoch(a, b, F(3, 4))
    assert A == -F(1, 8) and set(B) == {-F(3, 8), F(15, 8)}
    v = second_central(B)
    assert v == F(81, 64)
    v_rr = v / (1 - A * A)
    v_so = v / ((1 - A)**2)
    assert v_rr == F(9, 7) and v_so == F(1)
    assert (v_rr - v_so) * F(3, 4) == F(3, 14)

    # Three-component, unequal curvatures, with a zero or negative epoch product.
    for a3, b3, eta in [
        ((F(1),F(3),F(2)), (F(2),F(-1),F(4)), F(3,5)),
        ((F(2),F(3),F(4)), (F(1),F(-2),F(1)), F(1,3)),
    ]:
        A, B = random_epoch(a3, b3, eta)
        assert abs(A) < 1
        for k in range(1,5):
            rr=distribution(B,A,k,True); so=distribution(B,A,k,False)
            if k==1 or A==0:
                assert convex_order(rr,so) and convex_order(so,rr)
            elif A>0: assert convex_order(rr,so)
            else: assert convex_order(so,rr)
            cases+=1
    print('PASS:',cases,'exact finite-horizon distribution comparisons; stationary witness checked')

if __name__ == '__main__':
    check()
