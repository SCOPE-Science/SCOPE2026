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

Execute `python3 verify.py` using Python 3 and its standard library. The checker generates all \(208\) nonempty rook faces, all \(3280\) strict inclusion chains and the \(24\) simultaneous-label group actions. It constructs each orbit boundary over the integers, tests the two chain identities, and carries out all \(83\) valid unit-pivot cancellations with boundary-composition rechecks. Its deterministic output is:

```
FACE_COUNTS=16,72,96,24
BARYCENTRIC_COUNTS=208,1056,1440,576
QUOTIENT_COUNTS=19,59,66,24
UNIT_CANCELLATIONS=18,41,24
REMAINING_CHAIN_RANKS=1,0,1,0
VERIFY_OK
```

The calculation is an exhaustive finite arithmetic certificate, not evidence for any other board size. The use of Armstrong's orbit-space theorem and the two homotopy-recognition theorems is explained in the proof; the script does not independently implement these general theorems. No external review is claimed.
