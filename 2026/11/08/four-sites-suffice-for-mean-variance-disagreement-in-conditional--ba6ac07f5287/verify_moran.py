"""Exact verification of conditional fixation-time moment rankings.

Requires Python 3 and SymPy. Uses the full set of mutant subsets, including
self-loops caused by same-type reproduction. Fractions are exact.
"""
from fractions import Fraction
import sympy as S


def transition_data(edges, n, fitness):
    """Return transient Q and one-step success vector b in subset order."""
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    r = fitness
    states = list(range(1, (1 << n) - 1))
    idx = {mask: t for t, mask in enumerate(states)}
    Q = S.zeros(len(states))
    b = S.zeros(len(states), 1)
    for ai, mask in enumerate(states):
        k = mask.bit_count()
        total = k * r + (n - k)
        for u in range(n):
            weight = (r if mask & (1 << u) else 1) / total
            for v in neighbors[u]:
                nm = mask if bool(mask & (1 << u)) == bool(mask & (1 << v)) else mask ^ (1 << v)
                p = weight / len(neighbors[u])
                if nm == (1 << n) - 1:
                    b[ai] += p
                elif nm:
                    Q[ai, idx[nm]] += p
    return states, Q, b


def moments(edges, n, r):
    states, Q, b = transition_data(edges, n, r)
    A = S.eye(len(states)) - Q
    h = A.inv() * b
    a = A.inv() * h
    z = A.inv() * (2 * a - h)
    out = {}
    for v in range(n):
        j = states.index(1 << v)
        mean = S.factor(a[j] / h[j])
        var = S.factor(z[j] / h[j] - mean**2)
        out[v] = (S.factor(h[j]), mean, var)
    return out


def check_small():
    r = S.symbols('r', positive=True)
    edge = [(0, 1), (1, 2)]
    z = moments(edge, 3, r)
    assert S.factor(z[1][1] - z[0][1] + 3 / (2 * r + 1)) == 0
    assert S.factor(z[1][2] - z[0][2] + 6 * (r + 2) / (2 * r + 1)**2) == 0
    assert S.factor(z[0][1] - 2*(5*r*r+8*r+5)/(2*r*r+r+2)) == 0
    assert S.factor(z[0][2] - 2*(24*r**4+91*r**3+148*r**2+91*r+24)/(2*r*r+r+2)**2) == 0
    tri = moments([(0,1),(0,2),(1,2)], 3, r)
    assert tri[0] == tri[1] == tri[2]
    k2 = moments([(0,1)], 2, r)
    assert k2[0] == k2[1]
    print('All 2- and 3-vertex connected graph cases verified symbolically.')


def check_diamond():
    edges = [(0,1), (0,2), (0,3), (1,2), (2,3)]
    d = moments(edges, 4, S.Integer(5))
    assert d[0] == d[2]
    assert d[1] == d[3]
    assert d[0] == (
        S.Rational(1122875,1488426),
        S.Rational(72659908801,8913687172),
        S.Rational(1954046189090893922205,79453819000277357584))
    assert d[1] == (
        S.Rational(422375,496142),
        S.Rational(6854218276,838231909),
        S.Rational(136482613376588448261,5621061866126274248))
    assert S.factor(d[0][1] - d[1][1]) == -S.Rational(3095643, 121414228)
    assert S.factor(d[0][2] - d[1][2]) == S.Rational(4612716655893867,14741414760835984)
    print('Four-vertex diamond exact success probabilities, means and variances verified.')


if __name__ == '__main__':
    check_small()
    check_diamond()
    print('PASS')
