"""Exact exhaustive finite-field checks for a symmetric Burkhardt quartic twist."""
from itertools import combinations, product
from functools import reduce

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def multiply(a, b, degree):
    poly = IRREDUCIBLE[degree]
    answer = 0
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= poly
    return answer


def symmetric_e4(x, degree):
    e = [1, 0, 0, 0, 0]
    for a in x:
        for j in range(4, 0, -1):
            e[j] ^= multiply(a, e[j - 1], degree)
    return e[4]


def symmetric_e4_independent(x, degree):
    answer = 0
    for c in combinations(x, 4):
        v = 1
        for a in c:
            v = multiply(v, a, degree)
        answer ^= v
    return answer


def classical_equation(y, degree):
    cubes = 0
    for a in y:
        cubes ^= multiply(multiply(a, a, degree), a, degree)
    product_last = 1
    for a in y[1:]:
        product_last = multiply(product_last, a, degree)
    return multiply(y[0], cubes, degree) ^ product_last


def projective_representatives(q):
    for initial in range(5):
        for later in product(range(q), repeat=4-initial):
            yield (0,) * initial + (1,) + later


def count(m):
    q = 1 << m
    twisted = classical = 0
    for v in projective_representatives(q):
        six = v + (reduce(int.__xor__, v, 0),)
        a = symmetric_e4(six, m)
        if m <= 3:
            assert a == symmetric_e4_independent(six, m)
        twisted += (a == 0)
        classical += (classical_equation(v, m) == 0)
    return twisted, classical


def formula(m):
    q = 1 << m
    return 1 + q**3 + (11*q - 4*q*q if m % 2 else -29*q + 16*q*q)

expected_twisted = {1:15, 2:205, 3:345, 4:7729}
expected_classical = {1:23, 2:205, 3:761, 4:7729}
for m in range(1, 5):
    observed_twisted, observed_classical = count(m)
    assert observed_twisted == expected_twisted[m], (m, observed_twisted)
    assert observed_classical == expected_classical[m], (m, observed_classical)
    assert observed_twisted == formula(m)
    print(f"m={m} q={1<<m} symmetric_twist={observed_twisted} classical={observed_classical}")

# In F2, the hyperplane sigma_1=0 has even-weight vectors.
# Weight 2 has sigma_4=0; weights 4 and 6 have sigma_4=1.
# All 15 weight-two points have zero ambient sigma_4 gradient.
for i, j in combinations(range(6), 2):
    v = tuple(int(a in (i, j)) for a in range(6))
    assert symmetric_e4(v, 1) == 0
    for k in range(6):
        others = [v[t] for t in range(6) if t != k]
        e3 = 0
        for a, b, c in combinations(others, 3):
            e3 ^= a & b & c
        assert e3 == 0
print("all_15_F2_points_are_singular")
print("VERIFY_OK")
