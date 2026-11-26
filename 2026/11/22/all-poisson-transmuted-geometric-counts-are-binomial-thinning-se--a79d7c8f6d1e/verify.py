"""Exact rational regressions for the innovation formulas in RESULT.md."""
from fractions import Fraction as F


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def thinned(x, c):
    return x * c / (1 - (1-c)*x)


def ratio_polynomials(q, a, c):
    r = q*(q+a)/(1+a*q)
    l = lambda x: [F(1), -x]
    lc = lambda x: [1-(1-c)*x, -c*x]
    return mul(l(r), mul(lc(q), lc(q*q))), mul(lc(r), mul(l(q), l(q*q)))


q, a, c = F(1, 2), F(1, 2), F(2, 5)
n, d = ratio_polynomials(q, a, c)
rates = [F(1, 2), F(1, 4), F(4, 19)]
weights = [F(39, 110), -F(3, 10), F(6, 11)]
ds = [[F(1), -x] for x in rates]
den = mul(ds[0], mul(ds[1], ds[2]))
num = [c * x for x in den]
for i, (rate, weight) in enumerate(zip(rates, weights)):
    j, k = [j for j in range(3) if j != i]
    for t, x in enumerate(mul(ds[j], ds[k])):
        num[t] += weight * (1-rate) * x
assert mul(num, d) == mul(n, den)
r = F(-4, 11)
assert q**3 + q**6 - r**3 - (q**2 + q**4 - r**2) == F(719, 85184)

cases = 0
for q in (F(1, 50), F(1, 5), F(1, 2), F(9, 10)):
    for a in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
        for c in (F(1, 10), F(2, 5), F(1, 2), F(99, 100)):
            n, d = ratio_polynomials(q, a, c)
            r = q*(q+a)/(1+a*q)
            # The logarithmic derivative is n'/n - d'/d, independently
            # of the exponential Poisson summand (which adds only at j=1).
            nd = [i*n[i] for i in range(1, len(n))]
            dd = [i*d[i] for i in range(1, len(d))]
            numer = [x-y for x, y in zip(mul(nd, d), mul(dd, n))]
            denom = mul(n, d)
            logder = []
            for j in range(1, 15):
                rhs = numer[j-1] if j <= len(numer) else F(0)
                rhs -= sum(denom[i]*logder[j-1-i] for i in range(1, min(j, len(denom))))
                v = rhs / denom[0]
                logder.append(v)
                v0 = lambda k: q**k + q**(2*k) - r**k
                expected = v0(j) - (thinned(q,c)**j + thinned(q*q,c)**j - thinned(r,c)**j)
                assert v == expected >= (v0(j)-v0(j+1))*(1-c**j) > 0
                cases += 1
print(f"PASS: exact witnesses and {cases} innovation coefficient checks")
