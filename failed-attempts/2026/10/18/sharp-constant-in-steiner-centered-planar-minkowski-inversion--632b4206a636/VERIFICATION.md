---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the perimeter-2π normalization, the displayed Green function has first harmonics zero and satisfies (D²+1)G=δ₀−cos(t)/π: away from 0 this is direct differentiation, and the jump of G′ at 0 is 1. For 0<t<π, |G′(t)|≤1/2−t/(2π)+sin(t)/(4π)≤1/2, with one-sided slope 1/2 at 0. Balance removes the first-harmonic term. The support-function and Kantorovich–Rubinstein formulas therefore give the claimed upper bound. In the lower-bound family, s cos(ε)=1−s gives both horizontal cancellations, reflection cancels the vertical moments, and each support has more than two points. The displayed plan has the required marginals and upper-bounds W₁ by sTε. Substitution at angle zero gives the stated gap 2πsEε; Eε/ε→1/2 and Tε/ε→1 establish the lower bound π. Positive periodic heat convolution preserves balance, gives h+h″>0 for the reconstructed smooth bodies, and converges in W₁. The already proved upper bound then gives convergence of each reconstructed body in Hausdorff distance; the denominator at each fixed positive ε is nonzero. This also proves sharpness in the smooth class, not attainment. Replay is by RESULT.md lines 14–62 and the derivative/first-harmonic checks above. The inspected check.py is optional floating-point corroboration, not an audit or proof; it computes the specified plan's cost but does not separately assert the row/column marginal sums. The analytic marginal check suffices.

## originality

FAIL

An proves the π upper bound but explicitly leaves its optimality open. A distinct indexed record, 2d71ab1e88cd, states and proves the identical exact best constant with the same normalization, metric, domain and smooth-positive restriction. The frozen triangle–rectangle construction differs, but is a witness for that same invariant, not a distinct claimed theorem. The comparator is indexed under 2026-10-25; this is a finding of equivalent existing coverage, not a conclusion about which construction was first or whether either was derived from the other.

## value

PASS

Determining the best constant for a prescribed metric and centering is a meaningful stability question explicitly left open by the cited upper-bound source. The balanced polygonal family explains why requiring nondegeneracy, and even smoothing to strictly positive curvature radius, does not improve the coefficient. This mathematical utility does not remove the exact overlap on originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
