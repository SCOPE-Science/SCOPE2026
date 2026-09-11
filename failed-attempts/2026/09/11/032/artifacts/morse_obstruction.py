"""Recovery/obstruction test for lane-754 target (order-3 invariant jets on sextic threefold).

Uses published leading-term formulae (Rousseau/Merker):
  chi(X_d, E_{3,m}^3 T*) = m^9/(81648000000) * d * p(d) + O(m^8),
    p(d) = 389 d^3 - 20739 d^2 + 185559 d - 358873   (chi>0 iff p(d)>0)
  h^2(X_d, E_{3,m}^3 T*) <= m^9 * 49403/(252*10^7) * d(d+13) + O(m^8)
  h^0 >= chi - h^2 = m^9/(408240000000) * d * q(d) + O(m^8),
    q(d) = 1945 d^3 - 103695 d^2 - 7075491 d - 105837083.
Checks: chi-positivity at d=6 (tiny positive), h2-dominance ratio R(6)~331,
h0-lower negativity at d=6, and threshold root of q in (96,97) => d>=97.
"""
from fractions import Fraction as F
def p(d): return 389*d**3-20739*d**2+185559*d-358873
def q(d): return 1945*d**3-103695*d**2-7075491*d-105837083
def chi9(d): return F(d*p(d), 81648000000)
def h2_9(d): return F(49403*d*(d+13), 2520000000)
def h0_9(d): return F(d*q(d), 408240000000)
ok = True
# 1. chi leading coeff at d=6 is positive but tiny
assert p(6) == 91901 and chi9(6) > 0, "chi(6) should be tiny-positive"
# 2. h2 upper bound dominates chi at d=6 by factor > 330
R6 = h2_9(6)/chi9(6)
assert R6 > 330, f"R(6)={float(R6)}"
# 3. h0 lower bound negative at d=6 and throughout 6<=d<=96
for d in [6,8,10,29,43,72,96]:
    assert h0_9(d) < 0, f"h0lower({d}) should be <0"
# 4. threshold: q(96)<0<q(97), so certified h0>0-route needs d>=97
assert q(96) < 0 < q(97), "threshold bracket failed"
assert h0_9(97) > 0, "h0lower(97) should be >0"
print(f"chi9(6)={float(chi9(6)):.6e} h2_9(6)={float(h2_9(6)):.6e} h0lower9(6)={float(h0_9(6)):.6e}")
print(f"R(6)={float(R6):.3f} (h2 bound exceeds chi by ~331x)")
print(f"q(96)={q(96)} q(97)={q(97)} => order-3 Rousseau route certifies h0>0 only for d>=97")
print("MORSE_OBSTRUCTION_OK")
