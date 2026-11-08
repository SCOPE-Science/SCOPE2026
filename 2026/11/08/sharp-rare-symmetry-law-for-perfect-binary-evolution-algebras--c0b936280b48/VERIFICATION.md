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

# Mathematical verification

Run `python3 verify.py` using standard Python 3 without third-party dependencies. The program enumerates all binary matrices for each \(n\in\{1,2,3,4\}\), uses an independently implemented binary rank algorithm to identify invertible matrices, and tests simultaneous invariance under every coordinate permutation. It compares transposition centralizer totals, orbit counts, and full group cardinalities to the derived formulas and source small-dimensional values.

Expected output ends in `VERIFY_OK`. In dimensions two, three, and four, the transposition-fixed invertible matrix totals are respectively \(2,8,192\). The orbit totals for dimensions one through four are \(1,4,33,908\). This verification tests exact finite identities only. The proof of the infinite asymptotic statement is in `RESULT.md`, including the detailed cycle-deficiency bounds and uniform summation. No independent mathematical validation has been performed.
