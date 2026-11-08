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

# Reproducibility

Run `python3 verify.py` using the standard library. It computes the exact generating-function coefficients, compares an independent arch-state count for each parameter pair \(3\le q\le8\), \(2\le d<q\), and exhaustively enumerates seven small families of actual words. It also verifies the sharp minimum-length count and the quaternary radius-two rational denominator recurrence. The expected success line is:

`VERIFY_OK q=3..8 d=2..q-1 n<=32 finite_cells=1732 literal_instances=44223 quaternary_identity_n<=60`

The reported finite computation does not prove unbounded lengths, radii or alphabet sizes. The proof of the infinite formula and renewal limit is in `RESULT.md`. No independently executed external channel or third-party audit is asserted.
