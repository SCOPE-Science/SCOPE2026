"""Exact checks of stationary second moments for partially averaging star gossip.

Requires Python 3.10+ and SymPy. Run: python verify.py
All calculations use rational arithmetic; no simulation is used.
"""
from fractions import Fraction as F
import sympy as s


def full_labelled_covariances(a, b, k, theta):
    """Solve every pair moment equation, without symmetry reduction."""
    h = a + b
    mean = F(b, h)
    n = k + 1  # regular centre (0), regular leaves (1,...,k)
    nbrs = ([[(j, None) for j in range(1, n)]
             + [(None, -mean)] * a + [(None, 1 - mean)] * b]
            + [[(0, None)] for _ in range(k)])
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    loc = {pair: q for q, pair in enumerate(pairs)}
    matrix = s.zeros(len(pairs))
    rhs = s.zeros(len(pairs), 1)

    def add(row, i, j, coeff):
        if i > j:
            i, j = j, i
        matrix[row, loc[(i, j)]] += s.Rational(coeff.numerator, coeff.denominator)

    for row, (i, j) in enumerate(pairs):
        if i != j:
            add(row, i, j, -2 * theta)
            for src, other in ((i, j), (j, i)):
                for neigh, _ in nbrs[src]:
                    if neigh is not None:
                        add(row, neigh, other, theta / F(len(nbrs[src])))
        else:
            add(row, i, i, -2 * theta + theta * theta)
            for neigh, centred_fixed in nbrs[i]:
                if neigh is not None:
                    add(row, i, neigh, 2 * theta * (1 - theta) / F(len(nbrs[i])))
                    add(row, neigh, neigh, theta * theta / F(len(nbrs[i])))
                else:
                    const = theta * theta * centred_fixed * centred_fixed / F(len(nbrs[i]))
                    rhs[row, 0] -= s.Rational(const.numerator, const.denominator)
    sol = matrix.inv() * rhs
    return {pair: F(sol[loc[pair]]) for pair in pairs}


def closed(a, b, k, theta):
    h = a + b
    q = F(a * b, h * h)
    D = (k * (theta**2 - 8 * theta + 8)
         + h * (2 * theta**2 - 8 * theta + 8) + 2 * theta - theta**2)
    centre = q * theta * ((k + 2 * h) * (2 - theta) + theta) / D
    leaf = q * theta * (k * (2 - theta) + 2 * h + theta) / D
    offdiag = q * theta * ((k + h) * (2 - theta) + theta) / D
    return centre, leaf, offdiag


def main():
    checks = 0
    # The full labelled equations independently test the symmetry reduction.
    for a, b in [(1, 1), (1, 2), (2, 2), (1, 4)]:
        for k in (2, 3, 4):
            for theta in (F(1, 4), F(1, 2), F(2, 3), F(1)):
                direct = full_labelled_covariances(a, b, k, theta)
                centre, leaf, offdiag = closed(a, b, k, theta)
                assert direct[(0, 0)] == centre
                checks += 1
                for i in range(1, k + 1):
                    assert direct[(i, i)] == leaf
                    checks += 1
                    assert direct[(0, i)] == offdiag
                    checks += 1
                for i in range(1, k + 1):
                    for j in range(i + 1, k + 1):
                        assert direct[(i, j)] == offdiag
                        checks += 1

    # Independently check exact neighbouring-size differences, including signs.
    for h in range(2, 20):
        for theta in (F(1, 20), F(1, 4), F(1, 2), F(3, 4), F(19, 20), F(1)):
            c0 = closed(1, h - 1, 2, theta)[2]
            c1 = closed(1, h - 1, 3, theta)[2]
            f = h * theta**2 - (2 * h + 4) * theta + 4
            assert ((c1 > c0) - (c1 < c0)) == -((f > 0) - (f < 0))
            checks += 1

    k, h, t, q = s.symbols('k h t q', positive=True)
    D = k * (t**2 - 8*t + 8) + h * (2*t**2 - 8*t + 8) + 2*t - t**2
    Vc = q*t*((k+2*h)*(2-t)+t)/D
    Vl = q*t*(k*(2-t)+2*h+t)/D
    C = q*t*((k+h)*(2-t)+t)/D
    assert s.simplify((C.subs(k,k+1)-C)*D*D.subs(k,k+1)
                      +q*t**2*(h*t**2-(2*h+4)*t+4)) == 0
    checks += 1
    assert s.simplify((Vc-Vl)*D - 2*h*q*t*(1-t)) == 0
    checks += 1
    assert s.simplify((Vl-C)*D - h*q*t*t) == 0
    checks += 1
    assert s.simplify((C/Vl).diff(k) - h*t*(2-t)/(k*(2-t)+2*h+t)**2) == 0
    checks += 1
    print(f'PASS: {checks} exact labelled and symbolic assertions')


if __name__ == '__main__':
    main()
