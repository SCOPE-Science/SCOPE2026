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

# Exact reproducibility checks and limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The verified execution returned `RATIONAL_QUADRATIC_COMPOSITE_OK 1102 parameter_cases 309466 raw_comparisons 604026 fibre_shift_tests 91 spike_tests`. The script enumerates reduced numerator classes and denominator values through 60, and compares original floor/gcd indicators with the independent residue model. It also recomputes fiber frequencies by exact rational fractions, verifies predicted periodic shifts and the square-class invariance, and checks the exceptional square-denominator index.

These finite checks cannot establish an infinite theorem. The published proof supplies the full quantifiers, the divisibility arguments for all primes, the CRT density calculation and the square-class congruence. The result is self-reviewed only; independent audit and independent validation have not been performed.
