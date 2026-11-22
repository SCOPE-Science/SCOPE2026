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

# Reproducible verification

Run `python checks/verify.py` with Python 3 from the artifact root. The script reconstructs interval matchings from endpoint ranks, independently checks the largest concurrent active set, rebuilds the conditional ternary code, and tests component counts, tree structure, degree maxima, and exact finite component-size formulas. No external packages, network access, random seeds, or unlisted data files are needed. The finite enumerations are not proofs of infinite assertions. The general proof is given in RESULT.md, including the bounded-dependence truncation and longest-run arguments.

The statistical statements are under the triangle-free conditional law. Independent validation has not been performed.
