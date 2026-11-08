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

The ordinary Python 3 standard-library file `checker.py` is self-contained. Execute `python checker.py` to enumerate finite labelled block partitions, compute the join of each family using union-find, and compare against the exact recurrence, the common-block factorial moments and the classical alternating-cycle count. The observed terminal marker was `ALL_FINITE_CHECKS_OK`.

This finite computation covers eleven explicitly selected parameter triples (dimensions at most eight worlds, up to three independently chosen partitions). It does not exhaust all input sizes and it does not prove the asymptotic theorem. The infinite statement follows from the analytic inequalities, fixed-moment count and Stirling/entropy estimate written in RESULT.md. No external mathematical audit or machine-checked infinite proof has been performed.
