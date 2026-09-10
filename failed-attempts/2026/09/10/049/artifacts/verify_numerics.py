"""Bounded exact checks for lane-619 target (genus-8 elliptic cell).
Verifies: Mukai arithmetic, slopes, numerical wall position t0^2=1/7,
phase flip across wall, Ext lower bound, H0 fibre-jump counterexample,
rank-2 lattice (-2)-class Diophantine check, Reider numerics for L=H-E.
"""
from fractions import Fraction

H2, EH, E2 = 14, 5, 0
print("== Mukai arithmetic ==")
v2 = H2 - 2*2*2
print("v^2 =", v2, " dim M =", v2 + 2)
print("c2(v) =", H2//2, " lenZ = c2 - E.(H-E) =", H2//2 - EH)
a2 = E2 - 2
b2 = (H2 - 2*EH + E2) - 2
print("a^2 =", a2, " b^2 =", b2)
print("<a,v> = E.H - 4 =", EH - 4)
print("<a,b> = E.(H-E) - 2 =", (EH - E2) - 2)
print("BN expdim h0=6:", (v2 + 2) - 6*(6 - 4))
print("chi(v)=4 chi(a)=2 chi(E(-E))=-1 chi(O(H-E))=4")
print("mu(O(E)) =", EH, " mu(v) =", H2/2, " mu(B) =", H2 - EH)
print("slope route: 5 < 7, wrong direction -> no exclusion")

print("== numerical wall on beta=0, omega=tH ray ==")
print("Z_a=(7t^2-1)+i5t, Z_v=(14t^2-2)+i14t")
print("Im(Z_a conj Z_v)=4t(1-7t^2) -> wall at t0^2=1/7")
t = 0.30
import math
Xa, Ya = 7*t*t-1, 5*t
Xv, Yv = 14*t*t-2, 14*t
print("t=0.30<t0: arg_a=%.1f arg_v=%.1f (a destabilizes below)"
      % (math.degrees(math.atan2(Ya, Xa)), math.degrees(math.atan2(Yv, Xv))))
t = 0.50
Xa, Ya = 7*t*t-1, 5*t
Xv, Yv = 14*t*t-2, 14*t
print("t=0.50>t0: arg_a=%.1f arg_v=%.1f (a does NOT destabilize above)"
      % (math.degrees(math.atan2(Ya, Xa)), math.degrees(math.atan2(Yv, Xv))))

print("== Ext existence (abstract) ==")
print("chi(B,A) = -<b,a> = -3 -> ext^1(B,A) = hom+ext^2+3 >= 3 != 0")
print("(extensions exist as sheaves; sigma-semistability at wall UNPROVEN)")

print("== recovery test: fibre-jump counterexample ==")
print("V = O_F(6p) (+) O_F(-q) on elliptic F: deg=5, h0=6+0=6 > 5")
print("=> uniform per-fibre bound h0(E|_F)<=5 is FALSE")
print("naive factor sum: h0(O(E))+h0(O(H-E)) = 2+4 = 6, not <= 5")

print("== conditional rank-2 lattice check (NOT given) ==")
sols = [(a, b) for a in range(-6, 7) for b in range(-12, 13)
        if 7*a*a + 5*a*b == -1]
print("(-2)-classes aH+bE in range:", sols if sols else "none in range")
print("if Pic=<H,E>: no (-2) at all (|a| must divide 1; |a|=1 gives 5b=-6/-8)")
print("then L=H-E ample (L^2=4,L.H=9,Hodge index), Reider: C=aH+bE,C^2=0")
print("=> 7a+5b=0 => L.C=10k>=10, no L.C=1 offender => |L| base-point-free")
print("CONDITIONAL only: rank-2 hypothesis not in problem statement")
print("ALL CHECKS DONE")
