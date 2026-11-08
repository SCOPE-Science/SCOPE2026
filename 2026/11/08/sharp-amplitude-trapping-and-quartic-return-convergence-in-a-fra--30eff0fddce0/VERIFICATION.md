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
# Reproducible verification

The included standalone program `check.py` uses Python 3, SymPy and mpmath; execute `python check.py` in the directory containing this file and `check.py`. It symbolically verifies the kinetic derivative identities; checks six parameter regimes on a 2001-point amplitude grid; checks local superattracting derivatives for three fractional exponents; tracks convergence from twelve starting values; estimates critical flip relaxation for three exponents; and verifies the predicted quartic two-step coefficient with 85 digits of precision. It prints two `VERIFY_OK` lines when the checks pass.

The numerical grids and sampled trajectories are **not exhaustive proofs**. The universal claims rest on concavity, positive elasticity, one-dimensional ordering, the exact endpoint-slope criterion, and Taylor's theorem in `RESULT.md`. At the exceptional finite-hit initial points, asymptotic error ratios are undefined; the text explicitly excludes them. No external audit has occurred.
