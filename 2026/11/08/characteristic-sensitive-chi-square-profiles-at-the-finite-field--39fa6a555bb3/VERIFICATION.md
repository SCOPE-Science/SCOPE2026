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

# Reproducibility and verification boundaries

The proof is analytical. The `check_odd.py` and `check_even.py` programs are standard-library finite-field tests, not an external certificate or an exhaustive verification in infinitely many dimensions. Both were run from the supplied source files, and their output is documented in the review. Odd-characteristic checks enumerate all rank sectors in small prime fields; even-characteristic checks include the extension field of four elements. Direct finite convolution distributions were compared with the Fourier chi-square formula at the enumerated small sizes. Infinite-series convergence and the two cutoff limits use the written analytic arguments. Independent audit has not been performed.
