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

# Verification of coefficient trichotomy

The exact proof is in `RESULT.md`: cancellation of endpoint divisors, strict bound \(T_n(d)>n^sd^r/2\) for every proper divisor, an off-central factor pair for all composites except prime squares, and the exact unique central factor for a prime square.

Run `python3 prime_square_detector_verify.py` from the directory containing this file and the checker. The checker uses independent full-divisor enumeration, proper-divisor sum and multiplicative prime-power factorization. Its output is copied in `prime_square_detector_checks.txt`. The experiment checks 67,172 cases, tests all three arithmetic branches, compares exact squares to avoid rounding, and verifies every prime-square formula in its range. It does not test arbitrarily large arguments and is not a substitute for the infinite proof.

Primary-source comparison: full accessible 2024 Craig–van Ittersum–Ono text; full accessible 2026 published coefficient-content statement; later 2026 Allen–Craig abstract only. The latter paper remains a material originality-access limitation. No independent audit or external certification is claimed.
