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

# Verification scope

The proof in RESULT.md gives global statements analytically. The bundled `check_crossings.py` is a standalone Python 3 standard-library script, executed with `python check_crossings.py` and observed to report `PASS: 21082 supplementary checks; analytic global statements are proved in RESULT.md`.

The script computes the strict three-passage witness with exact rational Taylor polynomials, tests the two-passage derivative and monotonic-root formulas, and compares finite numerical samples and upper/lower bounds. The rational inequality is an exact finite certificate; the randomized comparisons and finite grids do not prove optimality over a continuum. Proof completeness rests on the derivative, Hessian, cubic Taylor and asymptotic arguments in RESULT.md, not on a test log.

The model's physical assumptions are stipulated rather than empirically verified. No independent external audit or ecological validation was performed.
