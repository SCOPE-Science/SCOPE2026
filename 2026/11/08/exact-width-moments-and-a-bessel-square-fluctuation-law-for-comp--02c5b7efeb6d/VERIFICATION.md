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

Run `python check_width.py` in an environment with NumPy and SciPy. The deterministic checker uses seed 20261102 and independently tests the signed-edge support formula, the conditional two-dimensional normal CDF formula for several small part sizes, the exponential-product Bessel CDF, the gamma moment transform, and mean/variance constants. It also computes rescaled sample widths for two balanced dimensions, allowing for the known slow convergence of Gaussian extremes. Successful output: `COMPLETE_BIPARTITE_SYMMETRIC_EDGE_WIDTH_CHECKS_PASSED`.

The exact gamma identity is derived by Tonelli and a beta integral in RESULT.md. Computations do not establish convergence or historical novelty. No independently performed mathematical audit is claimed.
