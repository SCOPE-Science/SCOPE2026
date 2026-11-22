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

Run `python3 verify.py` using Python 3 and the standard library. The checker exhaustively iterates over all permutations of length at most eight, computes strict-comparison signatures of every insertion-cut pair, checks the quadratic upper bound and verifies the exact nonparameter antichain signature family. Observed counts are `1,3,7,13,21,31,43,57,73`. The output ends with `VERIFY_OK`. The checker was executed from decoded bytes in the final package.

The proof extends to all finite sizes without an experimental assumption: the forest collision argument bounds every parameter configuration, and the reverse-permutation antichain yields sharpness. Independent review and historical-priority determination remain unperformed.
