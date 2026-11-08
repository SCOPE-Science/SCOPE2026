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

## Reproducing the exact finite computation
Execute `python3 verify.py`. The checker requires only the Python standard library and iterates all \(15,361\) nonnegative binary16 states of \([0,1]\) for each of the three specified evaluations. It uses exact integer-scaled rational arithmetic to perform every rounding operation, never using a host floating-point number for the mathematical graph. It derives and checks all orbit lengths, basins, extrema of first-entry times and SHA-256 digests of complete successor arrays. The terminal success line is `EXACT_GRAPH_CHECK_OK`.

The computed cycle basin sizes sum to \(15,361\) separately for each graph. Exact nearest-even ties include subnormal transitions; the value \(0\) is a single positive encoding. An independent test of all \(46,083\) transitions using explicit NumPy float16 operations for the two staged maps and double-precision exact polynomial evaluation for the single-rounded map produced zero mismatches. That supplemental check is not needed to establish completeness. No formal verification of the Python interpreter or independent mathematical audit has been performed; the certificate applies only to the specified finite maps.
