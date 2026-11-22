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

# Reproducibility checks

The separately embedded `checker.py` constructs every allowed marked hop directly from the hard-core rule. With Python 3, NumPy and SciPy installed, run:

```sh
python checker.py
```

The complete execution returned `PASSED 564 independent-generator and exact Poisson-corrector tests`. The independent moment generator is a three-block matrix exponential, not a repeated implementation of the spectral calculation. Exact `Fraction` arithmetic verifies the Poisson equation, including both reflecting endpoints, for all tested integer ring sizes and rate pairs. Further tests compare both tags' second moments across lengths, rates and times; check the squared-rate contrast; and verify the precise intercept at long numerical times.

All claims for arbitrary positive rates and all times rest on the complete analytic proof in `RESULT.md`, not on the finite test sweep. Numerically tiny differences of near-zero excess diffusivities are excluded from a ratio test to avoid cancellation; strict positivity follows symbolically from the first odd eigenmode. Numerical large-time comparisons do not assert exhaustive numerical verification of an infinite-time limit. No independent audit has been performed.
