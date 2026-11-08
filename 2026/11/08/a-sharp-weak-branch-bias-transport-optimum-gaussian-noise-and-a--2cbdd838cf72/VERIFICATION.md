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

Run `python3 CHECK.py` using only the Python standard library. The script tests a direct finite-state stationary master equation, exact canonical mass via Bernoulli convolution, limiting density and current, Gaussian variance, negative inter-site covariance, optimal bias, fixed-bias regimes, and the positive finite-size current excess. Output on the prepared script: `PASS 93 checks` followed by reference numerical values. The script uses finite state sizes and direct arithmetic; its results are not evidence of an infinite theorem by themselves. The proof in `RESULT.md` supplies the uniform local central limit/conditioning and asymptotic arguments.

The stationarity condition is independently enumerated on a small ring/path example with forward and reverse backbone moves and both branch directions. The finite-weight computations use normalization after multiplying Bernoulli and Poisson-binomial masses. The source stationary law and hypergeometric formula are prior results. No external independent audit or validation has been conducted.
