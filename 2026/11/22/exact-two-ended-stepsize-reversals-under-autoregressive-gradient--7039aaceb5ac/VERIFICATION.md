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

The standalone `verify.py` uses Python standard-library rational arithmetic to verify the finite-horizon noise-weight representation; exact AR(1) moment quadratic and first-order stationarity equations; the optimal risk and both adjacent sign classifications; exact rational witnesses; and positive risk gaps for finite perturbations. Invoke `python3 verify.py` in the same directory. The script prints `VERIFY_OK` with its assertion count on successful execution.

This is a reproducibility test only. Positive definiteness, uniqueness, admissibility and the parameter-uniform threshold results are proved analytically in `RESULT.md`. No externally performed independent mathematical audit is asserted.
