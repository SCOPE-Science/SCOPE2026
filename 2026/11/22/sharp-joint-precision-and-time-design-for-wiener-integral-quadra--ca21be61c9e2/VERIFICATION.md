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
# Verification and boundaries

Run `python -m pip install -r requirements.txt`, then `python verify.py` in this directory. The verifier checks symbolic scalar stationarity and Gaussian normal-equation identities, exact rational risk at two observations with unit budget, limiting noiseless formulas, covariance calculations at 56 parameter choices, 16,800 randomly drawn feasible comparator designs, and finite-limit sanity checks. All tests passed during the review.

The proof of global uniqueness is analytical, not a numerical certificate: it rests on the step-function reduction, strict monotone rearrangement, refinement of unused levels, and a unique positive solution of the scalar optimality equation. Random comparisons are finite corroboration only, not exhaustive verification over the continuum of designs. The result does not assess nonlinear observations, adaptive sensing, arbitrary kernels, or publication priority outside the literature examined.
