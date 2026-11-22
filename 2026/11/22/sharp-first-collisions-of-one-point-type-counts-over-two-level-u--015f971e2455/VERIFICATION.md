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

# Verification evidence and limits

The general theorem follows from the elementary complete Katětov inequalities and homogeneity, not from finite computation. For the finite sharp thresholds, the executable certificate is exhaustive rather than a random sample: it generates every unordered positive partition of every base size \(1\le n\le16\), checks canonical uniqueness through nondecreasing parts, compares both the scalar and the scalar-plus-number-of-classes keys, and independently checks the partition-number sequence. All collisions found at the first sizes are displayed in RESULT.md.

Run `python3 artifacts/verify.py` from this package root. No installation or external inputs are needed. `artifacts/verify_output.txt` contains the actual recorded stdout. The verifier also independently enumerates all possible 3-valued new-point distance assignments over 54 small bases and directly enforces every triangle inequality, comparing coefficient dictionaries with the formula. The full inverse polynomial is additionally recovered for every enumerated partition through sixteen points.

The code cannot certify historical originality and does not claim to exhaust unbounded-size partitions directly; the proved add-a-part identity supplies existence for every larger size. No independent mathematical review has been performed.
