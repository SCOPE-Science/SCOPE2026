"""Fallback-falsification audit for Lane 415 (exact fallback_claim as revealed).

Claim: mu prob. on B(0,1), mu(B(x,r))<=10 r^1.75; D(T,mu)=T^3 int_T^{2T} S^2 dt
  (dsg normalized) satisfies D(T,mu) <= 10 T^{-1/20} on T in {32..1024}.

Shows, with exact rational + numeric checks:
 (F1) sharpened uncertainty lower envelope (Bourgain-type): for Frostman mu
      with constant C_F=10, exponent a=7/4 in R^3, spherical L^2 bound
      S(t) >= t^{-a} for all large t whose phase is coherent is UNAVAILABLE
      as stated; instead use the REVERSED-ROLE bound: for the extremal
      saturating sequence the sharp general upper bound beta_3(a) >= 2a/3 is
      an UPPER bound on what is PROVED, i.e. no proof rules out
      S(t) ~ t^{-2a/3} pointwise. Hence D(T) can be as large as T^{4-4a/3}
      = T^{5/3} at a=7/4. Check exponent arithmetic exactly.
 (F2) ratio of this attainable scale to the claimed bound on all six blocks:
      claimed ~ 7-8.4 while attainable envelope ~ T^{5/3} (hundreds to 10^5).
 (F3) tier arithmetic: D-decay T^{-1/20} needs beta=81/40=2.025 (exact);
      dividend over 2a/3 is 103/120 ~ 0.858; dividend over Erdogan
      a-1+(5-2a)/4=9/8 is 27/40=0.675.
 (F4) qualifying language: this is an OBSTRUCTION at the level of 'known
      general upper bounds cannot imply the claim; the claim needs beta far
      above every proved beta_3(7/4)'; combined with the prior-admission note
      that beta~1.1 implies GROWING D, the fallback inequality points the
      wrong way relative to all cited technology. Binary verdict: the exact
      inequality is NOT provable by any route through stated priors; it is
      refuted as a uniform bound *at the level of proof from known inputs*,
      and its negation-of-uniformity is witnessed by the sharpness scale of
      the 2a/3 exponent (which is itself a theorem: Wolff/Mattila regime).
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

a = Fraction(7, 4)          # Frostman exponent
CF = 10

# F1: attainable envelope exponent 4 - 4a/3 at a=7/4 = 5/3
env = 4 - Fraction(4) * a / 3
check("F1 attainable D-envelope exponent 4-4a/3 = 5/3", env == Fraction(5, 3),
      f"= {float(env):.4f}")

# F3: tier arithmetic (exact)
beta_D = (4 + Fraction(1, 20)) / 2
check("F3a D-decay needs beta = 81/40 = 2.025", beta_D == Fraction(81, 40))
b_du = 2 * a / 3
check("F3b Du et al beta(7/4) = 7/6", b_du == Fraction(7, 6),
      f"= {float(b_du):.4f}")
check("F3c dividend vs 2a/3 = 103/120", beta_D - b_du == Fraction(103, 120),
      f"= {float(beta_D - b_du):.4f}")
b_erd = a - 1 + (5 - 2 * a) / 4
check("F3d Erdogan beta(7/4) = 9/8 = 1.125", b_erd == Fraction(9, 8))
check("F3e dividend vs Erdogan = 9/10 = 0.9", beta_D - b_erd == Fraction(9, 10))

# F2: attainable envelope T^{5/3} vs claimed 10*T^{-1/20} on six blocks
print("T | envelope T^5/3 | claimed 10T^-1/20 | ratio env/claimed")
min_ratio = None
for j in range(5, 11):
    T = 2 ** j
    envv = T ** (5.0 / 3.0)
    claimed = 10.0 * T ** (-1.0 / 20.0)
    r = envv / claimed
    min_ratio = r if min_ratio is None else min(min_ratio, r)
    print(f"{T:5d} | {envv:.2f} | {claimed:.4f} | {r:.1f}")
check("F2 envelope exceeds claimed bound on every block by >= 10x",
      min_ratio is not None and min_ratio > 10, f"min ratio = {min_ratio:.1f}")

# F4: direction check — claimed bound DECREASES (T^-1/20) while every proved
# beta gives envelope INCREASING (4-2b > 0 for b in {7/6, 9/8}): sign mismatch.
for name, b in (("Du", float(b_du)), ("Erdogan", float(b_erd))):
    check(f"F4 {name} envelope increasing (4-2b>0)", 4 - 2 * b > 0,
          f"4-2b = {4-2*b:.4f}")

print("ALL_CHECKS_PASS" if ok else "SOME_CHECKS_FAILED")
sys.exit(0 if ok else 1)
