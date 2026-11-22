#!/usr/bin/env python3
"""Independent finite-volume checks of the classical K4-by-cycle Ising tube.

Only standard-library Python is used. This code supports, but does not replace,
the finite-state and algebraic arguments in RESULT.md.
"""
from collections import defaultdict
from itertools import product

S = [tuple(1 if mask & (1 << j) else -1 for j in range(4))
     for mask in range(16)]
M = [sum(s) for s in S]
R = [(m*m - 4)//2 for m in M]
INTER = [[sum(a*b for a, b in zip(x, y)) for y in S] for x in S]


def energy(columns, h):
    n = len(columns)
    return sum(R[a] + INTER[a][columns[(i+1)%n]] - h*M[a]
               for i, a in enumerate(columns))


def brute(n, h):
    best = None
    counts = defaultdict(int)
    for columns in product(range(16), repeat=n):
        e = energy(columns, h)
        if best is None or e < best:
            best = e
            counts.clear()
        if e == best:
            counts[sum(M[a] for a in columns)//2] += 1
    return best, dict(counts)


def independent_dp(n, h):
    # Recurrence from the ORIGINAL spin Hamiltonian, not from the subset graph.
    result = {}
    global_best = None
    for a in range(16):
        dp = {(a, M[a]): (R[a]-h*M[a], 1)}
        for j in range(1, n):
            ndp = {}
            for (b, magnet), (cost, count) in dp.items():
                for c in range(16):
                    key = (c, magnet+M[c])
                    new_cost = cost+INTER[b][c]+R[c]-h*M[c]
                    prev_cost, prev_count = ndp.get(key, (10**20, 0))
                    if new_cost < prev_cost:
                        ndp[key] = (new_cost, count)
                    elif new_cost == prev_cost:
                        ndp[key] = (new_cost, prev_count+count)
            dp = ndp
        for (b, magnet), (cost, count) in dp.items():
            cost += INTER[b][a]
            if global_best is None or cost < global_best:
                global_best = cost
                result = {magnet//2: count}
            elif cost == global_best:
                result[magnet//2] = result.get(magnet//2, 0)+count
    return global_best, result


def subset_graph_polynomial(n, allowed):
    # State is the actual set of negative legs (bit mask), weighted by half magnetization.
    states = [b for b in range(16) if b.bit_count() in allowed]
    result = defaultdict(int)
    for a in states:
        dp = {(a, (4-2*a.bit_count())//2): 1}
        for step in range(1, n):
            ndp = defaultdict(int)
            for (b, degree), count in dp.items():
                for c in states:
                    if b & c == 0:
                        ndp[(c, degree+(4-2*c.bit_count())//2)] += count
            dp = ndp
        for (b, degree), count in dp.items():
            if b & a == 0:
                result[degree] += count
    return dict(result)


def recurrence_trace(n, a, b):
    # Roots of lambda^2-a lambda-b have power sums S0=2,S1=a.
    p0, p1 = 2, a
    if n == 0: return p0
    if n == 1: return p1
    for j in range(2, n+1):
        p0, p1 = p1, a*p1+b*p0
    return p1


def expected_count_3(n):
    return recurrence_trace(n,4,3)+3*recurrence_trace(n,-2,1)+2


def expected_count_5(n):
    return recurrence_trace(n,4,1)+3*(-1)**n

checks = 0
# The explicit block decomposition used in the all-size characteristic proof.
pairs = [b for b in range(16) if b.bit_count()==2]
B = [[int((a & b)==0) for b in pairs] for a in (1,2,4,8)]
for i in range(4):
    for j in range(4):
        assert sum(B[i][k]*B[j][k] for k in range(6)) == (3 if i==j else 1)
        checks += 1
for k in range(3):
    u=[int(i==k)-int(i==3) for i in range(4)]
    for idx,b in enumerate(pairs):
        complement_index=pairs.index(15 ^ b)
        assert sum(B[i][complement_index]*u[i] for i in range(4)) == -sum(B[i][idx]*u[i] for i in range(4))
        checks += 1
for n in range(3, 17):
    p3 = subset_graph_polynomial(n, {1,2})
    p5 = subset_graph_polynomial(n, {0,1})
    assert sum(p3.values()) == expected_count_3(n), (n,p3)
    assert sum(p5.values()) == expected_count_5(n), (n,p5)
    assert p3.get(0,0) == (6 if n%2 == 0 else 0)
    if n%2:
        assert p3.get(2,0) == 12*n*(n-2)
        checks += 1
    assert p3.get(n,0) == 3**n + 3*(-1)**n
    assert p5.get(n,0) == 3**n + 3*(-1)**n
    assert p5.get(2*n,0) == 1
    checks += 6
for n in range(3, 10):
    for h, allowed, target in [(3,{1,2},-6*n),(5,{0,1},-10*n)]:
        best, p = independent_dp(n,h)
        expected = subset_graph_polynomial(n,allowed)
        assert best == target and p == expected, (n,h,best,p,expected)
        checks += 1
    best, p = independent_dp(n,4)
    assert best == -8*n and p == {n: 3**n+3*(-1)**n}, (n,best,p)
    checks += 1
    best, p = independent_dp(n,6)
    assert best == -14*n and p == {2*n:1}, (n,best,p)
    checks += 1
for n in (3,4):
    for h in (0,3,4,5,6):
        direct = brute(n,h)
        dp = independent_dp(n,h)
        assert direct == dp, (n,h,direct,dp)
        checks += 1
print('K4_CYCLE_ISING_CHECKS_PASSED', checks)
