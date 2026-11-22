"""Exact, dependency-free transfer certificate for majority dynamics on prisms.

Run with Python 3.9+: python verify_transfer.py
"""
from collections import Counter
from math import cos, pi


def majority(a, b, c):
    return int(a + b + c >= 2)


def bits(number, count):
    return tuple((number >> i) & 1 for i in range(count))


def allows2(a, b, c):
    left, mid, right = bits(a, 4), bits(b, 4), bits(c, 4)
    return (mid[2] == majority(left[0], right[0], mid[1])
            and mid[3] == majority(left[1], right[1], mid[0])
            and mid[0] == majority(left[2], right[2], mid[3])
            and mid[1] == majority(left[3], right[3], mid[2]))


def allows1(a, b, c):
    left, mid, right = bits(a, 2), bits(b, 2), bits(c, 2)
    return (mid[0] == majority(left[0], right[0], mid[1])
            and mid[1] == majority(left[1], right[1], mid[0]))


def transfer(alpha, valid):
    size = alpha * alpha
    arcs = [[] for _ in range(size)]
    for a in range(alpha):
        for b in range(alpha):
            for c in range(alpha):
                if valid(a, b, c):
                    arcs[alpha * a + b].append(alpha * b + c)
    return arcs


def strongly_connected(arcs):
    size = len(arcs)
    index = 0
    stack, onstack, discover, low, answer = [], set(), {}, {}, []

    def visit(v):
        nonlocal index
        discover[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in arcs[v]:
            if w not in discover:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], discover[w])
        if low[v] == discover[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1 or (len(comp) == 1 and v in arcs[v]):
                answer.append(sorted(comp))

    for v in range(size):
        if v not in discover:
            visit(v)
    return sorted(answer, key=lambda c: (-len(c), c))


def adjacency(arcs, component):
    positions = {vertex: i for i, vertex in enumerate(component)}
    k = len(component)
    M = [[0] * k for _ in range(k)]
    for v in component:
        for w in arcs[v]:
            if w in positions:
                M[positions[v]][positions[w]] += 1
    return M


def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            a = A[i][k]
            if a:
                for j in range(n):
                    C[i][j] += a * B[k][j]
    return C


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def power_sums_and_char(A):
    """Exact Newton identities, coefficients of det(zI-A) and traces A^1..A^k."""
    k = len(A)
    X = [[int(i == j) for j in range(k)] for i in range(k)]
    sums = []
    for i in range(1, k + 1):
        X = multiply(X, A)
        sums.append(trace(X))
    co = [1]
    for j in range(1, k + 1):
        total = sum(co[j - i] * sums[i - 1] for i in range(1, j + 1))
        assert total % j == 0
        co.append(-total // j)
    return co, sums


def poly_multiply(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


def polynomial(*factors):
    result = [1]
    for factor in factors:
        result = poly_multiply(result, factor)
    return result


def lucas(k):
    a, b = 2, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def expected(n):
    L = lucas(n)
    L2 = lucas(2 * n)
    if n % 2:
        P = L2 + (4 if n % 3 == 0 else 1)
        H = L + (0 if n % 3 == 0 else 3)
    else:
        P = L2 + (8 * L + 18 if n % 3 == 0 else 2 * L + 3)
        H = L + (4 if n % 3 == 0 else 1)
    return H, P


T2, T1 = transfer(16, allows2), transfer(4, allows1)
assert sum(map(len, T2)) == 400
assert sum(map(len, T1)) == 20
S2, S1 = strongly_connected(T2), strongly_connected(T1)
assert sorted(map(len, S2), reverse=True) == [16, 8, 8, 2, 1, 1]
assert sorted(map(len, S1), reverse=True) == [4, 1, 1]

# All factor coefficient lists are ordered from highest to constant degree.
quad_golden = [1, -3, 1]
third = [1, 1, 1]
quartic_minus = [1, -1, 2, 1, 1]
quartic_plus = [1, 1, 2, -1, 1]
poly_core = polynomial([1, -1], [1, -1], [1, 1], [1, 1],
                       quad_golden, third, quartic_minus, quartic_plus)
poly_eight = polynomial([1, -1, -1], [1, -1, 1],
                        [1, 1, -1], [1, 1, 1])
poly_fixed = polynomial([1, -1, -1], [1, -1, 1])
checks2 = sorted([poly_core, poly_eight, poly_eight, [1, 0, -1], [1, -1], [1, -1]],
                 key=lambda v: (-len(v), v))
checks1 = sorted([poly_fixed, [1, -1], [1, -1]], key=lambda v: (-len(v), v))

for arcs, comps, expected_polys in [(T2, S2, checks2), (T1, S1, checks1)]:
    observed = sorted([power_sums_and_char(adjacency(arcs, c))[0] for c in comps],
                      key=lambda v: (-len(v), v))
    assert observed == expected_polys, (observed, expected_polys)

components2 = [adjacency(T2, comp) for comp in S2]
components1 = [adjacency(T1, comp) for comp in S1]

def trace_list(components, horizon):
    powers = [[[int(i == j) for j in range(len(M))] for i in range(len(M))]
              for M in components]
    result = []
    for n in range(1, horizon + 1):
        powers = [multiply(p, M) for p, M in zip(powers, components)]
        result.append(sum(trace(p) for p in powers))
    return result

p = trace_list(components2, 32)
h = trace_list(components1, 32)
for n in range(3, 33):
    H, P = expected(n)
    assert (h[n-1], p[n-1]) == (H, P), (n, h[n-1], p[n-1], H, P)
    assert (P - H) % 2 == 0 and P >= H
print('exact transfer identities: PASS')
print('2-step SCC sizes:', [len(c) for c in S2])
print('1-step SCC sizes:', [len(c) for c in S1])
for n in range(3, 13):
    H, P = expected(n)
    print(f'n={n:2d} fixed={H:7d} periodic_states={P:8d} primitive_two_cycles={(P-H)//2:7d}')
print('Lucas formulas checked through n=32; all-size claim follows from characteristic polynomials.')
