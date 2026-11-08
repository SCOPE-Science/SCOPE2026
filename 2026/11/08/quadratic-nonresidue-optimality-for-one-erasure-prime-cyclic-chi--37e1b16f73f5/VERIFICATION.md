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

# Verification and limits

The complete finite check was run with Python 3 using only the standard library:

`python3 verify_one_erasure.py`

Its exact output was:

`ZC_ONE_ERASURE_CHECK_PASS cyclic_cases=2268 prime_range=3..101`

The checker independently evaluates complex chirps and cyclic correlations, rather than only the derived residue-class formula. Two erasure sites are tested for each root. The finite tests do **not** certify the theorem for larger primes; that conclusion follows from the geometric-sum cancellation, the elementary quadratic-residue coset argument, and the established quadratic Gauss-sum evaluation reproduced in the proof. No external or independent mathematical audit has been performed.
