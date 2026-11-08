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

The stand-alone `check.py` requires Python 3 and `mpmath`. Execute `python check.py`. `check_output.txt` contains the recorded output from this package: 40,154 successful test assertions. Exact-rational checks concern the finite Markov run-length law and risk remainder. Numerical Gaussian mixture tails are checked at increasing scales; a separately evaluated Fourier sum agrees with the complex-gamma formula. A dense independent finite grid confirms the switching-price minimum.

These computations do **not** independently certify uniform convergence, the entire complex Fourier spectrum, analytical zero-freeness of Gamma, or novelty; those follow from the displayed proof or remain subject to independent review.
