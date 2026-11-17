#!/usr/bin/env python3
"""Exact finite certificate for a six-cycle maximal-averaging stability constant.
Run: python3 verify_c6.py c6_branch_certificates.json
Uses only the Python standard library; all checks are rational/integer arithmetic.
"""
import json, sys
from fractions import Fraction as Q
from pathlib import Path

n = 6
balls = []
for i in range(n):
    choices = []
    for center in range(n):
        for radius in range(4):
            ball = tuple(j for j in range(n)
                         if min((j-center) % n, (center-j) % n) <= radius)
            if i in ball and ball not in choices:
                choices.append(ball)
    assert len(choices) == 10
    balls.append(choices)
A = [[[30 * int(j in b) // len(b) for j in range(n)] for b in bset]
     for bset in balls]
assert all(30 % len(b) == 0 for bset in balls for b in bset)

def differences(prefix):
    return [tuple(A[i][choice][j] - A[i][other][j] for j in range(1,6))
            for i, choice in enumerate(prefix)
            for other in range(10) if other != choice]

def variation(v):
    return sum(abs(v[i] - v[(i+1) % n]) for i in range(n))

def norm_of_branch(prefix):
    best = Q(0)
    winning = None
    for mask in range(1, (1 << n)-1):
        bit = [(mask >> j) & 1 for j in range(n)]
        output = [sum(A[i][prefix[i]][j] * bit[j] for j in range(n))
                  for i in range(n)]
        ratio = Q(variation(output), 30*variation(bit))
        if ratio > best:
            best, winning = ratio, mask
    return best, winning

path = Path(sys.argv[1] if len(sys.argv) > 1 else 'c6_branch_certificates.json')
data = json.loads(path.read_text(encoding='utf-8'))
terminal = data['cert']
visited = set()
counters = [0] * 7
infeasible = [0] * 7
feasible_leaves = 0
best_ratio = Q(0)
winning = None

def run(prefix):
    global feasible_leaves, best_ratio, winning
    key = ''.join(map(str, prefix))
    counters[len(prefix)] += 1
    Ds = differences(prefix)
    if key in terminal and 'd' in terminal[key]:
        visited.add(key)
        dual = terminal[key]['d']
        assert dual and len(prefix) > 0
        weights = [(int(i), Q(int(p),int(q))) for i,p,q in dual]
        assert all(0 <= i < len(Ds) and w >= 0 for i,w in weights)
        assert sum(w for _,w in weights) > 0
        assert all(sum(w*Ds[i][j] for i,w in weights) == 0
                   for j in range(5))
        infeasible[len(prefix)] += 1
        return
    if len(prefix) < n:
        assert key not in terminal
        for choice in range(10):
            run(prefix + (choice,))
        return
    assert key in terminal and 'x' in terminal[key]
    visited.add(key)
    x = [Q(int(p),int(q)) for p,q in terminal[key]['x']]
    assert len(x) == 5
    assert all(sum(v * u for v,u in zip(d,x)) > 0 for d in Ds)
    feasible_leaves += 1
    ratio, cut = norm_of_branch(prefix)
    if ratio > best_ratio:
        best_ratio, winning = ratio, (prefix,cut)

run(())
assert set(terminal) == visited
assert counters == data['node_count']
assert infeasible == data['bad_count']
assert feasible_leaves == data['feasible_count'][6]
assert [best_ratio.numerator, best_ratio.denominator] == data['maximum']
assert best_ratio == Q(19,10)
print('EXACT_PRIMAL_DUAL_CERTIFICATES_PASSED', len(visited))
print('EXHAUSTIVE_BRANCH_PROFILES_PASSED', feasible_leaves)
print('EXACT_ALL_CUT_OPERATOR_NORMS_PASSED', feasible_leaves * 62)
print('SHARP_BRANCH_CUT', winning)
# Independent equality check: explicit nonnegative integer signals.
f = [50,352,360,302,365,346]
g = [50,352,361,303,366,346]
def maximal(y):
    return [max(Q(sum(y[j] for j in b), len(b)) for b in balls[i])
            for i in range(n)]
diff = [u-v for u,v in zip(maximal(g), maximal(f))]
assert diff == [Q(1,2),Q(0),Q(1),Q(3,5),Q(1),Q(0)]
assert variation([g[i]-f[i] for i in range(n)]) == 2
assert variation(diff) == Q(19,5)
print('NONNEGATIVE_INTEGER_INPUT_EQUALITY_PASSED')
print('C6_SHARP_TWO_INPUT_VARIATION_CONSTANT_PASSED 19/10')
