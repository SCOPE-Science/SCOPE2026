---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The sampling is iid on the entire Euclidean perimeter, so side probabilities are p,q,r; fractional side positions are iid uniform conditional on the labels and are preserved under affine normalization. I independently recovered both conditional coefficients. For two samples on AB and the third at (1-t)B+tC, the ray through the centroid reaches AB at B-fraction u=(2t-1)/(3t-1), admissible for t in [1/2,1]; the AB draws straddle u with probability 2u(1-u). Its integral is (3+4 ln 2)/27. For one point on each edge, noncapture has a unique origin of an open angular semicircle except on a null set. For an origin at AB fraction t, getting both other edges in that half turn requires t>1/2, and captures all of BC and CA fraction (2t-1)/(3t-1). Thus noncapture is three times its integral, 1-2 ln 2/3. All-three-on-one-side capture is impossible. Weighting the patterns by 3p_i^2 p_j and 6pqr yields the stated cubic. The pairwise Schur derivative is -(p_i-p_j)^2(kappa+eta p_k), strictly negative for unequal coordinates. The triangle side simplex has closure 0<=p_i<=1/2 with sum 1; (1/2,1/2,0) majorizes it and the equilateral vector is majorized by it. This gives exactly the asserted equilateral maximum and degenerating infimum, which is approached by genuine triangles but is not attained. Boundary equalities in the sampling geometry form measure-zero sets. The proof and independent conditional calculations suffice; no simulation is used as proof.

## originality

FAIL

The full-boundary iid cubic, both mixed-label probabilities, strict shape ordering, maximum and limiting minimizers are materially duplicated in distinct verified catalogued statements; broader entries also include arbitrary edge-selection weights. This establishes coverage, not who first established the result. Neither the area-sampling precedent nor the one-per-side result accounts for the whole overlap, which is established directly by the full-perimeter records.

## value

FAIL

An all-shape perimeter-capture law is intrinsically useful, but the submitted invariants, sharp ordering and classifications are already covered by a distinct full-boundary treatment, with some catalogued treatments also going beyond arclength weights. As submitted there is no independently useful new classification or theorem left after this coverage; another evaluation of the same coefficients does not fill a separate mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
