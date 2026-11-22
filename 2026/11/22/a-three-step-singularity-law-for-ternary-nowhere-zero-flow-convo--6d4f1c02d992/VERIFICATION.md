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

# Reproducible finite checks

Run `python3 check.py` with Python 3 and no external dependencies. The checker independently enumerates every valid nonzero checksum-zero ternary word, directly computes its phase contribution at each Fourier frequency, and checks that the result is the stated signed integer multiplier. For every length from two through nine it also checks the frequency-zero classification and predicted multinomial nullity. The expected final output is `VERIFY_OK direct_character_frequencies=29520 lengths=2..9`.

This finite computation tests 29,520 frequencies but does not substitute for the all-length factorization and integer-parity proof in RESULT.md. The Fourier transform is unnormalized; direct phase counts give a real signed coefficient because the counts for the two nontrivial cube-root phases coincide. The asymptotic formula is proved by Stirling's approximation, not extrapolated from the finite tests. No independent external audit has been performed.
