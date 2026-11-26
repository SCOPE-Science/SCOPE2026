---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Two distinct generating circles meet at at most two points, so after removing duplicates there are finitely many active-pair intervals. Inside the projection every disk has positive radius on the fiber and the body has a positive-width fiber. On each cell put f_i(y)=√(1−(y−b_i)²). Direct differentiation gives f_i′=−(y−b_i)/f_i and f_i″=−(1−(y−b_i)²)^(−3/2). Therefore curvature of the averaged graph is the Jensen ratio for Φ(t)=(1+t²)^(3/2), with Φ″=3(1+2t²)/√(1+t²)>0. Equality is equivalent to equal cap slopes, and hence equal transverse heights. A finite union of unit-circle boundary arcs cannot contain an open strict-curvature arc. For the converse, when b_i=b_j, the two symmetral arcs have centers ((a_j−a_i)/2,b_i) and ((a_i−a_j)/2,b_i). In fact the symmetral of the active pair's lens is exactly its horizontal translate with those centers (including i=j); fiberwise monotonicity makes both disks contain S(K). This also confirms the submitted support-disk argument using Theorem 4.1. The arc closures cover switching points and projection extremes by continuity; extremes have singleton fibers since a finite intersection of unit disks is strictly convex. If a point in the intersection of the selected disks lay outside S(K), a segment from an interior point to it would cross a selected circle before reaching its endpoint, impossible since that segment is strictly interior to every selected disk before the endpoint. For the centered lens, when either center coordinate is zero the lens is reflection-invariant. Otherwise at y=0 one disk uniquely supplies each endpoint, q and −q differ, and the width is positive by p²+q²<1. This gives κ(0)=(1−q²)^(−3/2), or (25/21)^(3/2) at the frozen example. The prior preservation theorem and a dense countable set of containing disk centers give countable representability by continuity in the center. Replay: RESULT.md §§1–5 and the differentiations/contact argument above; no uploaded code or numerical threshold is needed.

## originality

PASS

Qualified for the finite-representation equivalence and its exact directional lens consequence, not for Steiner preservation of planar ball-bodies or the curvature inequality. This is a close extension of the prior proof, with finite active pairs and disk reconstruction supplying the new global conclusion.

## value

PASS

A usable exact test of whether a common symmetrization preserves a finite generating family is a natural representational distinction beyond preservation of the ambient class. The classification covers any finite input and already shows a sharp distinction for the two-generator lens. It does not optimize the finite number of disks or claim approximation rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
