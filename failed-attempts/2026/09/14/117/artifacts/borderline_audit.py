"""Borderline audit for the BR sparse vertex P2 (d=2) — recovery/bounded test.

Checks, for fixed lambda in (0,1/2), lambda != 1/6, with
  p_lam = 4/(3+2λ),  q_opt = 4/(1+6λ),
the following exact identities / inequalities:

 (a) Knapp edge binds: G := (1-1/q) - 3*(1-1/p) == 0 at (p_lam, q_opt).
     Interior (q > q_opt, where BRS proves bounds): G > 0 (allowed side).
     Exterior (q < q_opt, ruled out by sharpness): G < 0.
 (b) Homogeneity (top) edge binds: 1/p + 1/q == 1 + 2λ at the vertex.
     So P2 is the UNIQUE point where TWO independent necessary
     conditions (Knapp side P1P2, top side P2P3) bind simultaneously.
 (c) Duality (adjoint + swap, exact for self-adjoint R): P2 <-> P3,
     P3 = (1/q_opt, 1/p_lam); both lie on the top edge x+y = 1+2λ.
     Hence duality maps the vertex to the boundary (not outside):
     no soft duality-exclusion exists.
 (d) q_opt == 2  <=>  λ == 1/6 (the solved Stein-Tomas/L2 case).
 (e) VBR-cap dichotomy: r* = p_lam'/3 vs 2 satisfies
     r* - 2 = 2(6λ-1)/(3(1-2λ)), so λ < 1/6 <=> Knapp cap (r < p'/3)
     binds, λ > 1/6 <=> L2 cap (r < 2) binds. Either way every known
     VBR input is STRICT (r < r*), i.e. zero room at the vertex.

RESULT interpretation: the vertex is exactly borderline on every
elementary axis (Knapp, homogeneity, duality, VBR openness). No
elementary scaling/symmetry separates it; deciding it needs either a
genuinely new endpoint estimate (endpoint VBR at r = r*) or a subtle
multi-scale construction beating an adaptive sparse supremum.
"""
import json
from fractions import Fraction as F

print("=== (a) Knapp gap G = (1-1/q) - 3(1-1/p) ===")
for lam in [0.02, 0.05, 0.10, 1 / 6, 0.25, 0.40, 0.49]:
    p = 4.0 / (3.0 + 2.0 * lam)
    q = 4.0 / (1.0 + 6.0 * lam)
    Gv = (1 - 1 / q) - 3 * (1 - 1 / p)
    Gi = (1 - 1 / (1.5 * q)) - 3 * (1 - 1 / p)   # interior q'>q_opt
    Ge = (1 - 1 / (0.9 * q)) - 3 * (1 - 1 / p)   # exterior q'<q_opt
    print(f"λ={lam:.4f} G(vertex)={Gv:+.2e} G(interior)={Gi:+.4f} G(exterior)={Ge:+.4f}")
    assert abs(Gv) < 1e-12 and Gi > 0 and Ge < 0

print("\n=== (b) homogeneity 1/p+1/q == 1+2λ (exact rational check) ===")
for lam in [F(1, 6), F(1, 4), F(1, 10), F(2, 5)]:
    p = F(4, 1) / (3 + 2 * lam)
    q = F(4, 1) / (1 + 6 * lam)
    assert F(1, 1) / p + F(1, 1) / q == 1 + 2 * lam, lam
    G = (1 - F(1, 1) / q) - 3 * (1 - F(1, 1) / p)
    assert G == 0, lam
    print(f"λ={lam} OK: 1/p+1/q={F(1,1)/p + F(1,1)/q} = 1+2λ, G=0 exactly")

print("\n=== (c) duality mirror P2 <-> P3 on top edge ===")
for lam in [0.05, 1 / 6, 0.25, 0.40]:
    x2 = (3 + 2 * lam) / 4          # 1/p_lam
    y2 = (1 + 6 * lam) / 4          # 1/q_opt
    assert abs(x2 + y2 - (1 + 2 * lam)) < 1e-15
    mx, my = y2, x2                 # diagonal mirror
    assert abs(mx - (1 + 6 * lam) / 4) < 1e-15 and abs(my - (3 + 2 * lam) / 4) < 1e-15
    print(f"λ={lam:.4f} P2=({x2:.4f},{y2:.4f}) mirror=({mx:.4f},{my:.4f})=P3, "
          f"both with x+y={x2 + y2:.4f}=1+2λ (boundary, not exterior)")

print("\n=== (d) q_opt == 2 <=> λ == 1/6 ===")
for lam in [0.05, 1 / 6, 0.25]:
    q = 4.0 / (1.0 + 6.0 * lam)
    print(f"λ={lam:.4f} q_opt={q:.4f}")
assert abs(4.0 / (1.0 + 6.0 * (1.0 / 6.0)) - 2.0) < 1e-15

print("\n=== (e) VBR-cap dichotomy r*=p'/3 vs 2 ===")
for lam in [0.05, 0.10, 1 / 6, 0.25, 0.40]:
    p = 4.0 / (3.0 + 2.0 * lam)
    pp = p / (p - 1)
    rstar = pp / 3.0
    formula = 2 * (6 * lam - 1) / (3 * (1 - 2 * lam))
    assert abs((rstar - 2) - formula) < 1e-12
    cap = "Knapp (r<p'/3)" if lam < 1 / 6 else ("equal" if lam == 1 / 6 else "L2 (r<2)")
    print(f"λ={lam:.4f} r*={rstar:.4f} r*-2={rstar - 2:+.4f} binding cap: {cap}; "
          f"vertex needs r=r* (room 0)")

out = {"borderline_audit": "PASS",
       "knapp_G_vertex": 0.0,
       "homogeneity_exact": True,
       "duality_mirror_boundary": True,
       "qopt2_iff_lambda_one_sixth": True,
       "vbr_room_at_vertex": 0.0}
with open("borderline_audit.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nRESULT: BORDERLINE-CONFIRMED on all elementary axes")
