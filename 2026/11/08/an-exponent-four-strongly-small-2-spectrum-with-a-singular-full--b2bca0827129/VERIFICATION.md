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

# Reproducing the finite checks

Run `python3 CHECK.py` with Python 3 and no third-party dependencies. The program first counts all ordered differences of the six-point subset of \((\mathbb Z/4\mathbb Z)^2\), and verifies its inversion symmetry and flat real Fourier sign. It then performs all order-four discrete Fourier transforms of the explicit local factors at levels \(j=1,2,3\) in exact Gaussian-integer arithmetic, checking all coefficients, their nonzero values, and antipodal exclusion. The normalization in `CHECK.py` is the integer array \(2f_j\) at \(a=1/2\); dividing the resulting transforms by twice the group order gives the normalized coefficients in the proof.

Observed output from the included program:

```text
CHECK_OK difference_set_order=16 exact_factor_levels=3 gaussian_integer_Fourier_coefficients=17472
```

These finite computations cannot certify the infinitely many product blocks, measure singularity, or regularity of convolutions by themselves. The infinite assertions follow from the explicit tensor formula, summable total-variation perturbations, two distinct almost-sure averages, Fourier summability, and the finite-intersection argument in `RESULT.md`. No independent mathematical audit has been performed.
