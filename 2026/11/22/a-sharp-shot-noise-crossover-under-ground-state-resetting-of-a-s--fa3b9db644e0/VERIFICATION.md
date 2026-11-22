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

# Reproducibility and verification

Run `python check.py` with SymPy. The checker separately reconstructs the ground-to-emission resolvent and the photon-count tilted-generator characteristic equation. It proves the exact Fano identity symbolically, proves the explicit third counting cumulant deficit after imposing the critical rate condition, and cross-checks first through third long-time count cumulants at nine independent positive rational parameter sets, including zero reset rate. Exact rational comparisons avoid finite-difference error.

The sign boundary follows by positivity of the denominator and monotonicity of the single scalar `u+r`; no finite parameter scan is used as proof. Counts are asymptotic in an ergodic renewal process, and photon detection, repumping costs, and partial-state resets are outside the model.

Independent audit has not been performed.
