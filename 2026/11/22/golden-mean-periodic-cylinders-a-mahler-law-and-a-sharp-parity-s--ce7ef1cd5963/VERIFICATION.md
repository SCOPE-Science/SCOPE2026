---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction checks

From a directory containing `checks/verify.py`, run `python3 checks/verify.py` using Python 3 with the standard library. The program enumerates all words of lengths 2–15 with no adjacent `11`, checks the ordinary word-period/unbordered equivalence for each word and the exact counts, checks 219 integer coefficient identities (degrees 2–220), and evaluates the two explicit parity constants with 110-digit decimal arithmetic. An explicit geometric inequality bounds the nonnegative truncated tail of the constant series.

The analytic proof is in `RESULT.md`: it uses the exact shortest-border decomposition and meromorphic pole propagation. Finite enumeration does not establish the infinite claims. No third-party computational package is required for the checker.
