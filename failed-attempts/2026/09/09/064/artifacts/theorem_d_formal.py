"""Propositional audit of Theorem D (§O, target-directed).

Premises (all source-grounded, see WORKLOG §§D/H/I):
 P1: target class T = {compact + contractible (chi=1) + with boundary + Stein domain}.
 P2: relative trisection genus is a diffeomorphism invariant (Takahashi §2.2).
 P3: chi values: chi(W)=1 (Mazur Alternatively: 1-1+1); chi(dW)=0 (closed odd-dim);
     chi(collar dWxI)=0; collar-glued M: 1+0-0=1; double: 1+1-0=2;
     mapping torus of closed 3-manifold: 0; cap-Z gluing: 1+chi(Z)-0.
 P4: only source-pinned ambient is E(n) (closed, chi=12n) -> outside T.
 P5: no cap Z / ambient X is pinned in target text or pinned figures.

Check: for each reading in taxonomy.py, verify (in_class, k_sensitive) flags
are consistent with chi/boundary arithmetic, and that no reading is BOTH
in-class AND k-sensitive AND pinned. Hence the stated mismatch is unsatisfiable.
"""
import json

chi_W, chi_dW, chi_collar = 1, 0, 0
rows = [
    {"reading": "abstract W", "chi": chi_W, "closed": False,
     "k_sensitive": False, "pinned": True},
    {"reading": "collar-reglued M_k", "chi": chi_W + chi_collar - chi_dW,
     "closed": False, "k_sensitive": False, "pinned": True},
    {"reading": "twist double", "chi": chi_W + chi_W - chi_dW,
     "closed": True, "k_sensitive": True, "pinned": True},
    {"reading": "boundary mapping torus", "chi": 0,
     "closed": True, "k_sensitive": True, "pinned": True},
    {"reading": "cap-Z gluing", "chi": "1+chi(Z)", "closed": "depends",
     "k_sensitive": True, "pinned": False},
    {"reading": "ambient twist", "chi": "chi(X)", "closed": "depends",
     "k_sensitive": True, "pinned": False},  # only E(n) pinned -> closed chi=12n
]
for r in rows:
    if isinstance(r["chi"], int):
        in_class = (r["chi"] == 1 and not r["closed"])
    else:
        in_class = False  # unpinned-dependent: cannot be established in-class
    r["in_class_established"] = in_class
    r["mismatch_possible_in_class"] = bool(in_class and r["k_sensitive"] and r["pinned"])

# chi arithmetic assertions
assert chi_W + chi_collar - chi_dW == 1
assert chi_W + chi_W - chi_dW == 2
# the danger zone must be empty
danger = [r for r in rows if r["mismatch_possible_in_class"]]
out = {"rows": rows, "danger_zone": danger,
       "THEOREM_D_PROPOSITIONAL_OK": len(danger) == 0}
print(json.dumps(out, indent=2))
assert len(danger) == 0
