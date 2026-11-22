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

# Verification details

The proof's logical cases are checked by the complete center-label partition in `RESULT.md`. The local expressions \(A_s\), \(B_s\), and \(C_s\) each count disjoint types of petal state; only the center-zero regime has a global exclusion at the all-one peripheral weight. The formula is valid for all \(q\ge2\) and all petal sizes \(s_i\ge2\), with no unproved extension to other graphs.

- `verify_attack.py`: direct adjacency-based tests for every one- and two-zero attack, followed by comparison with symbolic polynomial multiplication. Observed: `VERIFIED 10 cases 215298 direct assignments, all polynomial coefficients`.
- `verify_independent.cpp`: a distinct base-three counter, bit-mask neighborhoods and attack-pair verification, testing seven homogeneous cases. Observed: `INDEPENDENT_CHECK_OK`, including the \(3^{13}\)-assignment case with three petals of size four.
- `CHECKS.txt`: exact commands and the confirmed minimum-weight counts.

These tests establish only the verified finite instances. The arbitrary-parameter theorem is justified by the written exhaustive symbolic case classification, not by extrapolation from computation. Publication-priority searches are finite, and no independent audit has been performed.
