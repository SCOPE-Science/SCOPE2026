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

# Reproducibility

The standalone `verify.py` runs with Python 3 and the standard library. It checks exactly the two second-difference conditions against the four actual graph points for all moduli 1 through 90, verifies the multiplicative exact count and the maximizing step order, checks nine-term extension for moduli through 30, and checks valuation-sum formulas at primes 2, 3, 5, 7, 11, and 13 for exponents one through eight. The tests are finite sanity checks, not proof of the all-moduli theorem. The mathematical proof in `RESULT.md` is self-contained and uses no external software.

Run: `python3 verify.py`.
