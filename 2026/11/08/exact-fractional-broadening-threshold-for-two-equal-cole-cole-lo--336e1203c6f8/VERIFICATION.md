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

# Verification and reproduction

The proof is exact and covers an infinite continuous parameter range. All essential algebra appears in `RESULT.md`: rationalization of the fractional complex susceptibility, transformation \(y=\cosh s\), derivative factorization, strictly decreasing quadratic numerator, and the exact root formula. No finite calculation is used as proof of global uniqueness.

The extracted standalone `verify.py` can be run with `python3 verify.py` using only the Python standard library; it returns `VERIFY_OK checks=1004`. It compares the unsimplified physical Cole–Cole loss with the derived rational expression and checks direct unsimplified derivatives at every predicted outer maximum. It also exercises both sides of each threshold for six exponents, the center values, Debye endpoint, strict monotonicity samples, square-root critical splitting and deep-separation valley asymptotic.

These numerical tests verify finite representative parameter choices and floating-point identities within stated tolerances. They cannot independently prove nonduplication in literature, the global parameter theorem, or the behavior of unequal component strengths or exponents. The proof does not assert experimentally detectable resolution under finite noise or sampling.
