"""Exact finite arithmetic checks for a cube-free divisor-range theorem.

Run: python3 verify.py.  Only Python's standard library is required.
The analytic prime-ratio lemma and the infinite greedy argument are proved
or cited in the accompanying paper, not inferred from finite experiments.
"""
from fractions import Fraction as F
from math import isqrt


def prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def factor(p, e):
    assert prime(p)
    return sum((F(1, p ** (2*j)) for j in range(e + 1)), F(0))


# Two finite exceptions to the infinite prime-ratio lemma.
finite_primes = (7, 11, 13, 17, 19, 23)
checks = {5: finite_primes[:5], 7: finite_primes[1:]}
for p, qs in checks.items():
    product = F(1)
    for q in qs: product *= factor(q, 1)
    assert product > factor(p, 1)
    print('tail_exception', p, 'margin', product - factor(p, 1))

# Archimedes-style rational enclosure 157/50 < pi < 22/7.
pi_min, pi_max = F(157, 50), F(22, 7)
U_min = F(9720, 91) / pi_max**4
U_max = F(9720, 91) / pi_min**4
assert F(109, 100) < U_min < U_max < F(11, 10)
assert U_min > F(91, 90)
assert F(91, 81) * U_max < F(5, 4)
assert U_max < F(10, 9)

# Verify precise algebra of the 9 intervals and their 3 disjoint blocks.
a, b = (F(1), F(5, 4), F(21, 16)), (F(1), F(10, 9), F(91, 81))
assert factor(2, 2) == a[2] and factor(3, 2) == b[2]
assert a[2] * b[2] * F(9720, 91) == F(315, 2)
assert b[2] * F(9720, 91) == 120

blocks = [[], [], []]
for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        block = 0 if (i, j) == (0, 0) else (1 if i == 0 else 2)
        blocks[block].append((ai * bj, ai * bj))

for index, intervals in enumerate(blocks):
    intervals.sort()
    if index == 0:
        assert intervals == [(F(1), F(1))]
    else:
        end = intervals[0][0] * U_min
        for low, multiplier in intervals[1:]:
            assert low <= end
            end = max(end, multiplier * U_min)
    print('interval_block', index + 1, 'starts', [str(x) for x,_ in intervals])
assert blocks[1][0][0] == F(10, 9)
assert blocks[2][0][0] == F(5, 4)

# Prime-support cylinder densities, expressed as multiples of 1/zeta(3).
# For p=2,3 the local probability of v_p=a is p^-a-p^(-a-1).
local = lambda p, e: F(1, p**e) - F(1, p**(e + 1))
tail_density_factor = F(1) / ((1-F(1, 8)) * (1-F(1, 27)))
q = (
    local(2, 0) * local(3, 0),
    local(2, 0) * sum((local(3, j) for j in (1, 2)), F(0)),
    sum((local(2, i) for i in (1, 2)), F(0)) * sum((local(3, j) for j in (0, 1, 2)), F(0)),
)
expected = (F(36, 91), F(16, 91), F(39, 91))
assert tuple(tail_density_factor*x for x in q) == expected
assert sum(expected) == 1
print('density_coefficients_of_inverse_zeta3', [str(x) for x in expected])
print('VERIFY_OK finite_tail_inequalities=2 intervals=9 components=3 density_identities=3')
