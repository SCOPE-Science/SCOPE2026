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

The general statements are proved by a cyclic two-state transfer identity, modulo-two Lucas parity, and explicit integer matrix products. The standalone `checker.py` computes multipliers by distinct dynamic-programming and matrix-trace paths; for cycle lengths 3 through 9, it independently enumerates all independent sets. It checks every sign vector for lengths 3 through 16 and verifies the constructed frequency families and all-negative spectral-gap witnesses for lengths through 101.

Observed exact Walsh-zero counts at lengths 3, 6, 9, 12, 15: 3, 18, 111, 696, 4413. At tested lengths not divisible by three there were no zero multipliers. All checks returned `CHECKS_PASS`.

These finite checks are not a proof of the infinite-length assertion and are not an independent audit. The all-length proof is in `RESULT.md`. Exact zero multiplicities beyond the tested lengths are not claimed.
