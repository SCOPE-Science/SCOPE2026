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

# Verification

The normalized monomial formula follows directly from differentiation and repeated integration; the full proof in RESULT.md verifies the derivative cutoff for every nonnegative input degree. The exceptional sole column of the \((h+1)\)-st jet finite difference is calculated with its sign and exact factorial coefficient. All lower-order leading polynomial coefficients are identified symbolically and converted to sharp spectral tails by rearrangement. The closed span and minimum-cardinality statements are proved by matrix-unit density and a Vandermonde determinant.

Run `python3 CHECK.py` from this extracted package. The deterministic program outputs `JET_DIFFERENCE_VERIFY_OK 9008`; it tests 9,008 exact finite assertions on small orders and monomial degrees. These finite checks do not independently certify any unbounded family or infinite-dimensional conclusion, which follows only from the written arguments.

The closest published operator studies product commutators and the original paper provides the underlying monomial weights; neither furnishes the claimed additive finite-difference classification as a stated result. Priority is qualified by the risk of an older equivalent in general polynomial symbolic calculus. Independent mathematical audit has not been performed.
