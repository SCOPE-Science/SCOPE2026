"""Independent finite checks for a quadratic binary valuation theorem.
Only the Python standard library is required. These checks are not an infinite proof.
"""
from math import comb
from fractions import Fraction

def v2int(n):
    if not n:
        return None
    return (abs(n) & -abs(n)).bit_length() - 1

def v2frac(q):
    return v2int(q.numerator) - v2int(q.denominator)

def direct(n, t):
    return sum(comb(n, j)**2 * (2*t)**j for j in range(n+1))

def recurrence_values(limit, t):
    if limit == 0:
        return [1]
    values = [1, 1 + 2*t]
    for n in range(1, limit):
        a = (2*n+1)*(1+2*t)*values[n] - n*(1-2*t)**2*values[n-1]
        assert a % (n+1) == 0
        values.append(a // (n+1))
    return values

valtests = 0
directtests = 0
for t in range(-41, 42):
    if t % 4 != 3:
        continue
    values = recurrence_values(280, t)
    for n in range(0, 45):
        assert values[n] == direct(n, t)
        directtests += 1
    for n in range(8, 281, 8):
        assert v2int(values[n]-1) == 2*v2int(n)+2, (t, n)
        valtests += 1

# A(t)=sum_{k>=1}(2t)^k/k^2. Terms with k>=9 are zero modulo 8.
for t in (3, 7, -1, -5):
    A = 0
    for k in range(1, 9):
        a = v2int(k)
        e = k-2*a
        if e >= 3:
            continue
        odd = k // 2**a
        A += (2**e * pow(odd*odd, -1, 8) * pow(t, k, 8)) % 8
    assert A % 8 == 4, (t, A)

# Verify the needed finite polynomial-tail divisibility for k=1,...,8.
for k in range(1, 9):
    coeff = [Fraction(1)]
    for i in range(1, k):
        new = [Fraction(0)] * (len(coeff)+2)
        for j, c in enumerate(coeff):
            new[j] += c
            new[j+1] -= 16*c/i
            new[j+2] += 64*c/(i*i)
        coeff = new
    baseline = Fraction(64*2**k, k*k)
    for j in range(1, len(coeff)):
        if coeff[j]:
            assert v2frac(baseline*coeff[j]) >= 9, (k, j)

# For k>=9 all coefficients are divisible by 512. Bound tends to infinity.
for k in range(9, 4097):
    T = sum((k-1)//(2**r) for r in range(4, k.bit_length()+1))
    bound = 6+k-2*v2int(k)-2*T
    assert bound >= 9, (k, bound)

assert v2int(direct(4, 3)-1) == 11  # Sharp cutoff: the 4-divisible layer differs.
print('VERIFY_OK valuation_pairs=',valtests,'direct_recurrence_pairs=',directtests,
      'finite_coefficient_tests=8','tail_bound_indices=4088')
