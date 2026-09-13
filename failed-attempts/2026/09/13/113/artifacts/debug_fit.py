"""Debug k=2 fit failure: RANSAC-style degree-4 fit over many primes."""
import numpy as np
import sympy as sp
import itertools, sys
sys.path.insert(0, '.')
from chi_count import chi_at_p


def fit_on(pts, deg):
    xs = [sp.Integer(x) for x, y in pts[:deg + 1]]
    ys = [sp.Integer(y) for x, y in pts[:deg + 1]]
    V = sp.Matrix([[x ** j for j in range(deg + 1)] for x in xs])
    rhs = sp.Matrix(ys)
    try:
        coeff = V.LUsolve(rhs)
    except Exception as e:
        return None, str(e)
    return list(coeff), None


def evalc(coeff, x):
    return sum(c * (sp.Integer(x) ** j) for j, c in enumerate(coeff))


if __name__ == '__main__':
    l, k = 3, 2
    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    pts = [(p, chi_at_p(l, k, p, None)) for p in primes]
    for p, v in pts:
        print(p, v)
    deg = l + 1
    best = None
    for combo in itertools.combinations(range(len(pts)), deg + 1):
        sub = [pts[i] for i in combo]
        coeff, err = fit_on(sub, deg)
        if coeff is None:
            continue
        nagree = sum(1 for x, y in pts if evalc(coeff, x) == y)
        if best is None or nagree > best[0]:
            best = (nagree, combo, coeff)
    print('best agree:', best[0], 'combo:', [pts[i][0] for i in best[1]])
    print('coeff:', best[1] if False else best[2])
    bad = [x for x, y in pts if evalc(best[2], x) != y]
    print('disagreeing primes:', bad)
    # check expected: (t-1)(t-12)^3 = ?
    t = sp.Symbol('t')
    print('expected FULL:', sp.expand((t - 1) * (t - 12) ** 3))
