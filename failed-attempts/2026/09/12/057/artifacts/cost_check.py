"""Verify the fixed-cost arithmetic for the explicit G_{5/2} model.

Model: Q_n = S_n (factorials), k_0 = 1, k_2 = 1, all other k_n = 0.
Popa-Shlyakhtenko formula: t = 1 + sum_n k_n / |Q_n|.
Cost formula (Cor 3.6): C(G) = 1 + sum_n k_n / |Q_n|.
Expected: t = 1 + 1/1 + 1/2 = 5/2.
"""
from fractions import Fraction
from math import factorial

ks = {0: 1, 2: 1}
t = Fraction(1) + sum(Fraction(k, factorial(n)) for n, k in ks.items())
print("t =", t, "=", float(t))
assert t == Fraction(5, 2), t
print("OK: explicit model has parameter/cost exactly 5/2")
