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

# Verification and exact evidence

The main claim is the sharp formula for \(F_r(2)\) on the full real interval \(1/6\le r\le1/5\), with the stated threshold-to-radius correspondence and two attaining frequency pairs.

The analytic verification consists of: (i) the exact Bernoulli/Fourier formula for every coprime integer pair; (ii) the uniform estimate \(8r^2-Q(r)\ge1/32\), excluding all odd–odd frequency products at least \(16\) and mixed-parity products at least \(4\); (iii) a complete list of nine remaining coprime pairs, on which each probability-minus-bound is affine between \(1/6,3/16,1/5\); and (iv) exact nonnegative rational differences at all three nodes. No finite experiment is used in place of the global analytic estimate.

The standalone dependency-free `CHECK.py` was run from its package path using Python 3. It printed `CHECK_OK` with **834 separate geometric overlap comparisons**, after confirming the exact exceptional-pair list, all nine three-node rational tables, absence of missed interior Bernoulli breakpoints, and candidate formulas at 301 rational parameters. Its rational arithmetic does not require floating-point tolerance. The `RESULT.md` proof carries the infinite-frequency argument, so these checks are supplementary.

Source inspection for originality covered the relevant theorem statements and argument sections of the accessible full HTML versions of arXiv:2610.38135v1 and arXiv:2610.33190v1 and full published mathematical statement/proof text of the two closest indexed threshold-correlation results. Residual limitations: the theorem neither classifies all optimizers nor covers radii outside the stated closed interval; existence of an older unindexed equivalent result cannot be ruled out. Independent verification has not been performed.
