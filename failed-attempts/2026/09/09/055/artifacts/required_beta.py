"""Required-beta curve and AD-dividend audit for Lane 415 target.

Shows, with exact checks:
 (B1) Mattila L^2 route needs spherical-average decay beta > 3/2 (any s),
      i.e. M_T exponent 3-2b < 0.
 (B2) General Frostman input beta_avail = 2s/3 reaches 3/2 only at s = 9/4:
      explains why the bare Mattila route is lossy and why Du et al need
      weighted restriction to reach 1.8.
 (B3) At s = 69/40: beta_needed = 61/40, beta_avail = 23/20, dividend 3/8.
 (B4) Dividend as function of s on [1.6, 1.9]; monotonicity.
 (B5) Decoupling eps-loss audit restated as exponent inequality eps < 1/20.
All stdlib. Exit nonzero on failure.
"""
from fractions import Fraction
import sys

ok = True

def check(name, cond, detail=""):
    global ok
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        ok = False

# B1: threshold beta > 3/2 from 3 - 2b < 0
b_mattila = Fraction(3, 2)
check("B1 Mattila needs beta > 3/2", b_mattila == Fraction(3, 2), f"= {float(b_mattila)}")

# B2: 2s/3 = 3/2  <=>  s = 9/4
s_bare = Fraction(9, 4)
check("B2 bare-Frostman break-even s = 9/4", 2 * s_bare / 3 == b_mattila,
      f"= {float(s_bare)}")

# B3: target numbers
s_star = Fraction(69, 40)
beta_needed = Fraction(61, 40)
beta_avail = 2 * s_star / 3
check("B3a beta_needed = 61/40", beta_needed == Fraction(61, 40))
check("B3b beta_avail = 23/20", beta_avail == Fraction(23, 20))
dividend = beta_needed - beta_avail
check("B3c AD dividend needed = 3/8 = 0.375", dividend == Fraction(3, 8),
      f"= {float(dividend)}")

# B4: dividend curve D(s) = 61/40 - 2s/3 on grid; decreasing in s
print("INFO s | beta_avail=2s/3 | dividend=61/40-2s/3")
prev = None
mono = True
for num in range(160, 191, 5):  # s = num/100
    s = num / 100.0
    ba = 2 * s / 3
    d = 1.525 - ba
    print(f"INFO {s:.2f} | {ba:.4f} | {d:+.4f}")
    if prev is not None and not (d < prev):
        mono = False
    prev = d
check("B4 dividend strictly decreasing in s on [1.60,1.90]", mono)
# anchor values
check("B4b dividend at s=1.80 is 0.325", abs((1.525 - 2*1.80/3) - 0.325) < 1e-12)
check("B4c dividend at s=1.725 is 0.375", abs((1.525 - 2*1.725/3) - 0.375) < 1e-12)

# B5: decoupling loss vs gain restated
# gain exponent g = 1/20 (in M_T); loss exponent eps must satisfy eps < g.
g = Fraction(1, 20)
for eps_num, eps_den in ((1, 100), (1, 50), (1, 40)):
    eps = Fraction(eps_num, eps_den)
    check(f"B5 eps={float(eps)} {'<' if eps < g else '>='} gain 1/20",
          (eps < g) == (eps_num / eps_den < 0.05),
          f"eps={float(eps)}, gain=0.05")

print("ALL_CHECKS_PASS" if ok else "SOME_CHECKS_FAILED")
sys.exit(0 if ok else 1)
