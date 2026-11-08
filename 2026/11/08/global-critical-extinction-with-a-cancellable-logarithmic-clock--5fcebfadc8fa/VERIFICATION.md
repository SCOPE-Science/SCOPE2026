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

# Verification details

Run `python verify.py` from the same directory as the research files. The checker uses only Python 3 standard-library facilities. It performs exact rational algebra for the derived coefficient identities, and independent finite-iteration checks for positive, zero, and negative logarithmic-correction coefficients. It reports finite-part convergence in representative trajectories without claiming certified asymptotic error bounds.

The infinite-population-time limit is established by the estimates in `RESULT.md`, not by this finite checker. The source paper was inspected in its open-access PDF form (Sections 2–4, the pertinent bifurcation discussion, and conclusion). Independent scientific audit has not been performed.
