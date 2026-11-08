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

# Reproducibility and scope

Run `python3 verify.py` using a standard Python 3 interpreter. No third-party dependencies, external datasets, or network calls are needed.

The program constructs the claimed bivariate formal-series coefficients exactly over the integers from the rational expression, generates adjacency-distinct palindromes independently, and tests universality by subsequence matching against every word over the fixed alphabet through the largest possible index. It compares all distribution cells for half-lengths through 9, 8, 7, 6, and 5 when the alphabet sizes are 2, 3, 4, 5, and 6 respectively. For alphabet sizes 2 through 8 it also tests the coefficient recurrence, conservation of the total number of valid palindromes through half-length 56, and the sharp minima through universality level 7. It compares the ternary closed-form binomial coefficients through half-length 50.

Actual execution:

`VERIFY_OK q=2..8 half_length<=56 brute_palindromes=65414 extremal_checks=49 ternary_coefficients=0..50`

The proof in RESULT.md establishes the complete infinite statement. The finite checks do not claim to certify an unbounded parameter range by enumeration. No independent scientific audit has been performed.
