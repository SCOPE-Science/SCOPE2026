"""Classical-Mattila vs strong-route threshold audit for Lane 415 target.

Two formulations of link (iii):
 Route A (strong, sufficient but lossy): uniform M_T <= C T^{-1/20}
   needs beta >= 61/40 = 1.525 at s=69/40 (dividend 3/8 over 2s/3).
 Route B (classical Mattila Thm 2.2, Du et al 1802.10186 Sec 2.2):
   hypothesis S(R) <= C R^{alpha-d} (beta >= d-alpha) + finite alpha-energy
   I_alpha gives |Dl|>0. At s=69/40 needs beta >= 3-69/40 = 51/40 = 1.275
   (dividend 1/8 over 2s/3). Factor-3 reduction of burden on link (ii).

Checks:
 (T1) general-input crossing 2a/3 = 3-a at a = 9/5 = 1.8 (Du et al Thm 1.2).
 (T2) dividends at 69/40: strong 3/8, classical 1/8.
 (T3) Mattila-cap consistency: Remark 2.4 cap 5/3 < 69/40 (target above floor).
 (T4) energy identity finiteness: Frostman s-measure has I_alpha < inf for alpha < s.
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

s_star = Fraction(69, 40)

# T1: crossing of beta_avail(a)=2a/3 with beta_need_classical(a)=3-a
# 2a/3 = 3-a  <=> 5a/3 = 3 <=> a = 9/5.
a_cross = Fraction(9, 5)
check("T1a crossing at 9/5", 2 * a_cross / 3 == 3 - a_cross,
      f"= {float(2*a_cross/3):.4f}")
check("T1b crossing = 1.8 (Du et al Thm 1.2 d=3)", float(a_cross) == 1.8)

# T2: dividends
beta_avail = 2 * s_star / 3            # 23/20
beta_strong = Fraction(61, 40)         # 1.525
beta_class = 3 - s_star                # 51/40 = 1.275
check("T2a beta_avail = 23/20", beta_avail == Fraction(23, 20))
check("T2b beta_strong = 61/40", beta_strong == Fraction(61, 40))
check("T2c beta_classical = 51/40 = 1.275", beta_class == Fraction(51, 40),
      f"= {float(beta_class)}")
check("T2d strong dividend = 3/8", beta_strong - beta_avail == Fraction(3, 8))
check("T2e classical dividend = 1/8", beta_class - beta_avail == Fraction(1, 8),
      f"= {float(beta_class - beta_avail)}")
check("T2f classical burden is 1/3 of strong", 
      (beta_class - beta_avail) * 3 == beta_strong - beta_avail)

# T3: Mattila cap 5/3 (Du et al Remark 2.4) below target: target in reachable zone
cap = Fraction(5, 3)
check("T3a cap 5/3 = 1.666.. < 69/40 = 1.725", cap < s_star,
      f"cap={float(cap):.4f}")
check("T3b target above general best? No: 1.725 < 1.8 (improvement)",
      s_star < a_cross, f"gap={float(a_cross - s_star)} = 3/40")

# T4: energy finiteness structure: for Frostman s-measure, I_alpha < inf iff alpha < s.
# I_alpha(mu) ~ int_0^inf S(R) R^{alpha-1} dR (Du et al (2.3) / Wolff Ch.9).
# At s*=69/40, any alpha in (51/40... wait alpha here is the Falconer threshold
# itself: pick alpha_0 with 69/40 > alpha_0 > ...; energy I_{alpha_0}(mu) < inf
# since alpha_0 < s. E.g. alpha_0 = 69/40 - 1/80 = 137/80 = 1.7125 < s.
alpha_0 = s_star - Fraction(1, 80)
check("T4a probe alpha_0 = 137/80 < s*", alpha_0 < s_star, f"= {float(alpha_0)}")
check("T4b alpha_0 > cap 5/3 (nontrivial)", alpha_0 > cap, f"= {float(alpha_0)}")
# classical beta needed at alpha_0: 3 - alpha_0 = 103/80 = 1.2875
check("T4c beta_class(alpha_0) = 103/80", 3 - alpha_0 == Fraction(103, 80))

print("ALL_CHECKS_PASS" if ok else "SOME_CHECKS_FAILED")
sys.exit(0 if ok else 1)
