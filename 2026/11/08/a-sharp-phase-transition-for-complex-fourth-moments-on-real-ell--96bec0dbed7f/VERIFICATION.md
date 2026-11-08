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

The included `verify.py` uses Python 3 standard library and recomputes all fourth-order real-coordinate polynomial coefficients by a direct independent expansion. Its exact checks cover the cases \(p=1,2,\infty\), dimensions \(2\) through \(7\), 65 integer Gaussian-integer coefficient vectors per dimension and shape, and both nonnegative fourth-moment deficits. Further checks verify the positive sum-of-squares identity, compare the gamma endpoint values in five dimensions and eight shape parameters, and numerically corroborate five cases using a gamma/Dirichlet sampler.

To replay: `python3 verify.py` in the directory containing the extracted artifact. A successful run ends with `ALL_COMPLEX_LP_BALL_FOURTH_MOMENT_CHECKS_OK`. The universal assertions (including all real parameters \(p\) and arbitrarily large integer \(n\)) rely on the human-readable analytic proof in `RESULT.md`, not on finite enumerations or random simulations. No independent external audit has been performed.
