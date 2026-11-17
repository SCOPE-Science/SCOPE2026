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

# Verification

Execute `python3 tree_width_checker.py` in the directory containing this file. The script uses Python standard-library modules only and prints:

`TREE_ZONOTOPE_ANGULAR_PASS labelled_trees=1440 exact_tangent_mixtures=56262 path_edges=90 star_edges=90`

The finite checks cover every Prüfer-coded labeled tree on 3 through 6 vertices, with exact Fraction arithmetic for the Gram matrices and sharp tangent inequalities; they also verify path/star closed forms through 14 vertices and attained finite-angle formulas in selected geodesics. The general result rests on the analytical cut-basis proof in RESULT.md. Nothing here is an independent mathematical audit.
