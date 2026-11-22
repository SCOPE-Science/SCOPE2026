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

The polar potential polytope has |f_i|<=1 and |f_i-f_j|<=t. At every vertex some |f_i|=1; the entire cluster is then in [1-t,1] or its negative and a coordinate strictly in the interior can be varied both ways, so exactly the nonempty-subset +/- corner potentials occur, giving 2(2^m-1) facets. Squared centered Euclidean polar normal lengths are Q_m,t(k) with centering over all m+1 sites, with strictly concave k-dependence and vertex alpha=(m-1)/2+1/t; therefore maximizers are nearest integer(s). Central symmetry and opposed support inequalities give global inradius 1/sqrt(max Q), not only an origin-centered optimum. At contact level k=m alone, normals span one radial direction and slack permits an (m-1)-dimensional center family. For k<m, differences of all equal-k subset normals span the m-1 cluster contrast directions and their mean adds radial direction, forcing unique center. This switches exactly at t=2/m, including the tie wall. Independently checked exact rational Q maximizers and binomial contact counts for m=3,4,5,7 at t<,=,>2/m; all matched.

## originality

PASS

Earlier four-point m=3 work lists the 14 polar vertices and exact Banach–Mazur distortion; all-dimensional equiradial-star work optimizes an arbitrary Euclidean ellipsoid in a different metric-distance regime. Neither determines the canonical Euclidean inradius, all-m facet-shell/tangency staircase or sharp fixed-embedding incenter-locus collapse. No dominating named theorem retrieved in semantic searches, but broader historic metric-polytope literature is not exhaustively read.

## value

PASS

This is a natural one-cluster family in finite ultrametric Lipschitz-free geometry. The canonical Euclidean inradius and all maximizing-ball centers are geometric invariants not encoded by Banach–Mazur distortion, and the sharp phase change from (m-1)-dimensional center set to uniqueness at t=2/m is structurally meaningful. Further rational tie walls give full binomial contact counts for all m and t, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
