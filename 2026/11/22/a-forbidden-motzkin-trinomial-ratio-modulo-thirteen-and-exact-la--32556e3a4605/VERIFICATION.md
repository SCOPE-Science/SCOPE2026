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

The attached standard-library verifier `verify_ratio.py` reconstructs the first 2,501 Motzkin and central-trinomial values independently as exact integers. It tests the integer identity and finite-prime digit/carry formulas, then independently enumerates the complete modulo-thirteen ratio census through index 28,560 and compares the resulting four block distributions with the closed formula.

The infinite statement is established by the elementary Lucas and carry-cylinder proof in RESULT.md, not by the finite enumeration. For other odd primes with a vanishing digit coefficient, modular quotient definitions are intentionally excluded. Independent validation of the mathematical argument and novelty has not been performed.
