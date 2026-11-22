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

The mathematical claim is proved by the explicit Volterra covariance and conditional Gaussian variance formula, a log-time concavity argument using Prékopa's theorem, and a strict one-crossing stationarity equation. The proof covers all real \(\alpha\geq0\) and finite \(\eta\geq0\).

To reproduce supplemental computations, install the dependency in `standalone/requirements.txt` and run `python standalone/verify.py` from the parent directory. A local run passed 3,653 assertions, cross-checking direct covariance integration, hypergeometric evaluations, stationarity, finite-grid optimality, and the exact Brownian/integrated-Brownian examples. The computations do not establish global uniqueness over the continuum; that relies on the proof and the standard marginal log-concavity theorem.

Related historical designs may have equivalent implications that could not be resolved without inaccessible full texts. The results have received self-review only; independent mathematical and publication-priority checks have not been performed.
