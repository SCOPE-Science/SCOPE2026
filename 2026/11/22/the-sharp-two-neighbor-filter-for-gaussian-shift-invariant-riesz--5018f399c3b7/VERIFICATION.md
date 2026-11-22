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

# Verification and reproducibility

The analytic proof is in `RESULT.md`; the separately implemented Jacobi-series checker is `verify.py` with its actual output in `check_output.txt`. Executing `python verify.py` with Python 3, SciPy and mpmath produces `PASS 145 numerical assertions` over nine positive width parameters, multiple filter perturbations, four Poisson-duality widths and high-precision small-nome checks. The numerical routines do not certify global maxima or infinitely many widths; these follow from the strictly concave logarithmic theta product and the pointwise monotone normalization proved in the text.

Critical normalization check: for every positive Gaussian width, the squared translate Gram multiplier is `(2*s)**(-1/2) * theta3(pi*xi, exp(-pi*s/2))`. Both the theta series and Poisson-periodized Fourier representation are compared numerically. The equality of endpoint minima and the uniqueness of the interior maximum are analytic consequences of the product. Historical priority has been checked against identified published sources and semantic matches but is not independently certified.
