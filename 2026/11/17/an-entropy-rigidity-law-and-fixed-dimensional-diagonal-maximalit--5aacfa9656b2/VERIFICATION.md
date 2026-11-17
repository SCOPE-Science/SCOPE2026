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

# Reproduction and evidence limits

The exact analytic chain is given in `RESULT.md`: polar formula, uniform exponent differentiation, beta-coordinate marginal, strong entropy convexity, the nondegenerate Hessian, and a compactness step. The key stability assertion is therefore supported by a proof for every fixed integer dimension, not by finite enumeration.

Run `python VERIFY.py` with Python 3, NumPy and SciPy. In the recorded run it returned `PASS 2066 deterministic identity / quadrature checks`. This verifies selected dimension-two exact fiber formulas, dimension-three direct quadrature and derivatives, a family of numerical entropy inequalities, and diagonal curvature ratios over dimensions 2–15. All random normals are generated using the stated fixed seed.

The script does not prove global maximality over the continuous sphere, does not supply an explicit exponent threshold, and does not replace the domination/compactness proof. Historical priority has only been checked against the cited accessible papers and indexed mathematical records. Independent audit status: not performed.
