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

# Verification

`verify_modal.py` was executed with Python and SciPy. It passed 33 independently evaluated finite-parameter checks. The checks include: separate renewal-age integration of the Gaussian OU propagator, monotonicity comparisons on grids for multiple reset rates and separations, the analytic critical plateau both inside and outside the reset interval, normalized total mass, and an independent integration of the exact second moment.

The proof of the infinite-domain modality classification relies on positivity of the invariant density, the sign of the second derivative at every zero of its first derivative, the atom-induced derivative jump, and decay of the OU renewal density. Finite checks provide consistency evidence only; they are not exhaustive and are not substituted for these arguments. The result does not assert transient modality, asymmetrically weighted resets, or general outside-gap extrema.
