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

# Reproducibility and logical boundaries

Run `python verify.py` with Python 3 and NumPy, using the file shipped with this finding. The deterministic seed is `20261105` and the script evaluates the specified full-sketch and leave-one-out Nyström estimators on actual matrices; it is not a synthetic checker that compares only precomputed moments.

The recorded execution passed **479 assertions**. It checks equality between matrix-function Nyström traces and the projected-Gaussian residual representation at ranks \(2,3,4,6\) using \(k\) and \(k+1\) probes; verifies the angular-moment integrals and the exact two-probe Laplace transform; and independently simulates means, variances, pairwise covariances, and the error-proxy expectation for ranks \(2,3,5,8\). The simulation tolerances reflect stochastic sampling uncertainty; all universal formulas are established analytically in `RESULT.md`.

The proof requires no external numerical certificate: the key step is the exact two-dimensional conditional Gaussian residual geometry. The verifier does not certify historical novelty, finite-precision behavior, or a confidence guarantee for any one realization. Independent audit has not been performed.
