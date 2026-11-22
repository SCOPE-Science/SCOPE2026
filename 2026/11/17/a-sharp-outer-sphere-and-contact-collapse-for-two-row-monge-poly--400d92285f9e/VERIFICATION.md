---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For every q>=2, the monotone row differences y=a-b generate terminal top and initial bottom interval rays plus coincident column pairs, giving the 3q vertices A_k,B_k,C_j after normalization. The proposed c has weighted representation c=q/[4(q-1)]*(A1+B1)+1/[2(q-1)]*sum_{j=2}^{q-1}C_j and squared norm (q+2)/[8(q-1)]. Direct vertex squared-distance inequalities give radius squared (5q-6)/[8(q-1)], with equality all six vertices at q=2 and only A1,B1,C2..C_{q-1} for q>=3. The positive contact barycenter identity forces any other center z to have enclosing squared radius at least R^2+||z-c||^2; strict convexity excludes nonvertex contacts and yields uniqueness. Norm <=1 of nonnegative simplex vectors makes diameter sqrt2 only A1 vs B1. Independently reconstructed exact rational c, every vertex distance and full contact set at q=2,3,4,7; finite checks corroborate the universal proof.

## originality

PASS

Best-of-knowledge comparison against actual published findings, the identified primary literature, and explicit mathematical implication checks distinguishes known ingredients from this result; residual inaccessible or unindexed literature is not assumed absent.

## value

PASS

The Monge polytope is a natural canonical polytope family and the minimum enclosing Euclidean ball is an intrinsic, non-affine-invariant geometric invariant distinct from known inball, centroid, and volume. Exact center/radius, the sharp q=2 to q>=3 contact collapse, and the unique extremal pair answer a mathematically motivated geometry question for every number of columns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
