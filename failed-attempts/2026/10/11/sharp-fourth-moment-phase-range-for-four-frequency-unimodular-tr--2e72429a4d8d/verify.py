#!/usr/bin/env python3
import cmath
import itertools
import math


def support_relations(A):
    A = tuple(sorted(A))
    aps = []
    for triple in itertools.combinations(A, 3):
        u, m, v = triple
        if u + v == 2 * m:
            aps.append(triple)
    symmetric = (A[0] + A[3] == A[1] + A[2])
    return aps, symmetric


def direct_fourth(A, coeffs):
    fibers = {}
    for i, a in enumerate(A):
        for j, b in enumerate(A):
            fibers[a + b] = fibers.get(a + b, 0j) + coeffs[i] * coeffs[j]
    return sum(abs(z) ** 2 for z in fibers.values())


def closed_fourth(A, coeffs):
    A = tuple(sorted(A))
    idx = {a: i for i, a in enumerate(A)}
    aps, symmetric = support_relations(A)
    value = 28.0
    for u, m, v in aps:
        phase = coeffs[idx[m]] ** 2 * (coeffs[idx[u]] * coeffs[idx[v]]).conjugate()
        value += 4.0 * phase.real
    if symmetric:
        phase = coeffs[0] * coeffs[3] * (coeffs[1] * coeffs[2]).conjugate()
        value += 8.0 * phase.real
    return value


seen = set()
count = 0
for A in itertools.combinations(range(19), 4):
    aps, symmetric = support_relations(A)
    key = (len(aps), int(symmetric))
    seen.add(key)
    assert key in {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1)}
    if key == (2, 1):
        gaps = [A[i + 1] - A[i] for i in range(3)]
        assert gaps[0] == gaps[1] == gaps[2]
    plus = [1 + 0j] * 4
    expected_plus = 28 + 4 * len(aps) + 8 * int(symmetric)
    assert abs(direct_fourth(A, plus) - expected_plus) < 1e-12
    for seed in range(4):
        angles = [((seed + 1) * (j + 2) * 0.713 + (A[j] + 1) * 0.271) % (2 * math.pi) for j in range(4)]
        c = [cmath.exp(1j * x) for x in angles]
        assert abs(direct_fourth(A, c) - closed_fourth(A, c)) < 1e-9
    count += 1

assert seen == {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1)}

# Exact support representatives attain the asserted idempotent maxima.
reps = {
    (0, 0): (0, 1, 3, 7),
    (1, 0): (0, 1, 2, 5),
    (2, 0): (0, 1, 2, 4),
    (0, 1): (0, 1, 3, 4),
    (2, 1): (0, 1, 2, 3),
}
for key, A in reps.items():
    aps, sym = support_relations(A)
    assert (len(aps), int(sym)) == key

# Four-term-progression lower extremizer: alpha=beta=theta, cos(theta)=-1/4.
theta = math.acos(-0.25)
A = (0, 1, 2, 3)
c = [1 + 0j, 1 + 0j, cmath.exp(-1j * theta), cmath.exp(-3j * theta)]
assert abs(direct_fourth(A, c) - 19.0) < 1e-10
assert abs(closed_fourth(A, c) - 19.0) < 1e-10
assert abs(direct_fourth(A, [1 + 0j] * 4) - 44.0) < 1e-12

print(f"VERIFY_OK supports={count} types={len(seen)} phase_samples={4*count} endpoints=19,44")
