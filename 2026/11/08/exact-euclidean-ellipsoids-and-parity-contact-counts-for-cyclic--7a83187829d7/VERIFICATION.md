---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and scope

Run `python verify.py` with Python 3.10 or later. The script uses only the standard library and checks 288399 exact integer/rational assertions, reporting `PASS total 288399 assertions including weighted hypergraph outer-radii` when successful. The code exhaustively enumerates signed edge-vertex choices on cycles of orders three through eight, subset-covering minima through order twelve, finite small weighted graphs, and 144 weighted hypergraph instances. It independently checks the Euclidean support inequalities at bounded integer normals; no floating-point tolerances are used.

No program can replace the infinite proof in `RESULT.md`. In particular, the exact all-order claims use the coverage decomposition, maximizing-load exchange argument, parity classification of cycle independent sets, and uniqueness of extremal ellipsoids under symmetry. Numerical or finite enumeration results are not treated as exhaustive outside the ranges stated.

Historical originality has only self-review. Independent mathematical review, full specialist bibliographic verification, and any external certification have not been performed.
