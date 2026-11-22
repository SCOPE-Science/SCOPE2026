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

The mathematical proof is self-contained in `RESULT.md`, Steps 1–6. The executable finite check is `verify.py`, requiring Python, NumPy and SciPy. Run `python verify.py` from a directory containing the extracted script. Its reference output was `VERIFY_OK canonical_means=8 random_full_core_vs_factor=390 weighted_LP_matches=158 exact_pair_checks=9`.

The random tests compare two distinct LP formulations: one over all core coefficients and one over the two factor marginals; the example and codimension-one pair formulas are additionally checked with exact rational arithmetic where appropriate. Finite tests do not prove universal feasibility, uniqueness, rank-completion, or the polytope support bound. Those conclusions depend on the algebraic and convex-geometric arguments in the proof.

The corrections are studied in exact arithmetic and with an entrywise nonnegative constraint, not a positive numerical tolerance or a dynamical error estimate. No independent audit was performed.
