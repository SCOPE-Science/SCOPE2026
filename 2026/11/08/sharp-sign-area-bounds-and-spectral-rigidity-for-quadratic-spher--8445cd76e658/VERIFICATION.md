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

Run `python3 positive_area_degree2_checker.py`. The executable checks the closed endpoint transformations, the curvature factor, monotonicity at seven specified spectral inputs, the stability inequalities at those inputs, and four independent quasi-uniform spherical integrations. The standard-library checker uses no external numerical tables. Exact universal quantifiers, analytic monotonicity and equality cases are established by the proof, not by finite sampling.

No independent audit has been performed.
