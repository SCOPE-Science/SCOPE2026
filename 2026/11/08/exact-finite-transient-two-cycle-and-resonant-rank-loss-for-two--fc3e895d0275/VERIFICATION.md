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

The theorem follows from the exact two-singular-value map in `RESULT.md`. The classification is exhaustive because for any full-row-rank two-row matrix the contrast lies in \([0,1)\); its branches are disjoint and account for equality, resonance, and the nonresonant invariant interval. The universal and infinite-time conclusions are analytic.

Run `python3 checker.py` with Python 3 and NumPy. The checker performs exact-rational SVD-diagonal calculations for both step-size signs, resonances \(r=c^k\) for \(1\le k\le5\), their subsequent rank-one steps, and invariant equal-singular starts. It also runs 300 seeded tests with random orthonormal left/right singular vectors and 2, 3, and 8 columns, checking the full matrix two-step identity at nonresonant contrasts.

Actual package-source result: `VERIFY_OK exact rank-loss and two-step rational checks; 300 random-frame cases; max residual 2.520e-14`.

Numerical checks are supplementary and do not replace the proof. Near-resonant numerical ranks can be sensitive to floating-point rounding. Independent audit has not been performed.
