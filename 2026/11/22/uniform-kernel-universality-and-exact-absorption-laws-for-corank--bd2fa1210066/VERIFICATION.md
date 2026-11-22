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

Run `python3 check.py` with Python 3 and its standard library. The script enumerates actual finite-field matrices, multiplying each matrix explicitly rather than treating the theorem as the computation. In \(\mathbb F_2\) (dimensions two and three) and \(\mathbb F_3\) (dimension two), it checks all corank-one idempotents. In \(\mathbb F_2\) (dimension three), it separately tests all regular nilpotents. At each rank, it tests the predicted drop frequency. Through six factors, it enumerates the full matrix-state convolution and compares its rank marginal to the predicted pure-death chain using exact rational arithmetic. A second test compares survival probabilities through thirteen steps to the partial-fraction identity. `check_output.txt` contains the actual results and was recorded after replaying the included code.

The computations do not establish a theorem for arbitrary prime-power fields or arbitrary dimension, and they do not certify novelty. Those statements rest on the independent algebraic and probabilistic proof in `RESULT.md`. The limiting random variable is proved by the uniform \(L^1\) tail estimate, not by numerical extrapolation. Independent mathematical audit is not performed.
