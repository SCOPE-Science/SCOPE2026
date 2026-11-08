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

# Verification procedure and evidence

Run `python verify.py` using Python 3 with NumPy, SymPy and mpmath. The executable uses only explicit formulas and fresh random samples; no external input files are needed. The 2014 centroid numerical value is treated as a known reference check, not as new discovery.

Successful execution of the embedded script prints `VERIFY_OK` and reports three symbolic derivative/mean identities, four independent 40-digit corner integrals, 18,000 pairwise positive balancing checks, direct sampling of 480,000 triangles under a nontrivial affine transform at seven fixed target points, 201 boundary checks and four near-vertex entropy checks. The run recorded a largest absolute direct-sampling discrepancy of 0.0012914 across seven points; checks require discrepancy below 0.005. Symbolic integration confirms that the average of the exact target-location profile under a uniform target is 1/4.

The proof of the all-target identity, strict majorization law, and uniform vertex asymptotic appears in `RESULT.md`. Finite balancing examples, Monte Carlo and high-precision quadrature provide error detection only. They do not certify originality, any universal quantifier, or historical priority. Independent audit has not been performed.
