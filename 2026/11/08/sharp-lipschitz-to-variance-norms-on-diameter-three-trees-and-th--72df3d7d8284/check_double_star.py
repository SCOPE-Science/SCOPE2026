"""Exact standalone verification of the double-star Lipschitz-spread theorem.

Only the Python standard library is needed. Finite enumeration is a check,
not a substitute for the all-parameter proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb


def predicted(a, b):
    assert a >= 1 and b >= 1
    a, b = max(a, b), min(a, b)
    N = a + b + 2
    h = a + 2*b + 1
    if a <= 2*b + 1:
        delta = (2*b + 1-a)**2
    else:
        delta = h % 2
    return Fraction(N*(a + 4*b + 1)-delta, N*N)


def integer_objective(a, b, k, j):
    N = a+b+2
    S = a + 1-2*k+2*j
    Q = a + 1+4*j
    return N*Q-S*S


def brute(a, b):
    N = a+b+2
    best = Fraction(-1, 1)
    configs = []
    for signs_a in product((-1, 1), repeat=a):
        for signs_b in product((0, 2), repeat=b):
            x = [0, 1] + list(signs_a) + list(signs_b)
            sx = sum(x)
            sx2 = sum(v*v for v in x)
            val = Fraction(N*sx2 - sx*sx, N*N)
            if val > best:
                best = val
                configs = [(signs_a, signs_b)]
            elif val == best:
                configs.append((signs_a, signs_b))
    return best, configs


# Independent exhaustive enumeration of all signed tree-edge vertices.
ct = 0
for a in range(1, 9):
    for b in range(1, 9):
        expected = predicted(a, b)
        got, profiles = brute(a, b)
        assert expected == got, (a, b, expected, got)
        # Reconstruct every possible predicted optimizer, not merely its value.
        A, B = max(a, b), min(a, b)
        h = A + 2*B + 1
        best_k = {k for k in range(A+1)
                  if abs(h-2*k) == min(abs(h-2*t) for t in range(A+1))}
        # Brute graph edge orientation may be swapped if a < b.
        if a >= b:
            observed = {(sum(z == -1 for z in x), sum(z == 2 for z in y))
                        for x, y in profiles}
            assert observed == {(k, b) for k in best_k}, (a,b,observed,best_k)
            assert len(profiles) == sum(comb(a,k) for k in best_k)
        else:
            # Under hub-swapping and sign reversal followed by translation,
            # the larger part is the class whose leaves take the two values.
            observed = {(sum(z == -1 for z in x), sum(z == 2 for z in y))
                        for x, y in profiles}
            # On the originally smaller left side all leaves must be -1;
            # on the larger right side the number at 2 is k.
            assert observed == {(a,k) for k in best_k}, (a,b,observed,best_k)
            assert len(profiles) == sum(comb(b,k) for k in best_k)
        ct += 1
print('EXHAUSTIVE_EXACT_TREE_EDGE_VERTEX_AND_EQUALITY_CHECKS_OK', ct)

# Check the diagonal-saturation reduction directly on a larger parameter grid.
ct = 0
for a in range(1, 81):
    for b in range(1, 81):
        N = a+b+2
        optimum = max(integer_objective(a,b,k,j)
                      for k in range(a+1) for j in range(b+1))
        assert optimum == predicted(a,b)*(a+b+2)**2
        ct += 1
print('EXACT_ALL_INTEGER_PROFILE_MAXIMIZATIONS_OK', ct)

# The fixed-order strict-balancing and sharp upper envelope.
for s in range(2, 301):
    pairs = [(a,s-a) for a in range((s+1)//2, s)]
    vals = [predicted(a,b) for a,b in pairs]
    assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))
    N = s+2
    envelope = Fraction(9,4)-Fraction(4,N)-Fraction(9*(N%2),4*N*N)
    assert vals[0] == envelope
print('SHARP_FIXED_ORDER_BALANCE_AND_PARITY_ENVELOPE_OK', 299)

# Check threshold and tie classifications on a substantial range.
for b in range(1, 100):
    for a in range(b, 6*b+9):
        N = a+b+2
        h = a+2*b+1
        vals = [integer_objective(a,b,k,b) for k in range(a+1)]
        ks = {k for k,z in enumerate(vals) if z == max(vals)}
        assert (a in ks) == (a <= 2*b+2)
        if a == 2*b+2:
            assert ks == {a-1,a}
        if a >= 2*b+3:
            assert a not in ks
        if a >= 2*b+1:
            assert len(ks) == (2 if h%2 else 1)
print('SHARP_POLARIZATION_TRANSITION_AND_PARITY_TIES_OK')
print('ALL_DOUBLE_STAR_LIPSCHITZ_SPREAD_CHECKS_OK')
