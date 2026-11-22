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

## Actual computational checks
Run `python3 verify_adjacent.py` with the Python standard library. The standalone program checks 19 prime-depth pairs at primes 3, 5, 7, 11, 13 and 17. It enumerates 2,891 indices and compares the direct integer-binomial valuation with a separately implemented Kummer carry recurrence; it independently constructs the full five-state polynomial coefficient table and compares every coefficient with the enumerated joint pairs. The same checker tests the exact signed jump counts, means, variances, covariances and sign classification with rational arithmetic. All assertions passed.

## Mathematical proof and boundaries
The infinite result is justified by the five-state digit transition derivation, exact root counts of two coprime affine integer polynomials, and finite exact carry covariance summation. The computation is not an exhaustive verification for unbounded primes/depths. There is no assertion for the prime two or nonconsecutive indices, and historical novelty has not received independent validation.
