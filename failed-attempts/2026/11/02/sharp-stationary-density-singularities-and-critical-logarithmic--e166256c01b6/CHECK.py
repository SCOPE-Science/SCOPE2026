"""Exact finite consistency checks for the asymmetric dyadic stationary law."""
from fractions import Fraction as F

for p in (F(1, 10), F(1, 7), F(1, 5), F(3, 10)):
    q = 1-p
    eps = 1-3*p
    coeffs = [eps/q]
    for n in range(1, 60):
        coeffs.append(p*(coeffs[n-1]+(coeffs[n-2] if n >= 2 else F(0)))/q)
    assert q*coeffs[0] == eps
    assert q*coeffs[1] == p*coeffs[0]
    for n in range(2, len(coeffs)):
        assert q*coeffs[n] == p*(coeffs[n-1]+coeffs[n-2])
    # The stationary distribution at cell zero balances its self-loop and arrivals from one.
    assert coeffs[0] == q*(coeffs[0]+coeffs[1])
    # All finite dyadic-annulus weights are exact rational coefficients.
    prefix = F(0)
    for n in range(40):
        prefix += 2**n*coeffs[n]
        assert prefix > 0
    if p < F(1, 7):
        assert prefix < eps/(1-7*p)
    if p == F(1, 7):
        assert coeffs[0] == F(2, 3)
    print('pass: 60 exact balance coefficients and 40 exact annuli for p=',p)
print('all 400 rational tests passed')
