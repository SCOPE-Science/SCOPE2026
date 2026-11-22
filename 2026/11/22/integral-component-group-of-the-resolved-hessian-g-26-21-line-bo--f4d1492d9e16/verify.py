#!/usr/bin/env python3
"""Exact arithmetic reconstruction of the 21-line Hessian boundary and its graph group.

Requires Python 3.10+ and SymPy. All geometry uses Q(omega), omega^2+omega+1=0.
No numerical root approximation is involved.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import prod
import sympy as S

F = Fraction

def E(a=0, b=0):
    return (F(a), F(b))

zero, one, omega, omega2 = E(), E(1), E(0, 1), E(-1, -1)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def minus(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, minus(y))

def mult(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)

def inverse(x):
    a, b = x
    norm = a*a-a*b+b*b
    assert norm
    return ((a-b)/norm, -b/norm)

def divide(x, y):
    return mult(x, inverse(y))

def cross(x, y):
    return (sub(mult(x[1], y[2]), mult(x[2], y[1])),
            sub(mult(x[2], y[0]), mult(x[0], y[2])),
            sub(mult(x[0], y[1]), mult(x[1], y[0])))

def projective_key(p):
    leading = next(x for x in p if x != zero)
    return tuple(divide(x, leading) for x in p)

# The Hesse twelve-line block and the nine dual-Hesse mirrors.
lines = [(one, zero, zero), (zero, one, zero), (zero, zero, one)]
for u, v in [(one, one), (omega, omega2), (omega2, omega),
             (omega, one), (omega2, omega2), (one, omega),
             (omega2, one), (omega, omega), (one, omega2)]:
    lines.append((one, u, v))
for w in (one, omega, omega2):
    lines.extend(((one, minus(w), zero),
                  (one, zero, minus(w)),
                  (zero, one, minus(w))))
assert len(lines) == len({projective_key(x) for x in lines}) == 21

points = {}
for i, j in combinations(range(21), 2):
    point = projective_key(cross(lines[i], lines[j]))
    points.setdefault(point, set()).update((i, j))
profile = Counter(len(v) for v in points.values())
assert profile == Counter({2: 36, 4: 9, 5: 12}), profile
assert sum(k*(k-1)//2*v for k, v in profile.items()) == 210
multiple_points = sorted((tuple(sorted(v)) for v in points.values() if len(v) >= 3))
double_points = sorted((tuple(sorted(v)) for v in points.values() if len(v) == 2))
assert len(multiple_points) == 21
edges = list(double_points)
for i, point in enumerate(multiple_points):
    for j in point:
        edges.append((j, 21 + i))
assert len(edges) == 132

laplacian = S.zeros(42, 42)
for u, v in edges:
    laplacian[u, u] += 1
    laplacian[v, v] += 1
    laplacian[u, v] -= 1
    laplacian[v, u] -= 1
assert Counter(int(laplacian[i, i]) for i in range(42)) == Counter({8: 21, 5: 12, 4: 9})
assert len(edges) - laplacian.rows + 1 == 91

# Matrix-tree via rational Schur complement of the exceptional-vertex diagonal.
root = 20
root_indices = [i for i in range(42) if i != root]
reduced = laplacian.extract(root_indices, root_indices)
B = reduced[:20, 20:]
exceptional_degrees = [int(reduced[i, i]) for i in range(20, 41)]
block = reduced[:20, :20] - B * S.diag(*(S.Rational(1, x) for x in exceptional_degrees)) * B.T
order = prod(exceptional_degrees) * block.det(method='domain-ge')
assert order.q == 1
order = int(order)
prime_orders = {2: 8, 3: 13, 5: 8, 7: 1, 67: 8}
assert S.factorint(order) == prime_orders

# Independent characteristic-polynomial consistency check.
t = S.Symbol('t')
expected_poly = (t*(t-9)**3*(t-4)**3*(t**3-25*t**2+188*t-392)
                 *(t**4-25*t**3+218*t**2-788*t+1005)**8)
assert S.expand(laplacian.charpoly(t).as_expr() - expected_poly) == 0
assert S.diff(expected_poly, t).subs(t, 0) * (-1)**41 // 42 == order

# Elementary divisors computed by exact row/column elimination modulo p^k.
# A pivot of minimum p-valuation in the trailing block divides all its entries
# p-adically. After its unit part is inverted, clear the pivot column and
# iterate; no floating point or unproved finite search is used.
def valuation(x, p, bound):
    if not x:
        return bound
    count = 0
    while x % p == 0:
        x //= p
        count += 1
    return min(count, bound)

def local_smith(matrix, p, exponent_bound):
    modulus = p ** exponent_bound
    n = matrix.rows
    data = [[int(z) % modulus for z in row] for row in matrix.tolist()]
    factors = []
    for h in range(n):
        best = (exponent_bound, None, None)
        for i in range(h, n):
            for j in range(h, n):
                v = valuation(data[i][j], p, exponent_bound)
                if v < best[0]:
                    best = v, i, j
                if v == 0:
                    break
            if best[0] == 0:
                break
        v, i, j = best
        if i is None:
            factors += [exponent_bound] * (n - h)
            break
        data[h], data[i] = data[i], data[h]
        for row in data:
            row[h], row[j] = row[j], row[h]
        pivot_power = p ** v
        assert data[h][h] % pivot_power == 0
        unit = data[h][h] // pivot_power
        reduced_modulus = p ** (exponent_bound - v)
        unit_inverse = pow(unit, -1, reduced_modulus)
        for i in range(h + 1, n):
            if data[i][h]:
                assert data[i][h] % pivot_power == 0
                factor = (data[i][h] // pivot_power) * unit_inverse % reduced_modulus
                for j in range(h+1, n):
                    data[i][j] = (data[i][j] - factor * data[h][j]) % modulus
                data[i][h] = 0
        factors.append(v)
    return Counter(factors)

expected_local = {
    2: {0: 38, 2: 2, 4: 1},
    3: {0: 34, 1: 4, 3: 3},
    5: {0: 33, 1: 8},
    7: {0: 40, 1: 1},
    67: {0: 33, 1: 8},
}
root2 = laplacian.extract(list(range(41)), list(range(41)))
invariant_factors = [1] * 41
for p, e in prime_orders.items():
    precision = max(20, e + 1)
    actual = local_smith(reduced, p, precision)
    assert actual == Counter(expected_local[p]), (p, actual)
    assert local_smith(root2, p, precision) == actual
    assert sum(k*v for k, v in actual.items()) == e
    elementary = sorted(x for k, v in actual.items() for x in [k] * v)
    for i, valuation_i in enumerate(elementary):
        invariant_factors[i] *= p ** valuation_i
assert invariant_factors == ([1]*33 + [335] + [1005]*4 + [36180]*2 + [1013040])
assert prod(invariant_factors) == order
print('G26_HESSIAN_STABLE_BOUNDARY_INTEGRAL_CRITICAL_GROUP_OK')
