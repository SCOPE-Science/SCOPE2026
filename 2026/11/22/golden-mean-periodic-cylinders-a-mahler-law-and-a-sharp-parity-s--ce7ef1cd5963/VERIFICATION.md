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

# Reproduction checks

From a directory containing `checks/verify.py`, run `python3 checks/verify.py` using Python 3 with the standard library. The program enumerates all words of lengths 2–15 with no adjacent `11`, checks the exact unbordered/full-period equivalence independently for each word, checks 220 integer coefficient identities, and evaluates the two explicit asymptotic phase constants with 110-digit decimal arithmetic. The nonnegative truncated tail of the constant series is bounded by an explicit geometric inequality, not assumed zero.

The analytical proof is in `RESULT.md`: it uses the exact shortest-border decomposition and meromorphic pole propagation. Finite enumeration does not establish the infinite claims. No third-party computational package or unavailable certificate is required. An external independent mathematical audit has not been performed.
