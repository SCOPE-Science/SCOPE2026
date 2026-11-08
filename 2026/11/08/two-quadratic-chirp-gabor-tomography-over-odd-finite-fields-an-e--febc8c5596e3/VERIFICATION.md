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

# Verification record

`checker.py` uses only the Python standard library. Run `python checker.py` in the same extracted directory. It enumerates the entire finite-field additive ambiguity from the definition for prime orders 3, 5, 7, 11, 13, 17, 19 and extension orders 9, 25, 27, 49, with multiple distinct slope pairs. All finite-field operations use exact integer polynomial arithmetic; root-of-unity sums are floating-complex with tolerance 1e-7. Checks include the complex-valued explicit formula, modulus sector, per-trace fiber multiplicities, rank-nullity, predicted sharp smallest/largest modulus, Gauss-magnitude and Moyal energy. The successful output terminates in `ALL_QUADRATIC_PAIR_AMBIGUITY_CHECKS_PASS`.

The extension field of order 27 has precisely 208 ambiguity zeros among 729 frequencies, giving lifted rank 521. The orders 9, 25 and 49 have no zeros and are fully invertible; all primes tested are also invertible. The proof in `RESULT.md`, not the finite code, establishes the arbitrary-odd-prime-power assertion. A numerical singular-value decomposition on every full matrix was not required: the exact Weyl-basis conjugation argument proves the multiplier-to-singular-value correspondence.

Independent mathematical validation was not performed. Completeness of historical priority is not certified.
