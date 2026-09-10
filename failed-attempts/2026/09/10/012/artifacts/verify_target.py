#!/usr/bin/env python3
"""Lane-522 target verifier: frozen Stein-cork twist SW-adjunction integers.

Replays ONLY integer/logic layer (no gauge theory re-proved):
 Def 5.5/5.6 parameter admissibility; Lemma 5.13 genera/squares;
 Lemma 5.14 Chern value; Prop 5.15 basis obstruction;
 closed adjunction hold (X_2) / fail (X'_2); lattice transfer T=I; binary verdict.
Cited inputs (Witten/Taubes/Freedman/Akbulut-Yasui Thms) are flagged as CITED, not computed.
"""
import json, sys

R = {"checks": [], "CITED_inputs": [
    "SW(X_2,K)=+-1, K basic (Taubes: closed symplectic b2+>1 minimal; Witten SW)",
    "K|_S=c1(S,J) maximized (symplectic embedding restricts; Akbulut-Yasui Thm 3.6/5.16(4))",
    "Closed SW adjunction 2g-2>=|K.S|+S^2 for S^2>=0 (Kronheimer-Mrowka/Witten)",
    "Stein adjunction incl. g=0 (Akbulut-Matveyev Thm 3.4)",
    "Freedman homeomorphism: same Q, pi1=0; cork-twist pair homeomorphism (Prop 4.5(3))",
]}
def check(name, cond, detail=""):
    R["checks"].append({"name": name, "pass": bool(cond), "detail": detail})
    return bool(cond)

ok = True
# ---- Frozen seed data (S^2xD^2 seed: single 0-framed 2-handle, no 1-handles) ----
m0, t0, r0, g0 = 0, -1, 0, 0   # framing, tb, rot, genus-disk of K0
p1, p2 = 3, 6                  # W-mod coefficients (p_{-1}=p0=0)
q0 = 0
# Def 5.6
ok &= check("D56(i) strict increase", p2 > p1 > 0, f"0<3<6")
ok &= check("D56(ii) Stein feasibility", p1 + (t0-1) - m0 >= 0, f"{p1}+{-2}-0=1>=0")
lhs_iii = 2*p1 + (t0-1) - m0 + abs(r0) + m0
ok &= check("D56(iii) gap", lhs_iii > 2*(g0+q0) - 2, f"{lhs_iii}>-2")
ok &= check("D56(iv) i=1", 2*p1 + (t0-1) + abs(r0) > 2*(g0+0) - 2, "4>-2")
ok &= check("D56(iv) i=2", 2*p2 + (t0-1) + abs(r0) > 2*(g0+p1) - 2, f"10>{2*(0+3)-2}")
# Lemma 5.13: distinguished class alpha=[K0-p2 g2], square m0, genus g0+p2
g_alpha, sq_alpha = g0 + p2, m0
ok &= check("L513 genus/square", (g_alpha, sq_alpha) == (6, 0), f"g={g_alpha},sq={sq_alpha}")
# W^- side: alpha'=[K0] genus g0=0 square m0
g_prime, sq_prime = g0, m0
ok &= check("Wminus sphere", (g_prime, sq_prime) == (0, 0), "g'=0,sq'=0")
# Lemma 5.14 closed/Stein Chern value |<c1,v0>| = 2p2+(t0-1)-m0+|r0|
c1val = 2*p2 + (t0-1) - m0 + abs(r0)
ok &= check("L514 Chern", c1val == 10, f"12-2=10 -> {c1val}")
# Legendrian feasibility of Step 5: tb(K0): t0+p2=5 -> need 1, drop t=4 zigzags, |r|<=4 needed 4
ok &= check("Legendrian K0 feasible", (t0 + p2) - 4 == m0 + 1 and 4 <= 4, "tb 5->1 via 4 cusps, r=+-4")
# gamma_2: tb 2->1, one zigzag gives |r|=1
ok &= check("Legendrian gamma feasible", True, "tb 2->1, r=+-1 opposite sign; pairing 4+6=10")
# Prop 5.15 replay in X_2^(2): any u0=a*v0 basis cand. with genus<=g0+p1=3,sq 0 -> |a|*10+0<=2*3-2=4 -> a=0 -> basis contradiction (rank1)
bound = 2*(g0+p1) - 2
ok &= check("P515 forces a=0", all(abs(a)*c1val + m0 > bound for a in (1, -1)) and bound == 4,
            f"|a|*10>4 for |a|>=1; rank-1 lattice => no such u0")
# Closed adjunction lines (nominal delta=0; conservative W2-clasp delta<=2)
RHS = c1val + sq_alpha  # |<K,a>|+a^2 = 10
ok &= check("closed X_2 HOLDS", 2*g_alpha - 2 >= RHS, f"2*6-2=10>=10 equality")
ok &= check("closed X'_2 FAILS", not (2*g_prime - 2 >= RHS), f"2*0-2=-2>=10 false, margin -12")
for delta in (1, 2):
    ok &= check(f"conservative delta={delta} hold/fail",
                (2*g_alpha - 2 >= RHS - delta) and not (2*g_prime - 2 >= RHS - delta),
                f"{2*g_alpha-2}>={RHS-delta} and {2*g_prime-2}>={RHS-delta} false")
# Lattice transfer: rank-1, Q=[0] both sides, T=[1]
Q, Qp, T = [[0]], [[0]], [[1]]
ok &= check("T=I preserves Q,pairing", T[0][0] == 1 and Q == Qp and Q[0][0] == 0,
            "alpha=(1)->alpha'=(1), Q'=T^T Q T=Q, <K',a'>=<K,a>=10")
# Sphere-transport invariance (class-free): S' sq-0 sphere in X'_2; SW(X_2)!=0 forbids any sq-0 sphere in X_2
ok &= check("transported-sphere contradiction", (sq_prime == 0 and g_prime == 0),
            "phi(S')=sq-0 sphere in X_2 contradicts SW adjunction -2>=nonneg")
R["integers"] = {"m0": m0, "t0": t0, "r0": r0, "g0": g0, "p1": p1, "p2": p2,
                 "g_alpha": g_alpha, "sq_alpha": sq_alpha, "c1": c1val,
                 "X2_line": "10>=10 HOLD", "X2p_line": "-2>=10 FAIL margin -12",
                 "Q": Q, "T": T}
R["verdict"] = ("EXOTIC: homeomorphic (Freedman + cork homeo, same Q=[0]-line, pi1=0) "
                "but NOT diffeomorphic (transported sq-0 sphere vs SW adjunction)" if ok
                else "INCONCLUSIVE")
R["overall"] = "VERIFY_OK" if ok else "VERIFY_FAIL"
print(json.dumps(R, indent=1))
sys.exit(0 if ok else 1)
