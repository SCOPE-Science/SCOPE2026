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

# Verification record

The standalone `verify.py` program enumerates all words of the specified small lengths over alphabets of size two or three, checks primitive cut uniqueness and exact per-cut counts, and directly computes the occurrence-probability inequalities as exact fractions for all patterns in the stated finite regimes.

Observed language totals for binary odd lengths 3, 5, 7, 9, 11: 8, 32, 100, 260, 684. For ternary odd lengths 3, 5, 7, 9: 21, 123, 549, 2127. All checks passed.

These tests are finite consistency checks only. Infinite-length correctness comes from the elementary reflection argument, the period-divisor bound, the second-moment occurrence calculation and the geometric-sum bounds detailed in RESULT.md. No exhaustive unbounded computation, sharp leading constant, external formal certification or independent audit is claimed.
