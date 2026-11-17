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

# Reproducibility

Run `python verify.py` with Python 3, NumPy, and SciPy. The checker constructs real route-incidence vectors and independently projects onto their direction space for four small networks (48 comparisons). It tests the exact Gaussian route-exposure integral against 70,000 independent normal samples, then checks three moderate-dimensional critical ratios against 16,000 samples per ratio and a finite-sample normal-max proxy. The direct checks use numerical tolerances; Monte Carlo tests have explicitly loose probabilistic tolerances. The mathematical proof, not these finite experiments, establishes the infinite sequences and all integer graph parameters.

External review has not been performed.
