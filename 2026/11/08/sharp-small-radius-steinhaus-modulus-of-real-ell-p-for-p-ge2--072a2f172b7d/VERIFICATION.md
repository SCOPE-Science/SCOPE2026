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

The universal argument is the real scalar monotonicity inequality, exact two-coordinate equality, and the dimension-free second-derivative bound for the \(\ell_p\) norm on segments that stay at distance at least \(1/2\) from zero. These imply the claimed uniform absolute error before taking either extremum. No external theorem beyond elementary Hölder and one-dimensional integration is required.

To corroborate the scalar step for even integer exponents, run `python3 verify_rational.py`. The test uses only exact fractions and explicitly checks opposite-sign equality and the two-coordinate sharp coefficient. It cannot establish the inequality for every real exponent or every scalar pair; those cases are proved analytically in RESULT.md.

Limitations: no finite-radius exact formula is asserted, the second-order constant need not be optimal, and independent mathematical validation has not been performed.
