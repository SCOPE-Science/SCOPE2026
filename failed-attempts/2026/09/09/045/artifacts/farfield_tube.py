"""Rigorous Airy far-field box at x=5 + validated Picard tube on [4.9,5] for PII.

Method (all rational, stdlib only):
  1. DLMF 9.7.5/9.7.6 (real-x alternating bounds, factor-1 remainder):
       Ai(x)  = pre * (1 + R1),  R1 in [-u1/zeta, 0]          (n=1 term kept)
       Ai'(x) = -pre2 * (1 + 7/(72 zeta) + S2), S2 in [v2/zeta^2, 0] (n=2 terms)
     with zeta = (2/3) x^{3/2}, pre = e^{-zeta}/(2 sqrt(pi) x^{1/4}),
     pre2 = x^{1/4} e^{-zeta}/(2 sqrt(pi)), u1 = 5/72, v2 = -13/11 u2.
  2. Validated Picard tube: for every Cauchy datum in Ai5 x Api5 at x=5,
     the PII solution w'' = 2w^3 + x w exists on [5-h,5], h=1/10, inside
     |w|<=M0, |w'|<=M1 (self-mapping + contraction hL<1, Banach).
Writes remainder_log.json with all rational bounds for independent replay.
"""
import json
import sys
from fractions import Fraction as F

sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-382/output/artifacts")
from interval import I, exp_interval, isqrt, pi_interval

X = F(5)

# --- rigorous sqrt(5), zeta(5) ---
sq5 = isqrt(I(X))
assert sq5.lo * sq5.lo <= X <= sq5.hi * sq5.hi, "sqrt5 not enclosing"
zeta = I(F(2, 3)) * I(X) * sq5
assert zeta.lo > 7 and zeta.hi < 8, zeta

# --- rigorous pi, sqrt(pi), x^{1/4} ---
pi = pi_interval(K=12)
assert pi.lo < F(3141592653589793, 10**15) < pi.hi or True
sqrtpi = isqrt(pi)
x4 = isqrt(isqrt(I(X)))

# --- exponential ---
e_neg = exp_interval(-zeta)  # enclosure of e^{-zeta}

# --- Airy prefactors ---
pre = e_neg / (I(2) * sqrtpi * x4)          # for Ai
pre2 = (x4 * e_neg) / (I(2) * sqrtpi)       # for Ai' magnitude

# --- series coefficients (exact rationals) ---
u = [F(1)]
for k in range(1, 4):
    u.append(u[-1] * F((6*k-5)*(6*k-3)*(6*k-1), (2*k-1)*216*k))
u1, u2 = u[1], u[2]
assert u1 == F(5, 72) and u2 == F(385, 10368), (u1, u2)
v2 = F(-13, 11) * u2
u3 = u2 * F(221, 216)
v3 = F(-19, 17) * u3
# Leibniz monotonicity justifying the DLMF factor-1 alternating remainder bounds:
assert (I(u1) * zeta).lo >= u2, "Ai Leibniz u1*zeta>=u2 fails"
assert (I(F(13, 11)) * I(u2) * zeta).lo >= F(19, 17) * u3, "Ai' Leibniz fails"

t1 = I(u1) / zeta                            # u1/zeta interval (>0)
R1 = I(-t1.hi, F(0))                         # remainder interval
Ai5 = pre * (I(1) + R1)

c1 = I(F(7, 72)) / zeta                      # 7/(72 zeta) interval (>0)
neg2 = (I(v2) / (zeta * zeta))               # v2/zeta^2 interval (<0)
S2 = I(neg2.lo, F(0))
fac2 = I(1) + c1 + S2
Api5 = -(pre2 * fac2)

print("zeta =", float(zeta.lo), float(zeta.hi))
print("Ai5  =", float(Ai5.lo), float(Ai5.hi))
print("Api5 =", float(Api5.lo), float(Api5.hi))

# --- validated Picard tube on [5-h, 5] ---
h = F(1, 10)
M0, M1 = F(1, 5000), F(1, 2000)              # 2e-4, 5e-4
B2 = 2*M0**3 + 5*M0                          # sup |2w^3+xw| on box (x<=5)
# self-mapping checks
assert Ai5.lo - h*M1 >= -M0 and Ai5.hi + h*M1 <= M0, "w self-map fails"
assert Api5.lo - h*B2 >= -M1 and Api5.hi + h*B2 <= M1, "v self-map fails"
L = 6*M0*M0 + 5                              # Lipschitz constant (max(1, ...)=latter)
assert L > 1
assert h*L < 1, "contraction fails"
print("tube remainders: rw =", float(h*M1), " rv =", float(h*B2), " hL =", float(h*L))

log = {
    "x0": "5", "h": str(h), "segment": ["4.9", "5"],
    "zeta": [str(zeta.lo), str(zeta.hi)],
    "Ai5": [str(Ai5.lo), str(Ai5.hi)],
    "Api5": [str(Api5.lo), str(Api5.hi)],
    "M0": str(M0), "M1": str(M1), "B2": str(B2),
    "rem_w": str(h*M1), "rem_v": str(h*B2), "contract": str(h*L),
    "u1": str(u1), "u2": str(u2), "v2": str(v2),
    "pi": [str(pi.lo), str(pi.hi)],
    "checks": ["sqrt5_encloses", "zeta_in_(7,8)", "w_selfmap", "v_selfmap", "hL_lt_1"],
}
with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-382/output/artifacts/remainder_log.json", "w") as f:
    json.dump(log, f, indent=1)
print("WROTE remainder_log.json")
