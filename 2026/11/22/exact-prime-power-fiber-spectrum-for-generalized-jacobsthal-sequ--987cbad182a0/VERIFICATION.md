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

# Reproducible checks and scope

Run `python3 verify_jacobsthal.py` with Python 3 standard library. The deterministic script independently computes sequence values using the recurrence (not the Binet formula), verifies primitive roots by exact modular-order tests, compares every target's observed fiber to the Legendre-indicator formula, counts all three histogram entries, and tests character intersections and the period state.

The observed output is `VERIFY_OK cases=76 targets=583944 sequence_terms=566784` for tested prime-power moduli at most 100000 with primes from 5 through 47. These are **finite** checks only. The all-parameter theorem follows instead from the exact least-period argument, two cyclic unit-group branches, quadratic character overlap, and counting. Primes below five, nonprimitive parameters, general composite moduli, and Artin-type infinitude are not covered.

No independent audit or independent validation has been performed.
