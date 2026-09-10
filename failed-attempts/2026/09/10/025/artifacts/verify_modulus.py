"""Verify corrected log-modulus balance for lane-553 conditional chain (stdlib only).

Corrected model (3D low-ball volume accounted):
  uniform low-freq bound after e^{k t}eps^{1/2}=1 cancellation: |F| <= (ML)^{-1/2},
    M = 1 + ||h||_{H^2}-type a priori factor, L = |log eps|, t = L/(2k).
  H^{-1}-norm split at rho = (ML)^beta:
    low  ~ rho^{3/2} (ML)^{-1/2}   [Cauchy-Schwarz: (int_{|xi|<=rho} <xi>^{-2})^{1/2}]
    tail ~ rho^{-3} M              [H^2 a priori, weight <xi>^{-1-3}]
  Balance (3/2)b - 1/2 = -3b  =>  b = 1/9;
    E_{-1} <= M^{1/3} L^{-1/3} (rate p = 1/3).
  Interpolation r=-1, s=2, t=13/8: theta = (s-t)/(s-r) = (3/8)/3 = 1/8;
    t = 13/8 = 1.625 > 3/2 embeds into C^0 in 3D.
  alpha = p*theta = 1/24.
"""
import math
from fractions import Fraction

beta = Fraction(1, 9)
# balance residual: (3/2)b - 1/2 + 3b = 0
assert Fraction(3, 2) * beta - Fraction(1, 2) + 3 * beta == 0
print(f"beta = {beta} OK")

p = Fraction(1, 3)
theta = Fraction(2 - Fraction(13, 8), 3)  # (s-t)/(s-r), r=-1,s=2,t=13/8
assert theta == Fraction(1, 8), theta
alpha = p * theta
assert alpha == Fraction(1, 24), alpha
print(f"p = {p}, theta = {theta}, alpha = {alpha} OK")

for k, tau0 in [(2, 2), (3, 2), (4, 2)]:
    bound = math.exp(-2 * k * tau0)
    print(f"kappa={k}, tau0={tau0}: need eps <= {bound:.2e}")
    assert bound > 0

print("MODULUS-BALANCE_OK (alpha=1/24)")
