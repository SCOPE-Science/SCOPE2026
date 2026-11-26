---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The nested case is the smaller ball, with no contact with the larger sphere except at internal tangency (where the larger-sphere contact is e₁). In proper overlap the concave squared-distance quadratics determine containment and actual contact sets. The pole prescription makes the smaller-sphere equality set s=−1/d, and the larger quadratic has its clipped vertex at s=1 exactly when (d²q²−1)h≤d²−1. The h map increases from 1−q to 1+q, giving the stated cutoff and retaining the singleton at equality. In the two-latitude branch the negative-square identities place the vertices at t and −1/(dt), both strictly interior to the normalized axis interval. Upon setting z=dt², the derivative of the squared separation has the negative sign of the positive factor in RESULT.md lines 114–121. The separation tends to 1+q at the lower t endpoint and equals Lc at t=1, where h=1+θ and the formulas agree. The two-contact probability measure has axial mean zero and second moment −s₊s₋=1/d, and uniform transverse second moment gives I_d/d (in d=2, equal weights on each two-point latitude). John's sufficient contact criterion therefore establishes unrestricted optimality and uniqueness. Read VERIFICATION.md and verify.py without executing the supplied script; the recorded 675 finite checks supplement, not replace, this proof.

## originality

FAIL

Exact equivalent coverage was verified in distinct indexed records for d=3 and d≥4. The uncovered-by-statement planar slice follows by the same proof and algebra, with no new dimension-two obstruction; the higher-dimensional record expressly notes lower-dimensional applicability of the formulas. The decision credits demonstrated indexed coverage and does not infer who discovered it first from catalogue dates.

## value

FAIL

The contact bifurcation is a natural and useful invariant. Its exact formulas and unrestricted maximality certificate are already covered by the compared classification and proof. Merely rewriting the parameters or restricting to dimension two without a further planar result is not a distinct valuable remainder in this submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
