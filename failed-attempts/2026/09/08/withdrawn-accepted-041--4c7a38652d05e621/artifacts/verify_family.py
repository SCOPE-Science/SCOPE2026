"""Exact verification for odd Martin-type largest-denominator theorem.
Checks: base expansion sums to 1 (odd/distinct), splitting identities hold
as exact rational identities for all k tested, iterated family E_n valid
with strictly increasing odd maxima. Uses only stdlib Fraction.
"""
from fractions import Fraction

E0 = [3, 5, 7, 9, 15, 21, 27, 35, 63, 105, 135]

def split(k):
    assert k % 2 == 1 and k > 1
    if k % 4 == 3:
        a = 3 * k
        b = (3 * k + 1) // 2
        c = 3 * k * b
    else:  # k % 4 == 1
        a = 3 * k
        b = 3 * (k + 1) // 2
        c = 3 * k * (k + 1) // 2
    return (a, b, c)

def check_identity(k):
    a, b, c = split(k)
    assert (3 * k + 1) % 2 == 0 or k % 4 == 1  # integrality guard
    assert Fraction(1, a) + Fraction(1, b) + Fraction(1, c) == Fraction(1, k), k
    assert a % 2 == b % 2 == c % 2 == 1, (k, a, b, c)
    assert len({a, b, c}) == 3, (k, a, b, c)
    assert a > k and b > k and c > k, (k, a, b, c)
    assert c == max(a, b, c)
    return (a, b, c)

# 1. base expansion
assert len(set(E0)) == len(E0) and all(d % 2 == 1 and d > 1 for d in E0)
assert sum(Fraction(1, d) for d in E0) == 1, "base sum != 1"
print("E0 ok, max =", max(E0))

# 2. identity sweep over many odd k (both residue classes)
for k in range(3, 4000, 2):
    check_identity(k)
print("identity sweep ok for all odd k in [3,3999]")

# 3. iterate family splitting the current maximum
E = list(E0)
maxima = [max(E)]
for n in range(4):
    M = max(E)
    a, b, c = check_identity(M)
    assert M not in (a, b, c) and a > M and b > M and c > M
    assert all(d not in E for d in (a, b, c))  # freshness: children exceed old max
    E = [d for d in E if d != M] + [a, b, c]
    assert len(set(E)) == len(E) and all(d % 2 == 1 for d in E)
    assert sum(Fraction(1, d) for d in E) == 1, f"E{n+1} sum != 1"
    maxima.append(max(E))
    print(f"E{n+1} ok: split {M} -> {(a,b,c)}, new max {max(E)}, terms {len(E)}")
assert all(m % 2 == 1 for m in maxima) and all(b > a for a, b in zip(maxima, maxima[1:]))
print("maxima:", maxima)

# 4. prime-obstruction sanity: exhaustive subset check that no odd-distinct
# expansion with largest denominator p exists for small odd primes
import itertools
def has_expansion_with_max(p):
    odds = [d for d in range(3, p + 1, 2)]
    # subset must include p and sum to 1
    rest = [d for d in odds if d != p]
    need = Fraction(1, 1) - Fraction(1, p)
    for r in range(0, len(rest) + 1):
        for combo in itertools.combinations(rest, r):
            if sum(Fraction(1, d) for d in combo) == need:
                return True, (p,) + combo
    return False, None
for p in (3, 5, 7, 11):
    ok, wit = has_expansion_with_max(p)
    print(f"prime max {p}: expansion exists? {ok}")
    assert not ok
print("ALL CHECKS PASSED")
