#!/usr/bin/env python3
"""Exact standard-library verification of genus-four hyperelliptic spin spectra.

Run: python3 verify_genus4_spin.py

The two checks are independent: orbit traversal on actual finite sets, and
fixed-point generating-function counts for every power of each permutation.
"""
from collections import Counter, defaultdict
from functools import reduce
from itertools import combinations
from math import comb, gcd, lcm

N = 10
U = frozenset(range(N))


def partitions(n, upper=None):
    if n == 0:
        yield ()
    else:
        for a in range(min(n, n if upper is None else upper), 0, -1):
            for rest in partitions(n - a, a):
                yield (a,) + rest


def permutation(parts):
    s = list(range(N))
    pos = 0
    for size in parts:
        for j in range(size):
            s[pos + j] = pos + (j + 1) % size
        pos += size
    assert pos == N
    return s


def normalize_five(a):
    a = frozenset(a)
    return min(a, U - a, key=lambda z: tuple(sorted(z)))

ODD = [frozenset(c) for c in combinations(range(N), 3)]
EVEN = [frozenset([i]) for i in range(N)] + sorted(
    {normalize_five(c) for c in combinations(range(N), 5)},
    key=lambda x: tuple(sorted(x))
)
assert len(ODD) == 120 and len(EVEN) == 136


def cycle_spectrum(perm, domain):
    """Method A: directly follow every orbit of the induced permutation."""
    domain = set(domain)
    seen = set()
    lengths = Counter()
    for element in domain:
        if element in seen:
            continue
        here = element
        span = 0
        while here not in seen:
            seen.add(here)
            span += 1
            moved = frozenset(perm[i] for i in here)
            here = normalize_five(moved) if len(moved) == 5 else moved
        assert here == element
        lengths[span] += 1
    assert seen == domain
    return tuple(sorted(lengths.items()))


def fixed_from_spectrum(spectrum, n):
    return sum(length * count for length, count in spectrum if n % length == 0)


def power_cycles(parts, n):
    result = []
    for length in parts:
        count = gcd(length, n)
        result.extend([length // count] * count)
    return result


def coefficient_five(cycle_lengths):
    coeff = [1, 0, 0, 0, 0, 0]
    for size in cycle_lengths:
        for k in range(5, size - 1, -1):
            coeff[k] += coeff[k - size]
    return coeff[5]


def formula_fixed(parts, n):
    """Method B: cycle-index coefficient and complementary half-subset formula."""
    counts = Counter(power_cycles(parts, n))
    one, two, three = (counts.get(j, 0) for j in (1, 2, 3))
    odd = (comb(one, 3) if one >= 3 else 0) + one * two + three
    cycles = list(counts.elements())
    stable_five = coefficient_five(cycles)
    swapped_five = 2 ** len(cycles) if all(k % 2 == 0 for k in cycles) else 0
    assert (stable_five + swapped_five) % 2 == 0
    even = one + (stable_five + swapped_five) // 2
    return (odd, even)

P = list(partitions(N))
assert len(P) == 42 and len(set(P)) == 42
spectra = {}
for part in P:
    perm = permutation(part)
    spectrum_odd = cycle_spectrum(perm, ODD)
    spectrum_even = cycle_spectrum(perm, EVEN)
    assert sum(k * m for k, m in spectrum_odd) == 120
    assert sum(k * m for k, m in spectrum_even) == 136
    # Check all powers through the precise order of the branch permutation.
    order = lcm(*part)
    for n in range(1, order + 1):
        actual = (fixed_from_spectrum(spectrum_odd, n),
                  fixed_from_spectrum(spectrum_even, n))
        assert actual == formula_fixed(part, n), (part, n, actual)
    spectra[part] = (spectrum_odd, spectrum_even)

joint = defaultdict(list)
odd_spectra = defaultdict(list)
even_spectra = defaultdict(list)
for part, (odd, even) in spectra.items():
    joint[(odd, even)].append(part)
    odd_spectra[odd].append(part)
    even_spectra[even].append(part)
assert len(joint) == 40 and len(odd_spectra) == 40 and len(even_spectra) == 37
collisions = sorted(sorted(group) for group in joint.values() if len(group) > 1)
assert collisions == [[(4, 4, 1, 1), (4, 4, 2)], [(8, 1, 1), (8, 2)]], collisions

def signature(part, through):
    odd, even = spectra[part]
    return tuple((fixed_from_spectrum(odd, n), fixed_from_spectrum(even, n))
                 for n in range(1, through + 1))

for through, num in [(1, 22), (2, 33), (3, 39), (4, 39), (5, 40)]:
    assert len({signature(part, through) for part in P}) == num

four = defaultdict(list)
for part in P:
    four[signature(part, 4)].append(part)
assert sorted(sorted(g) for g in four.values() if len(g) > 1) == [
    [(4, 4, 1, 1), (4, 4, 2)],
    [(5, 5), (10,)],
    [(8, 1, 1), (8, 2)],
]
assert signature((10,), 4) == signature((5, 5), 4)
assert signature((10,), 5) != signature((5, 5), 5)
assert max(min(length for length, num in spectra[part][0]) for part in P) == 10
assert spectra[(10,)][0] == ((10, 12),)
assert spectra[(10,)][1] == ((1, 1), (5, 3), (10, 12))

# Explicit irreducible polynomials over F3: coefficients from constant upward.
EXPLICIT = {
    'quadratic': (1, 0, 1),                # x^2 + 1
    'quartic_A': (2, 1, 0, 0, 1),         # x^4 + x + 2
    'quartic_B': (2, 2, 0, 0, 1),         # x^4 + 2x + 2
    'octic': (2, 0, 1, 0, 0, 0, 0, 0, 1),# x^8 + x^2 + 2
    'quintic_A': (1, 2, 0, 0, 0, 1),     # x^5 + 2x + 1
    'quintic_B': (2, 2, 0, 0, 0, 1),     # x^5 + 2x + 2
    'decic': (1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1), # x^10+2x^2+1
}

def trim(a):
    a = tuple(i % 3 for i in a)
    while a and a[-1] == 0:
        a = a[:-1]
    return a

def poly_divmod(a, b):
    a, b = list(trim(a)), trim(b)
    assert b
    q = [0] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        t = len(a) - len(b)
        coeff = a[-1] * pow(b[-1], -1, 3) % 3
        q[t] = coeff
        for i, v in enumerate(b):
            a[i + t] = (a[i + t] - coeff * v) % 3
        while a and a[-1] == 0:
            a.pop()
    return trim(q), trim(a)

def poly_mulmod(a, b, modulus):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % 3
    return poly_divmod(out, modulus)[1]

def poly_powmod(a, k, mod):
    acc = (1,)
    while k:
        if k & 1:
            acc = poly_mulmod(acc, a, mod)
        a = poly_mulmod(a, a, mod)
        k //= 2
    return acc

def poly_gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, poly_divmod(a, b)[1]
    if a:
        v = pow(a[-1], -1, 3)
        a = trim(tuple(v * x % 3 for x in a))
    return a

def distinct_prime_divisors(n):
    result = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            result.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.add(n)
    return result

def irreducible(f):
    f = trim(f)
    n = len(f) - 1
    x = (0, 1)
    assert f[-1] == 1
    def minus_x(p):
        t = list(p) + [0] * max(0, 2 - len(p))
        t[1] = (t[1] - 1) % 3
        return trim(t)
    if poly_powmod(x, 3**n, f) != x:
        return False
    return all(poly_gcd(f, minus_x(poly_powmod(x, 3**(n//r), f))) == (1,)
               for r in distinct_prime_divisors(n))

assert all(irreducible(f) for f in EXPLICIT.values())
assert EXPLICIT['quartic_A'] != EXPLICIT['quartic_B']
assert EXPLICIT['quintic_A'] != EXPLICIT['quintic_B']
assert all(f[0] != 0 and sum(f) % 3 != 0 for k, f in EXPLICIT.items())

# These four monic squarefree polynomials have Frobenius types:
# octic*quadratic (8,2), octic*x*(x-1) (8,1,1),
# quartic_A*quartic_B*quadratic (4,4,2),
# quartic_A*quartic_B*x*(x-1) (4,4,1,1).

def fmt(s):
    return ' '.join(f'{length}^{count}' for length, count in s)

with open('spin_spectra_42.tsv', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('branch_partition\todd_cycles\teven_cycles\tfirst_five_counts_(odd,even)\n')
    for part in P:
        odd, even = spectra[part]
        fh.write(f'{part}\t{fmt(odd)}\t{fmt(even)}\t{signature(part,5)}\n')

print('GENUS4_HYPERELLIPTIC_SPIN_42_TYPES_40_JOINT_SPECTRA_VERIFIED')
print('odd_spectra=40 even_spectra=37 joint_spectra=40')
print('joint_collisions=', collisions)
print('first_extension_count_types_by_cutoff=22,33,39,39,40; sharp_cutoff=5')
print('ten_cycle_odd=', spectra[(10,)][0], 'ten_cycle_even=', spectra[(10,)][1])
print('all_seven_F3_polynomials_irreducible=True')
