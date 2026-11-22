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

The proof in `RESULT.md` establishes the full two-parameter statement using the first-collision argument, which handles arbitrarily long or infinite digit sequences and controls possible carries before a forbidden digit. The separate exact checker `checker.py` tests \(r=2,3,4,5\), interior parameters \(r+2\le k<\min(13,r+6)\), and input lengths \(n=k,k+2,k+4\). It enumerates every binary-input digit word of those lengths, directly computes the product by both integer multipliers, checks all possible output digits, and compares membership to the predicted gap rule and recurrence. Its actual successful execution reported: `PASS: 48 pair/depth tests and 75600 complete input-word checks`.

Reproduce with `python checker.py` (Python 3; standard library only). Finite enumeration is not an all-parameter proof and makes no assertion about independent verification. The dimension equation follows from the already known repunit shift and is not presented as a new standalone result.
