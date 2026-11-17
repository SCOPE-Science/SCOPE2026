---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Diagonal invertible rescaling and coordinate sign changes reduce any box to the standard centered cube and normal coefficients a_i=s_i |u_i|. Active support at most three gives product of a centrally symmetric polygon (or segment/point) with intervals, hence a zonotope. Dominance makes the section the graph of a full cube. Otherwise every active-coordinate facet is an offset section of >=3 active cube coordinates. Its capped-simplex y_i in [0,b_i], sum delta=(sum b_i-|t|)/2 has forced hypothetical center coordinate min(b_i,delta)/2, but when no coefficient dominates the truncated sum strictly exceeds 2delta, contradicting the center lying in the slicing hyperplane. The obstruction is a nonsymmetric exposed face, impossible for a zonoid. Boundary equality and inactive factors are covered. Independently computed exact off-center 3-coordinate vertex reflections for all weights 1..3 and positive integral feasible offsets and found agreement; the analytic proof covers real parameters.

## originality

FAIL

FAIL: A fully read October 18 published theorem (A dominance criterion for zonotopal central sections of cubes) states EXACTLY the same all-dimensional equivalence for cubes with arbitrary real normal coefficients including zero coordinates, and contains the same off-center cube-section dominance iff and nonsymmetric-face obstruction. Every rectangular box is the diagonal invertible image of a cube, changing its normal precisely to scaled coefficients s_i u_i; zonoid/zonotope property is affine-invariant. Hence this submitted theorem is an immediate equivalence, not a new extension beyond four dimensions.

## value

FAIL

FAIL as an original scientific contribution: the full normal-support/dominance classification, equality cases, off-center rigidity lemma and exposed-facet obstruction are already proved for all dimensions by the October 18 primary theorem. Recasting it for rectangular boxes via coordinate scaling and a different proof of an identical lemma is a routine change of variables; 6827 finite checks add reproducibility but no new motivated invariant or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
