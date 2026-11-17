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

# Verification notes

The exact three-by-three matrix and stationary left and right vectors were reconstructed directly from the six-coordinate quadratic recurrence. The polynomial identity \((B-\Pi)^2-(B-\Pi)+s(I-\Pi)=0\) was checked in exact rational arithmetic over positive rational mass grids with common denominators from three to thirteen. The critically defective identity was checked using the exact mass triple \((1/6,1/6,2/3)\), including ten iterates of the original nonlinear map. The independent polar-integral coefficient calculation is an exact rational identity \(120((1/6)/27-(1/6)^2/12)=25/54\).

Execute `python checks/verify.py` using Python's standard library. The checker was run successfully with three success lines beginning `FIBER_SPECTRUM_EXACT_OK`, `DIRICHLET_DISK_INTEGRAL_OK`, and `ORIGINAL_QSO_JORDAN_EXACT_OK`. It does not explore all real parameter values; the universal matrix, Jordan and integration arguments are established symbolically in RESULT.md. The public literature may contain an equivalent unindexed result. Independent audit is not performed.
