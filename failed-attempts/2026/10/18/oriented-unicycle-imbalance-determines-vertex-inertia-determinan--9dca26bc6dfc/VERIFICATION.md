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

For the population covariance on the Euclidean zero-sum space, the intrinsic determinant is n times a reduced principal cofactor. The augmented incidence Gram determinant is m^n times that cofactor by Schur complementation. Disconnected minors vanish by rank, and a spanning unicycle minor is the imbalance up to sign by the unimodular tree basis and its signed fundamental cycle. Every cycle extends to a spanning unicycle, so the vanishing criterion includes trees and semi-balanced orientations. The other Schur complement yields the matrix-tree/pseudoinverse expression; the row-space projector accounts for the squared norm. On K_n the restriction is (n/m)I-ss^T/m^2. Partial score sums are bounded by k(n-k), attained by the transitive score vector; strict convexity characterizes equality, and parity gives the regular/near-regular opposite endpoints. Even orders are realized by adjoining a vertex to an odd regular tournament with wins and losses split by one. These give the stated count, spectrum, condition numbers, and four-vertex examples. Reviewed RESULT.md proof and checker.py (especially covariance_cofactor, unicycle_imbalance_squared and tournament_check). The recorded finite checks are supplementary and were not executed for this review.

## originality

FAIL

The main all-graph identity is the quadratic coefficient of Forman's matrix-CRSF theorem for a uniform small phase along the chosen orientation. The precise centered covariance normalization follows from rescaling the constant row; see the implication below. This is positive proof of coverage of the main identity, not an inference from a missing search hit. The projection form and tournament specializations are elementary Schur complement, complete-graph spectrum and score consequences, not an independently surviving substantive finding.

## value

FAIL

Vertex covariance is a natural invariant and the identity is a useful interpretation of the small-phase coefficient. As submitted, however, the main exact invariant is mechanically implied by the stronger determinant theorem. The remaining tournament census and condition bounds are direct applications of the scalar complete-graph Laplacian and classical score extrema, with no separate nonroutine threshold established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
