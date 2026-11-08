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

# Verification of the all-iteration covariance-probing law

The proof uses the exact covariance polynomial in the normal matrix, so every statement for all positive iteration indices is an algebraic theorem under the listed hypotheses, not a finite numerical extrapolation. A Rademacher coordinate-product bijection and the projector identity \(P^2=P\) justify the sub-Gaussian proxy; the flat-spike binomial counting is exhaustive at arbitrary finite parameters by the independent-sign proof.

Run `python verify.py` with Python 3.9+ and NumPy. The observed output was:

```
VERIFY_OK; 1200 dense-operator comparisons; 6 exact exhaustive binomial cases; 20 endpoint checks
```

The script creates random orthoprojectors of ranks one and co-rank one and tests the signed error identity against explicit dense covariance multiplications at eight iteration counts and many positive step sizes. Six small finite Rademacher models are enumerated exhaustively and their multiplicities compared with binomial coefficients. The checker also verifies both endpoint factors and their threshold ordering. Finite tests do not establish infinite-time monotonicity; the weighted-average argument in RESULT.md does. The probability tail bound is the standard Rademacher moment-generating-function inequality applied once to the shared projector estimator; it does not require checking infinitely many steps computationally.

Limitations: exact arithmetic is assumed; the code uses floating-point computations for diagnostic dense tests, not a formal proof of their validity for untested inputs. The estimator targets the exact propagated covariance rather than a randomized-SVD approximation. Independent audit has not been performed.
