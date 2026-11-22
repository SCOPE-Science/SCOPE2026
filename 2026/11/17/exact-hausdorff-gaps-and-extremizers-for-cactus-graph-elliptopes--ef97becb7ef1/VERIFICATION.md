---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For an odd-parity signed cycle, the antiperiodic signed adjacency has top eigenvalue 2cos(pi/n), of multiplicity two. The PSD trace bound is attained by a planar Gram matrix, and n>=3 unit-diagonal constraints force unique edge coordinates. For arbitrary weights w, separating m=min|w_i| from residual coefficients bounds the support gap by m(n cos(pi/n)-n+2), with equality only at constant magnitudes; the nearest cut point is ((n-2)/n)xi. One-vertex unions of cactus blocks give exact Cartesian products, whose squared Euclidean distances add. Independent eigenvalue and barycenter checks passed n=3..11; these diagnostics alone do not prove all n.

## originality

PASS

PASS best-of-knowledge: the cycle signed SDP support n cos(pi/n) and Grothendieck ratio n cos(pi/n)/(n-2) are earlier results, and one-vertex graph-body products are also earlier. The new full claim concerns additive Euclidean Hausdorff metric, all maximizing directions, every farthest elliptope point and its unique metric projection, and the cactus square-sum composition. The multiplicative formula does not by itself determine all Euclidean minimizing projections or equality classifications.

## value

PASS

The exact metric distortion of a canonical SDP relaxation and full extremizer geometry quantify an optimization relaxation beyond its known multiplicative integrality ratio. The cactus Pythagorean rather than max law and freely varying bridge coordinates give a natural complete classification, not an arbitrary finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
