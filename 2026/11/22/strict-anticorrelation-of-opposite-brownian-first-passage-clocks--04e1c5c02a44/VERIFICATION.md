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

# Verification of the opposite-target first-passage covariance

The analytic proof is in RESULT.md. For reproducibility, run `python check.py` with SymPy, mpmath, NumPy, and SciPy installed. The ordinary checker performs:

- Exact symbolic elimination for the mixed moment and the strictly negative covariance, with the independent variables \(x=e^A\), \(y=e^B\).
- A symbolic limit confirming the coefficient of the weak-reset \(r^{-1/2}\) mixed second moment and cancellation of the leading \(r^{-1}\) terms.
- Six independent, 60-digit bivariate Laplace-transform cross derivatives and four independent marginal-variance derivatives.
- Three independent sparse CTMC finite-lattice first-passage computations converging toward the continuum covariance.

The script successfully passed all listed tests during review. The numerical checks are finite; the uniform statement for all positive parameters rests on the exact Markov/renewal proof and symbolic identity. The general proof uses known one-dimensional Brownian hitting transforms and the strong Markov property. Independence of validation or worldwide literature priority is not asserted.
