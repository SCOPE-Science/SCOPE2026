"""Lindeberg-vs-truncation tradeoff ledger for the Pareto-4.5 target.

Exact algebra (Fractions) + verified numerics. Convention (labeled, standard):
entrywise Lindeberg to 4th order (first 3 moments matched exactly by symmetry,
4th up to truncation error handled separately); per off-diagonal swap Taylor
integral remainder with sup 5th entrywise derivative D5:

  E_comp <= M5(T) * D5 / (120 N^{1/2}),   M5(T) = E|xi|^5 1_{|xi|<=T} <= C_M5 T^{1/2}

summed over N^2/2 swaps (diagonal: N swaps, lower order, noted). Budgeting
E_comp <= N^{-1/18}/3 gives the REQUIRED derivative bound

  D5 <= D5*(tau) := 40 N^{4/9 - tau/2} / C_M5   [since 1/(3/120)=40]

while coincidence needs tau >= 37/81. The script prints the tradeoff curve and
the naive-local-law scale gap Q^2/N vs needed smoothing eta* = N^{-13/18}:
gap exponent exactly 103/162. Conclusion lines are quantitative inputs to the
WORKLOG obstruction candidate E1; the DBM-regularized route is NOT covered by
this ledger (D5 there is tamed by Gaussian convolution, still main effort).
"""
from fractions import Fraction
import math
import sys

ALPHA = Fraction(9, 2)
XM = math.sqrt(5.0) / 3.0
C_TAIL = XM ** 4.5
C_M5 = 9.0 * C_TAIL  # ~2.3976

# exact gap identity: (Q^2/N) / eta* with Q=N^{37/81}, eta*=N^{-13/18} -> N^{103/162}
assert Fraction(2 * 37, 81) - 1 + Fraction(13, 18) == Fraction(103, 162)
print(f"scale-gap exponent = 103/162 = {103/162:.6f}")

def trunc_exp(tau):
    return 2 - 4.5 * tau  # P(fail) ~ N^{this}

def d5_exp(tau):
    return float(Fraction(4, 9) - tau / 2)  # D5* ~ N^{this}

print(f"{'tau':>10} {'trunc-err':>12} {'D5*-exp':>10} {'D5*(N=1e6)':>12}")
for tau in (Fraction(37, 81), Fraction(47, 100), Fraction(1, 2)):
    te = trunc_exp(float(tau))
    de = d5_exp(tau)
    d5val = 40.0 / C_M5 * (1e6 ** de)
    flag = " <- coincidence threshold" if tau == Fraction(37, 81) else ""
    print(f"{float(tau):>10.6f} N^{te:>+8.4f}  N^{de:>+7.4f}  {d5val:.3e}{flag}")
    if tau == Fraction(37, 81):
        assert abs(te - (-1.0 / 18.0)) < 1e-12
        assert abs(de - float(Fraction(35, 162))) < 1e-12

# At tau=37/81: D5* = (40/C_M5) N^{35/162}; print prefactor
pref = 40.0 / C_M5
print(f"D5*(37/81) = {pref:.4f} N^(35/162) = {pref:.4f} N^{float(Fraction(35,162)):.6f}")
assert 16.0 < pref < 17.5

# Scale gap at N=1e6: Q^2/N vs eta*
N = 1e6
Q2ovN = N ** (float(Fraction(2 * 37, 81)) - 1)
eta_star = N ** (-13.0 / 18.0)
print(f"N=1e6: Q^2/N = {Q2ovN:.3e}, eta* = {eta_star:.3e}, ratio = {Q2ovN/eta_star:.3e}")
assert abs(math.log(Q2ovN / eta_star) / math.log(N) - 103.0 / 162.0) < 1e-9

print("LINDEBERG_LEDGER_OK")
sys.exit(0)
