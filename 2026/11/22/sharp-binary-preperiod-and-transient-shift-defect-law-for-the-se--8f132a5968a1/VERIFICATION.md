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

The Python 3 standard-library checker `verify_stirling7.py` was executed from the package content. It passed 13,074 integer assertions through binary depth 11, independently generating the fixed Stirling column by recurrence and shift differences by modular inclusion-exclusion. Direct checks include least-period witnesses, the exact earliest index, complete per-period residue histograms and all tested nonresonant defect valuations. This finite replay does not establish the unbounded-precision claims; the all-depth proof uses Mahler-coefficient bounds and exact remainder valuations. No independent mathematical audit is asserted.
