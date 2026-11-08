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

The standalone Python standard-library program `checker.py` was run against the included analytic formulas and produced 205 passing deterministic assertions. It checks geometric-weight majorization, Gaussian mixture moment identities, exact normal and Laplace stop-loss endpoints and finite illustrative risk integrals. Direct symbolic differentiation verified the two derivatives of the positive-threshold Gaussian stop-loss function. The proof does not infer infinite convex ordering or asymptotics from numerical grids; finite examples are diagnostics only.

The mathematical proof uses an absolutely convergent stationary characteristic-function product, independent exponential mixing, finite-dimensional Schur-convexity followed by a controlled infinite limit, strict Jensen for endpoint nonattainment, and the fourth-centered-moment bound for a uniform Taylor remainder. The Gaussian limiting endpoint is not attainable at any admissible fixed rescaling.

Literature priority remains conditional on the accessible sources, particularly broader weighted-sum comparison literature. No independent scientific audit has been performed.
