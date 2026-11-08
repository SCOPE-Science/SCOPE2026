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

The proof uses an exact partition of the pair-space and positive Laplace deconvolution; it is not based on finite enumeration. The executable sanity checks in `CHECK.py` confirm the four-site pair distances and noncongruence with integer arithmetic, perform finite-grid checks for small site counts, compare the rooted-interval Laplace expression for five positive parameters, and sample 260000 independent whole-graph point pairs across the two configurations. The finite-grid checks are corroboration only; all continuous and arbitrary-tree assertions are derived analytically in `RESULT.md`.

The public source comparison is restricted to the accessible portions described in `REVIEW.md` and `AUDIT.json`. Independent validation was not performed.
