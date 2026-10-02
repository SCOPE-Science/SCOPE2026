from fractions import Fraction
from math import factorial

def elementary_symmetric(xs):
    e = [Fraction(1)]
    for x in xs:
        e.append(Fraction(0))
        for k in range(len(e)-1, 0, -1):
            e[k] += x * e[k-1]
    return e

def survival_coefficients(p, q, N):
    e = elementary_symmetric(p)
    out = []
    for n in range(N + 1):
        s = Fraction(0)
        for k in range(min(n, len(p)) + 1):
            s += Fraction(factorial(n), factorial(n-k)) * e[k] * (q ** (n-k))
        out.append(s)
    return out

def log_series_from_egf_survival(a):
    # If B(z)=sum_n a_n z^n/n!, return coefficients l_n of log B.
    b = [a[n] / factorial(n) for n in range(len(a))]
    ell = [Fraction(0)] * len(a)
    for n in range(1, len(a)):
        corr = sum((Fraction(k) * ell[k] * b[n-k] for k in range(1, n)), Fraction(0))
        ell[n] = b[n] - corr / Fraction(n)
    return ell

p = [Fraction(2,5), Fraction(1,5), Fraction(1,10)]
q = Fraction(3,10)
assert q + sum(p) == 1

a = survival_coefficients(p, q, 7)
ell = log_series_from_egf_survival(a)

for r in range(2, 8):
    recovered = ((-1) ** (r-1)) * r * ell[r]
    direct = sum(x**r for x in p)
    assert recovered == direct, (r, recovered, direct)

# Directly verify the survival formula for n=0,...,7 by coefficient
# expansion of exp(q z) prod_i(1+p_i z), truncated exactly.
e = elementary_symmetric(p)
for n in range(8):
    coeff = sum(
        e[k] * q**(n-k) / factorial(n-k)
        for k in range(min(n, len(p)) + 1)
    )
    assert factorial(n) * coeff == a[n]

# In the purely discrete case, q=0 and a_n/n! are exactly the
# elementary symmetric polynomials in the atom masses.
p2 = [Fraction(1,2), Fraction(1,3), Fraction(1,6)]
a2 = survival_coefficients(p2, Fraction(0), 4)
e2 = elementary_symmetric(p2)
for n in range(4):
    assert a2[n] == factorial(n) * e2[n]
assert a2[3] > 0 and a2[4] == 0

print("exact rational checks passed")
print("mixed survival a_0..a_7 =", ", ".join(str(x) for x in a))
print("collision powers C_2..C_7 =", ", ".join(
    str(sum(x**r for x in p)) for r in range(2, 8)
))
print("finite discrete support check: a_3 =", a2[3], "and a_4 =", a2[4])
