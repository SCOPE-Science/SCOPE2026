---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Flat torus difference is Haar-uniform, and the nearest-lattice representative is uniform in its central Voronoi cell C, so F(r)=vol(C∩B_r)/V and F'(r)=r²(4π-U(r))/V. A Voronoi facet plane has foot v/2 in its relative interior, ensuring its spherical cap is born at r=|v|/2 uncovered. Its area 2π(1-a/r) contributes U' right jump 2π/a. Other caps and crossings have continuous exposed-boundary first variations, so F'' jump equals -2πr m(r)/V; covolume from initial r³ coefficient. Opposite facets counted separately. Independent cube case tested six simultaneous facet births at r=1/2, yielding exact jump -6π. Full-dimensional/general coincident critical radii proof examined; no analytic gap found.

## originality

PASS

PASS, qualified: two-dimensional flat-torus results have square-root births in an angular derivative, while the submitted result is a three-dimensional second-derivative jump law for every Euclidean lattice with simultaneous degeneracies. The Voronoi relevant-vector bijection is classical, but neither the inspected two-dimensional full mathematical theorem nor accessible primary abstracts state or algebraically imply the exact three-dimensional cap coefficient. Source access limits remain.

## value

PASS

PASS: sharp distributional singularities recover the covolume and entire multiset of three-dimensional Voronoi facet distances with multiplicity from the natural pair-distance invariant. The no-spurious-edge/vertex-jump classification is a useful structural inverse-geometric statement, not a small table or routine normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
