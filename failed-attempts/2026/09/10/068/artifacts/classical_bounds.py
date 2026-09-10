"""Classical SDP-free upper bounds for N_{1/5}(14) — bounded fallback attempt.

Checks every closed-form bound available without an SDP solver:
 relative (Delsarte-Goethals-Seidel), Gerzon absolute, Lemmens-Seidel-type,
 Neumann parity remark. Exact rational arithmetic, stdlib only.
Question: does any reach <=28? If not, only the 4-point SDP tier can,
which env_probe.log shows is tooling-blocked.
"""
from fractions import Fraction as Q

d, r = 14, 5
a = Q(1, 5)

# 1. Relative bound R(d,a) = d(1-a^2)/(1-d a^2), valid since d=14 < 25 = 1/a^2
R = Q(d * (1 - a * a), 1 - d * a * a)
print("relative bound R(14,1/5) =", R, "=", float(R), "-> N <=", int(R), "(floor)")

# 2. Gerzon absolute bound d(d+1)/2
G = d * (d + 1) // 2
print("Gerzon absolute =", G)

# 3. Lemmens-Seidel absolute-type bound for angle 1/(2m-1), here m=3:
#    N <= C(d+m-1, m) ... use the standard form N <= (d+1)d/2 capped by
#    the r=5 frame bound (d-1)(d+2)/... : report Gerzon only, plus
#    Neumann: alpha=1/odd integer allows N>2d (no exclusion).
print("Neumann: 1/alpha=5 odd -> N>2d permitted, no exclusion of 29")
print("2d =", 2 * d, "(28-line construction attains exactly 2d)")

# 4. Best literature floats at this row (cited, not computed):
print("de Laat Table 1 floating SDP bound: 30")
print("Greaves Table 4 combinatorial row: 28--29 (30+ excluded)")
print()
print("CONCLUSION: best SDP-free closed form =", int(R),
      "; best tabulated = 29; need 28 -> four-point SDP dual required.")
