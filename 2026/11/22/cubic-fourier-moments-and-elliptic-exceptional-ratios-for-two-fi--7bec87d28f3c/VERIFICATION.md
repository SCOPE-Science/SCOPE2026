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

# Verification and reproducibility

Run `python3 artifacts/verify_two_shell_threefold.py` in a Python 3 environment without dependencies beyond the standard library. The program constructs prime and extension fields, computes all ordered two-point sums of two hyperbola shells, and checks the formula independently at every target. It computes threefold return counts from those direct tables, checks the exact exceptional-ratio census, and for the smallest field models directly compares every threefold convolution support value against the asserted all-or-nothing origin criterion.

Field models tested: orders 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 9, 25, 49, 27 and 125, with both prime and extension characteristic representations. The full threefold support was enumerated for orders 3, 5, 7, 9, 11, 13 and 17. The cubic return was checked for each selected shell ratio, and the count of exceptional ratios across *all* allowed parameters was evaluated for each field. All assertions in the recorded replay passed.

The verifier checks finitely many fields and, for some larger fields, only representative ratios for direct convolution. The complete all-field correctness is supplied by the algebraic proof and classical Hasse bound in `RESULT.md`. No separate external or independent mathematical review has been conducted.
