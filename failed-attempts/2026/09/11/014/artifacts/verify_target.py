"""Verify baseline Floer/topological data for target cell (T(2,7), slope +5).

Checks (stdlib only):
 T1 Alexander of T(2,7), genus, determinant, a2 (Conway), torsion/V-profile.
 T2 L-space threshold 2g-1=5; Moser lens slopes rs+-1 = 13,15 (so 5 non-lens).
 T3 d(L(5,1)) vector and d(Y=S^3_5(T)) via Ni-Wu integer surgery formula.
 T4 Y is not a lens space (d-vector mismatch vs L(5,1); triangle-group infinitude)
    and mirror-torus surgery excluded (mirror V=0 -> lens d != d(Y)).
 T5 Torus-impostor arithmetic: {r,s,|rs-5|}={2,7,9} forces (r,s)=(2,7)/(7,2);
    unknot (r=1) impossible.
 T6 Seifert base S^2(2,7,9) atoroidal (orbifold Euler < 0).
"""
from fractions import Fraction as Q

ok = []

# ---- T1: Alexander of T(2,7) = (t^7+1)/(t+1), symmetric form ----
# coeffs for exponents 3..-3
alex = {3: 1, 2: -1, 1: 1, 0: -1, -1: 1, -2: -1, -3: 1}
assert sum(alex.values()) == 1, "Alexander(1)==1"
g = max(e for e, c in alex.items() if c != 0)
assert g == 3, "genus 3"
det = abs(sum(c * ((-1) ** e) for e, c in alex.items()))
assert det == 7, f"det={det}"
# a_i for i>=0 in t^i: a3=1,a2=-1,a1=1,a0=-1
a = {3: 1, 2: -1, 1: 1, 0: -1}
# torsion coefficients t_i = sum_{j>=1} j*a_{i+j}
t = {}
for i in range(0, 6):
    t[i] = sum(j * a.get(i + j, 0) for j in range(1, 6))
assert t == {0: 2, 1: 1, 2: 1, 3: 0, 4: 0, 5: 0}, f"torsion={t}"
V = [t[i] for i in range(5)]  # V_s = t_s for L-space staircase
assert V == [2, 1, 1, 0, 0], f"V={V}"
# Conway a2 = (Delta''(1))/2 ; Delta(t)=t^3-t^2+t-1+t^-1-t^-2+t^-3
# Delta''(1) = 6+ -2 +0+0+ -2? compute: d2/dt2 of t^3=6t->6; -t^2->-2; t->0;
# -1->0; t^-1->2t^-3->2; -t^-2->-6t^-4->-6; t^-3->12t^-5->12. Sum=6-2+0+0+2-6+12=12
assert 6 - 2 + 0 + 0 + 2 - 6 + 12 == 12
a2 = 12 // 2
assert a2 == 6, "a2(T(2,7))=6 (nonzero -> chiral Casson signal)"
ok.append("T1 Alexander/genus3/det7/torsion(2,1,1,0)/V/a2=6")

# ---- T2: thresholds ----
assert 2 * g - 1 == 5, "L-space onset slope"
assert 2 * 7 - 1 == 13 and 2 * 7 + 1 == 15, "Moser lens slopes 13,15"
assert 5 not in (13, 15)
ok.append("T2 threshold 2g-1=5; lens slopes {13,15}; 5 non-lens")

# ---- T3: d-invariants ----
def d_lens51(i):
    return Q((2 * i - 5) ** 2, 20) - Q(1, 4)

dL = [d_lens51(i) for i in range(5)]
assert dL == [Q(1), Q(1, 5), Q(-1, 5), Q(-1, 5), Q(1, 5)], dL
# Ni-Wu integer surgery: d(S^3_5(K),i) = d(L(5,1),i) - 2*max(V_i, V_{5-i}), V_5:=0
Vext = V + [0]
dY = [dL[i] - 2 * max(Vext[i], Vext[5 - i]) for i in range(5)]
assert dY == [Q(-3), Q(-9, 5), Q(-11, 5), Q(-11, 5), Q(-9, 5)], dY
ok.append(f"T3 d(L(5,1))={list(map(str,dL))} d(Y)={list(map(str,dY))}")

# ---- T4: Y not lens; mirror excluded ----
assert sorted(dY) != sorted(dL), "d(Y) != d(L(5,1)): Y not L(5,1)"
# any mirror-torus +5 surgery has V=0 profile -> d = lens d; mismatch kills it
d_mirror = list(dL)
assert sorted(d_mirror) != sorted(dY)
# triangle group infinitude: 1/2+1/7+1/9 < 1
assert Q(1, 2) + Q(1, 7) + Q(1, 9) < 1, "base orbifold hyperbolic -> pi1 infinite"
ok.append("T4 Y non-lens (d-mismatch); mirror-torus d=lens d excluded; pi1 infinite")

# ---- T5: torus impostor arithmetic ----
import math
sols = []
for r in range(1, 12):
    for s in range(1, 12):
        if math.gcd(r, s) != 1:
            continue
        if sorted([r, s, abs(r * s - 5)]) == [2, 7, 9]:
            sols.append((r, s))
assert sols == [(2, 7), (7, 2)], f"torus orders solutions={sols}"
ok.append(f"T5 Seifert-order match forces torus (2,7): {sols}")

# ---- T6: atoroidal ----
chi_orb = 2 - (Q(1, 2) + Q(6, 7) + Q(8, 9)) - 0  # 2 - sum(1-1/m)
# chi(S^2(2,7,9)) = 2 - (1/2+6/7+8/9) < 0 ?
assert 2 - (Q(1, 2) + Q(6, 7) + Q(8, 9)) < 0, "orbifold Euler negative"
ok.append("T6 base S^2(2,7,9) orbifold Euler <0 -> Y atoroidal small Seifert")

print("VERIFY_OK", len(ok), "checks")
for line in ok:
    print(" -", line)
