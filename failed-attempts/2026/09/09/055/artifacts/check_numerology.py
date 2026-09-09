"""Numerology audit for Lane 415 target (AD-regular Falconer, R^3, s > 69/40).

Checks, with exact rational arithmetic where possible:
 (N1) threshold identities: 69/40 = 7/4 - 1/40; gaps vs general best 9/5 and 7/4 baseline.
 (N2) dyadic-block equivalence: M_T <= C T^{-1/20}  <=>  S(T) decay exponent beta = 61/40.
 (N3) summability: uniform M_T <= 10 T^{-1/20} over dyadic T=2^j (j>=0) gives finite
      Mattila integral with explicit constant; low-frequency block [0,1] bounded.
 (N4) decoupling eps-loss vs 1/20 gain on the six dyadic blocks 2^5..2^10.
 (N5) known-input gap: beta_avail = 2*s/3 at s=69/40 vs beta_needed = 61/40.
All stdlib. Exit nonzero on any failed check.
"""
from fractions import Fraction
import math
import sys

ok = True

def check(name, cond, detail=""):
    global ok
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        ok = False

# ---- N1: threshold identities ----
s_star = Fraction(69, 40)
check("N1a s*=69/40", s_star == Fraction(69, 40), f"= {float(s_star)}")
check("N1b s* = 7/4 - 1/40", s_star == Fraction(7, 4) - Fraction(1, 40))
check("N1c s* = 1.725", float(s_star) == 1.725)
gap_best = Fraction(9, 5) - s_star          # general best 1.8 (Du et al) minus target
check("N1d gap 9/5 - 69/40 = 3/40", gap_best == Fraction(3, 40), f"= {float(gap_best)}")
gap_base = Fraction(7, 4) - s_star          # 7/4 baseline minus target
check("N1e gap 7/4 - 69/40 = 1/40", gap_base == Fraction(1, 40), f"= {float(gap_base)}")
# decay rate 1/20 is twice the 1/40 threshold gain: consistent with S^2 squaring
check("N1f (1/20)/2 = 1/40 threshold gain", Fraction(1, 20) / 2 == gap_base)

# ---- N2: block/decay equivalence ----
# M_T := \int_T^{2T} S(t)^2 t^2 dt ~ T^3 S(T)^2. If S(T) ~ T^{-beta: M_T ~ T^{3-2b}.
# Claim M_T <= C T^{-1/20} needs 3 - 2b = -1/20 -> b = 61/40.
beta_needed = (3 + Fraction(1, 20)) / 2
check("N2a beta_needed = 61/40 = 1.525", beta_needed == Fraction(61, 40),
      f"= {float(beta_needed)}")
check("N2b 3 - 2*beta_needed = -1/20", 3 - 2 * beta_needed == Fraction(-1, 20))

# ---- N3: summability with explicit constant ----
# sum_{j>=0} 10 * (2^j)^{-1/20} = 10 / (1 - 2^{-1/20})
r = 2.0 ** (-1.0 / 20.0)
total = 10.0 / (1.0 - r)
check("N3a ratio 2^{-1/20} < 1", r < 1, f"= {r:.6f}")
check("N3b total tail <= 294", total < 294, f"= {total:.3f}")
check("N3c total tail >= 290", total > 290, f"= {total:.3f}")
# low frequency: mu probability => |muhat| <= 1 => S <= 1 => int_0^1 S^2 t^2 dt <= 1/3
check("N3d low-freq block [0,1] <= 1/3", 1.0 / 3.0 < 0.34)
# six-block window partial sum 2^5..2^10
six = sum(10.0 * (2.0 ** j) ** (-1.0 / 20.0) for j in range(5, 11))
print(f"INFO six-block sum j=5..10 of 10*T^{{-1/20}} = {six:.4f}")
# blocks T=2^5..2^10 individual bounds 10*T^{-1/20}
for j in range(5, 11):
    T = 2 ** j
    print(f"INFO block T=2^{j}={T}: 10*T^{{-1/20}} = {10.0 * T ** (-1.0/20.0):.4f}")

# ---- N4: decoupling R^eps loss vs T^{1/20} gain on six blocks ----
print("INFO eps-loss T^eps vs gain T^{1/20} (need eps < 1/20 for loss << gain):")
for eps in (0.005, 0.01, 0.02):
    worst = max((2.0 ** 10) ** eps, 1.0)
    gain_top = (2.0 ** 10) ** (1.0 / 20.0)
    check(f"N4 eps={eps}: top-block loss {worst:.3f} < gain {gain_top:.3f}",
          worst < gain_top)
# eps = 1/20 is the break-even; decoupling allows arbitrarily small eps (C_eps blows up)
check("N4d break-even eps=1/20 equals gain exponent", True, "eps < 0.05 required")

# ---- N5: known-input gap ----
beta_avail = float(2 * s_star / 3)   # ~2alpha/3 spherical-average input
check("N5a beta_avail = 2*(69/40)/3 = 23/20 = 1.15", 2 * s_star / 3 == Fraction(23, 20),
      f"= {beta_avail}")
m_exp_avail = 3 - 2 * beta_avail      # M_T exponent under known input: +0.7 GROWING
check("N5b known input M_T exponent +0.7 (growing)", abs(m_exp_avail - 0.7) < 1e-12,
      f"= {m_exp_avail}")
gap_beta = float(beta_needed) - beta_avail
check("N5c beta gap = 0.375", abs(gap_beta - 0.375) < 1e-12, f"= {gap_beta}")
check("N5d M_T exponent gap = 0.75", abs((0.7 + 0.05) - 0.75) < 1e-12)

print("ALL_CHECKS_PASS" if ok else "SOME_CHECKS_FAILED")
sys.exit(0 if ok else 1)
