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

# Verification of the ball–cube metric-projection coefficient

The proof uses (i) the KKT clipping scale with a Euclidean-ball multiplier, (ii) the exact block derivative \(s^{-1}(I-uu^{\mathsf T})\) on each fixed active face, (iii) a sharp Cauchy–Schwarz row-sum argument under componentwise caps, (iv) a one-variable scalar maximization, (v) integration of piecewise differentiable local bounds, and (vi) explicit KKT witness sequences whose multipliers tend to zero. The formula handles all integers \(n\ge2\), positive radii, and relevant active-face sizes; the pure-cube endpoint is treated separately.

A standalone source file, `CHECK.py`, was executed using Python's standard library and reported 2,951 passing finite checks. It tests randomized numerical derivatives, analytic special values, the \(r\uparrow\sqrt n\) limit, and the thirteen-coordinate capped-face witness. The checker is a reproducibility aid, not a proof of the universal quantifiers. Its default run does not require data files or nonstandard libraries.

There is no independent external mathematical audit. Literature priority is assessed against the sources specifically named in the scientific review and is subject to unindexed-equivalence risk.
