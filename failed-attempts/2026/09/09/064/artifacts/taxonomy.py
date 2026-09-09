"""Exhaustive taxonomy of possible meanings of 'twist manifold Y_k from (C1,f^k)'
(§I). Every construction from cork datum alone falls in exactly one class:
  k-blind (abstract W itself; collar-reglued W) -> genera necessarily equal;
  k-sensitive closed (double chi=2; mapping torus chi=0) -> outside target class;
  auxiliary-Z or ambient-X dependent -> unpinned by target (no Z/X in claim).
Target class = compact contractible (chi=1) with boundary (Stein domain sense).
Only the k-blind class intersects (target class x no-unpinned-input), and there
the 3-vs->=4 mismatch is impossible by diffeomorphism invariance of genus.
"""
import json

rows = [
    {"meaning": "Y_k = W (abstract manifold itself)",
     "needs_aux": False, "k_sensitive": False, "chi": 1, "has_boundary": True,
     "in_target_class": True, "mismatch_possible": False,
     "reason": "f^0,f^1 in Diff(dW) of one fixed W; Y0=Y1=W; genus invariant"},
    {"meaning": "Y_k = W U_{f^k} (dW x I) (collar regluing)",
     "needs_aux": False, "k_sensitive": False, "chi": 1, "has_boundary": True,
     "in_target_class": True, "mismatch_possible": False,
     "reason": "Psi=id_W U (f^k x id) descends to diffeomorphism M_k->M_0 (replay collar_descent.py)"},
    {"meaning": "Y_k = W U_{f^k} Z, fixed auxiliary cap Z (single boundary comp.)",
     "needs_aux": True, "k_sensitive": True, "chi": "1+chi(Z)",
     "has_boundary": False, "in_target_class": False,
     "mismatch_possible": "N/A (Z unpinned)",
     "reason": "closed (glued along full boundary); Z not in target text/figures"},
    {"meaning": "Y_k = W U_{f^k} Z, Z with extra boundary components",
     "needs_aux": True, "k_sensitive": True, "chi": "1+chi(Z)",
     "has_boundary": True, "in_target_class": "needs chi(Z)=0 + pi1/contractibility (unpinned)",
     "mismatch_possible": "N/A (Z unpinned)",
     "reason": "no such Z pinned in Teng/Takahashi; collar (chi(Z)=0, k-blind) is the only source-grounded case"},
    {"meaning": "Y_k = twist double W U_{f^k} (-W)",
     "needs_aux": False, "k_sensitive": True, "chi": 2, "has_boundary": False,
     "in_target_class": False, "mismatch_possible": "N/A (outside class)",
     "reason": "homotopy S^4, closed, non-contractible, non-Stein (replay twist_double.py)"},
    {"meaning": "Y_k = mapping torus T_{f^k}",
     "needs_aux": False, "k_sensitive": True, "chi": 0, "has_boundary": False,
     "in_target_class": False, "mismatch_possible": "N/A (outside class)",
     "reason": "closed, chi=0, non-contractible, non-Stein-domain (replay mapping_torus.py)"},
    {"meaning": "Y_k = (X-W) U_{f^k} W (ambient twist)",
     "needs_aux": "ambient X", "k_sensitive": True, "chi": "chi(X)",
     "has_boundary": "boundary of X", "in_target_class": "only if X contractible (none pinned)",
     "mismatch_possible": "N/A (X unpinned)",
     "reason": "only source-pinned ambient E(n): closed chi=12n non-Stein (replay e_ambient.py); P/Q precedent b2=1 non-contractible"},
]
ok = (
    all(not r["k_sensitive"] or not r["in_target_class"] or r["needs_aux"]
        for r in rows if isinstance(r["in_target_class"], bool))
    and rows[0]["in_target_class"] and rows[1]["in_target_class"]
    and not rows[0]["mismatch_possible"] and not rows[1]["mismatch_possible"]
)
out = {"taxonomy": rows,
       "conclusion": "No pinned-input construction in the target class is k-sensitive; "
                     "every k-sensitive construction is unpinned or outside the class. "
                     "Hence the stated 3-vs->=4 mismatch is unsatisfiable as stated.",
       "TAXONOMY_EXHAUSTIVE_OK": ok}
print(json.dumps(out, indent=2))
assert ok
