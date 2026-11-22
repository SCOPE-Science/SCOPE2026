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

The proof gives a general finite-field argument using scalar averaging, exact annihilator character sums, a line-weight arithmetic-mean inequality, and a unique one-variable minimax. The resulting center-atom rigidity is derived from the preservation of that atom under both averaging steps. This argument does not depend on numerical experiments.

A standalone standard-library Python checker is supplied as `check_bias.py`. Running `python3 check_bias.py` gave eight PASS lines at field orders \(2,3,4,5,7,8,9,11\), totaling 4,376 comparisons of nontrivial Fourier-coefficient magnitudes with the exact formulas. The checker verifies the claimed attaining construction but does not exhaust the continuum of probability measures; the lower bound is proved analytically.

Normalizations: unnormalized finite-field Fourier transform; nonnegative probability masses; maximum only over nonzero frequencies. The full pencil with \(q+1\) directions is excluded from the nonzero formula. Independent mathematical audit is not performed.
