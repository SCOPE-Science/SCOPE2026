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

# Reproducible scientific checks

Run `python3 CHECKER.py` from this package using Python 3 standard library. Expected terminal markers are `SEVEN_WEIGHT_OPTIMUM_AND_REFLECTION_CHECKS_PASS`, `EIGHTEEN_INDEPENDENT_JUMP_QUADRATURE_CHECKS_PASS`, `FOUR_HUNDRED_TWENTY_SIGNED_MULTIJUMP_TESTS_PASS`, `SHARP_QUADRATIC_BV_STABILITY_CHECKS_PASS`, `ONE_HUNDRED_ONE_MINIMAX_MIXTURE_CHECKS_PASS` and `ALL_REFLECTED_HARDY_BV_CHECKS_PASS`.

Analytically verified identities: the jump response is rational on the two complementary intervals; its exact integrated absolute value is the weighted binary entropy function; the derivative in the jump position is strictly decreasing; midpoint evaluation gives a universal lower bound over mixture weights; Shannon entropy has second derivative at most \(-4\). Arbitrary signed real BV inputs follow by the distributional jump-measure representation and Fubini–Tonelli, not by finite enumeration. The numerical checks sample finitely many jump configurations and do not certify historical originality, infinite-dimensional completeness or independent validation.
