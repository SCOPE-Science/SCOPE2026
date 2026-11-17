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
# Reproducibility

Run `python CHECK.py` with Python 3, SymPy, mpmath, NumPy and SciPy installed. The expected final line is `GLOBAL_ISOCHRON_HYPERGEOMETRIC_CHECK_OK`. The checker rederives the source polynomial shear and logistic radial identity symbolically, substitutes the hypergeometric basis into the associated Gauss ordinary differential equation numerically on both sides of the cycle, and verifies exact phase covariance on five representative original-time trajectories, including interior, exterior and on-cycle starts.

Proof of the universal result is contained in `RESULT.md`; no finite set of tests can establish its all-parameter or all-initial-data statement. The hypergeometric function may require analytic continuation for large exterior radii, and high-precision evaluation is advisable close to the limiting cases. Published results on the cycle itself (period, physical-time phase density, Floquet multiplier) are prior work, not independently discovered in this contribution.

The self-review is recorded in `REVIEW.md` and `AUDIT.json`. No independent validation has been performed.
