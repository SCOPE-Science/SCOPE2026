---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Directly reconstructed the C-infinity periodic flat bump b, delta=pi/100, epsilon=delta^2/1000 and disjoint translate supports for alpha in [pi/4,pi/2]. The supplied second-derivative bound gives h+h''>1-32/1000>0; the normal curve is a strictly convex support boundary. Integrating any bounded Borel function of a finite jet over the complement and two translated intervals gives a joint law independent of alpha. Curvature-radius weighting similarly handles boundary-arclength sampling even for k<2. Support area and perimeter integrals give A=pi+4 epsilon B+2 epsilon^2 C and P=2pi+4 epsilon B without mixed terms; separation of bump centers is a rigid-motion invariant. Cross-covariance at t=pi/3 is exactly epsilon^2/pi integral b^2 for alpha=pi/3 but zero for alpha=pi/2. Finite quadrature only illustrates, never proves all orders.

## originality

PASS

The exact one-point jet law combined with fixed two global intrinsic quantities and smooth strict convexity is not mathematically implied by the examined planar unlabeled-width examples (which have unequal areas), curvature-signature set examples, or polygonal classification. Piece-rearrangement mechanisms are older and acknowledged. Priority is best-of-knowledge rather than exclusive novelty certification.

## value

PASS

A concrete identifiability obstruction in natural convex-shape inverse data persists after simultaneously conditioning on area, perimeter, positive curvature and all finite one-direction derivative statistics; its explicit two-direction separating statistic identifies precisely the additional information needed. This is mathematically stronger than a mere width histogram anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
