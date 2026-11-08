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

# Reproducible mathematical checks

Run `python3 verify_hasse_family.py` with Python 3 and no third-party packages. Successful execution prints `HASSE_POLYNOMIAL_IDENTITY_AND_SQUAREFREE_FINITE_CHECK_PASS` followed by eighteen tested prime/degree pairs and three lines `CARTIER_DIRECT_EXTRACTION_PASS` for primes 5, 11, and 17. The first comparison evaluates \(H_{2q+1}(T)\) in two independent ways, checks the exact factorization modulo each prime and verifies squarefreeness and endpoint values; the second reconstructs Cartier matrix entries from direct exponent filtering in \((x^6+t x^3+1)^n\).

The finite range ends at 149 and is **not** evidence of an infinite-prime statement by itself. The actual proof for every allowed prime uses the central-trinomial differential equation, an invertible coefficient recurrence, and the simple-root argument, with algebraic-closure and smoothness hypotheses stated explicitly in `RESULT.md`. This evidence does not independently verify historical priority or certify a full Newton polygon away from the superspecial locus.
