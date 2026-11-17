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

Run `python3 verify_gini_convex.py` using standard Python 3 from the directory containing the package files. It uses only `fractions.Fraction` and built-in constructs; no external modules, datasets, or prior records are required.

The executable checks all \(2^{n-2}\) active second-difference sets and one of each complementary pair of the \(2^n-2\) nontrivial Gini cuts for each integer \(2\le n\le8\). It reconstructs the rational orthogonal projector from its Gram matrix and verifies constant preservation, symmetry, idempotence, and the seven exact target values. It also independently verifies a finite four-site input-pair KKT witness and the fixed-face rational lower formula for every integer \(4\le n\le30\).

Actual execution printed `ALL_EXACT_CONVEX_GINI_CHECKS_PASS 24782`. The code's full enumerations suffice for the *finite* coefficient assertions only after the analytically proved face-and-cut reductions. Its checks through observation count 30 do not establish an infinite statement; the every-dimensional strict bound is proved symbolically in RESULT.md. Computations and literature comparisons were completed without an independent audit.
