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

A standalone C++17 verifier, `verify_cycle.cpp`, was compiled with `-O3 -Wall -Wextra` and executed from the material being packaged. The output ended `CYCLE_INDEPENDENT_SECURE_VERIFY_OK` after all orders 4 through 22 matched. It compares a direct adjacency-based test of independence, domination and every possible defending neighbor swap with a separately coded cyclic-gap predicate and a separately evaluated binomial tiling census.

Finite enumeration validates the stated small cases and detects local errors but does not prove the assertion for arbitrarily large cycles. The full proof for all orders is the local gap necessity/sufficiency argument and the canonical tiling bijection in RESULT.md. The root-based asymptotic uses dominant simple poles and the relatively prime lengths two and seven. Compilation requires only a C++17 compiler and the standard library.
