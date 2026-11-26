"""Finite exact checks for the positive-input, two-objective cooling theorem."""
from fractions import Fraction as F
from itertools import product


def state(a, k, h, b, y):
    # Without loss of generality scale H1 to 1 and H2 to h.
    a1, a2 = a + b - y, a + y
    d = a1 * a2 + k * (a1 + a2)
    return d, (a2 + k + k*h)/d, (k + (a1+k)*h)/d


def main():
    vals = (F(1, 4), F(1), F(4))
    hs = (F(1, 9), F(1, 4), F(2, 3), F(9, 10))
    cases = 0
    for a, k, h in product(vals, vals, hs):
        bp = (1-h)*a/h
        for b in (bp/4, bp/2, bp, bp*2, bp*4):
            yp = max(F(0), (h*b-(1-h)*a)/(1+h))
            d, t1, t2 = state(a, k, h, b, yp)
            if b >= bp:
                assert t1 == t2
                assert t1*(b-2*yp) == 1-h
                assert t1*(2*yp-b)/d == -(1-h)/d < 0
            expected = max(t1, t2)
            for i in range(21):
                y = b*F(i, 20)
                d, x1, x2 = state(a, k, h, b, y)
                if y != yp:
                    assert max(x1, x2) > expected
                assert (a+b-y+k)*x1-k*x2 == 1
                assert (a+y+k)*x2-k*x1 == h
            cases += 1

    _, t10, t20 = state(F(1), F(1), F(1,4), F(2), F(0))
    _, t11, t21 = state(F(1), F(1), F(1,4), F(2), F(1,5))
    assert t10+t20 == F(17,28) and t11+t21 == F(55,92)
    assert t10 == F(9,28) and t11 == F(245,736)
    assert t11+t21 < t10+t20 and t11 > t10
    print(f'{cases} exact rational budget cases and the strict objective comparison passed')


if __name__ == '__main__':
    main()
