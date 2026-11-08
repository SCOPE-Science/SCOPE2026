"""Independent finite checks for the geometric-occupancy discovery theorem.

The infinite limiting assertion is proved analytically in RESULT.md; this script
checks finite identities, exact combinatorial probabilities, and numerical
approximations. No external packages are required.
"""
from collections import defaultdict
from fractions import Fraction
from math import exp, expm1, prod

CHECKS = 0

def check(condition):
    global CHECKS
    assert condition
    CHECKS += 1

def mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ans

def polynomial_one_minus_power(k):
    out = [0]*(k+1)
    out[0], out[k] = 1, -1
    return out

# The algebraic factorization behind the telescoping zero-event product.
left = mul(mul([1, -1, 1], polynomial_one_minus_power(3)), polynomial_one_minus_power(2))
right = mul(polynomial_one_minus_power(6), polynomial_one_minus_power(1))
check(left == right)

# Exact finite occupancy construction: box j has mass 2^{-j}, j >= 1.
# The lower bound counts the event that all first 2n labels lie among
# the first J boxes AND the second block introduces no new box.
def finite_lower_bound(n, J):
    weights = [Fraction(1, 2**j) for j in range(1, J+1)]
    distribution = {0: Fraction(1)}
    for _ in range(n):
        nxt = defaultdict(Fraction)
        for mask, p in distribution.items():
            for i, weight in enumerate(weights):
                nxt[mask | (1 << i)] += p*weight
        distribution = nxt
    result = Fraction(0)
    for mask, p in distribution.items():
        weight = sum((weights[i] for i in range(J) if mask & (1<<i)), Fraction(0))
        result += p*weight**n
    return result

for n in range(1, 8):
    for J in (5, 7):
        lower = finite_lower_bound(n, J)
        check(lower >= 0)
        check(lower <= 1)
        # Probability any of 2n labels lies outside the retained J boxes.
        omitted_bound = Fraction(2*n, 2**J)
        bigger = finite_lower_bound(n, J+1)
        check(lower <= bigger)
        check(bigger-lower <= omitted_bound)

# Check the finite product identity and its limit for representative t.
for t in (0.125, 0.5, 1, 2, 4, 16):
    theoretical_mean = 1-exp(-t)
    theoretical_void = (1+exp(-t)+exp(-2*t))/3
    for J in (16, 32, 56):
        a = [exp(-t*2.0**(-j))-exp(-t*2.0**(-(j-1)))
             for j in range(1, J+1)]
        check(abs(sum(a)-(exp(-t*2.0**(-J))-exp(-t))) < 5e-13)
        void_direct = prod(1-x for x in a)
        void_finite = (expm1(-3*t)/expm1(-t)) * (expm1(-t*2.0**(-J))/expm1(-3*t*2.0**(-J)))
        check(abs(void_direct-void_finite) < 5e-7)
        if J == 56:
            check(abs(sum(a)-theoretical_mean) < 1e-12)
            check(abs(void_direct-theoretical_void) < 1e-12)

# The bi-infinite phase law has mean 1 and probability of zero equal to 1/3.
for v in (1.0, 1.125, 1.5, 1.875, 2.0):
    a = [exp(-v*2.0**(-k)) - exp(-2*v*2.0**(-k))
         for k in range(-18, 56)]
    check(abs(sum(a)-1) < 5e-12)
    check(abs(prod(1-p for p in a)-Fraction(1, 3)) < 5e-12)
    check(0 < sum(p*(1-p) for p in a) < 1)

print(f"{CHECKS} finite exact/algebraic and numerical checks passed")
