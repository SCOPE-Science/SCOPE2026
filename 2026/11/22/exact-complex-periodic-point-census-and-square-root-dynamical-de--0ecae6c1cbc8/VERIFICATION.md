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

# Reproducibility and verification

The exact companion-coordinate change and highest-homogeneous-form induction are proved in `RESULT.md`. The projective nonintersection and Bézout calculation apply to every positive period; the auxiliary Chebyshev witness establishes generic simplicity algebraically.

Run `python checker.py` with SymPy available. The script was run successfully: degrees and leading-form projective nonintersection for seven successive iterate periods, exact product counts 2, 4, 8, 16, 32, 64, 128, and squarefreeness of six logistic iterates all passed. This finite test is not treated as an infinite-period proof. No independent external mathematical audit was conducted.
