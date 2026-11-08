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

Run `python3 verify.py` with Python 3 standard library from this folder. The program derives coefficient counts using integer dynamic programming; separately enumerates full permutations in eight cases with at most eight semigroup elements; and compares the symmetric, one-column, two-row and parity consequences in sixteen additional parameter pairs. Direct-permutation tests use the multiplication `(i,a,l)*(j,b,m)=(i,a xor b,m)` without the coefficient argument. The expected exact text is stored in `verification_output.txt`; all assertions must pass.

Finite tests verify only the cases explicitly enumerated. The theorem for arbitrary positive index sizes rests on the six-step combinatorial proof in `RESULT.md`, not the program. An independent mathematical audit has not been performed.
