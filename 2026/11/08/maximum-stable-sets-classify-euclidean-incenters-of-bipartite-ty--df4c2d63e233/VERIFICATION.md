---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For connected bipartite G, each edge-root constraint in the polar Q is |y_i|+|y_j|<=1, rendering ±e_i redundant. In every orthant the nonnegative edge-incidence inequalities have totally unimodular matrix and integral right sides, giving 0/1 independent-set vertices; the full polar vertices are exactly all signings of inclusion-maximal independent sets. Central symmetry makes maximal Euclidean inradius 1/max||q||=1/sqrt(alpha(G)). The optimal center support inequalities are sum_{i in I}|c_i|<=1-sqrt(|I|/alpha), and the active constraints from maximum sets force c_i=0 on U(G), leaving a relative full neighborhood on its complement; hence affdim=n-|U|. For odd P_{2k+1}, the unique maximum independent set is the odd positions and the center set is the k-dimensional even-coordinate l1 ball of radius 1-sqrt(k/(k+1)); for even paths, both parity classes cover V, making center unique. The tree bound floor((n-1)/2) follows by bipartition and is attained by odd paths or the specified even-order leaf attachment. Independent enumeration of all independent sets on P_n, n=2..8, reproduced alpha and center dimensions 0,k alternately. The proof is universal; enumeration is corroborative.

## originality

PASS

Bipartite total unimodularity and the stable-set interpretation of the polar are classical and credited. The new final claim is the exact Euclidean inball radius, complete center polytope, affine-dimension formula, and sharp tree extremum in the canonical type-B root realization. Ohsugi--Tsuchiya investigate reflexivity, h-star and triangulations, not this Euclidean center-locus theorem in the relevant inspected sections. Similar inball theorems for type-A symmetric edge polytopes, graph associahedra, zonotopes or a graph-matching polytope cannot be transferred by name: their polar bodies and metrics are not this Q. An earlier formulation in unconditional-stable-set/antiblocking convexity remains a relevant priority risk.

## value

PASS

The Euclidean incenter set is a natural metric invariant of canonical graph-root polytopes, not an arbitrary optimization at a handpicked graph. The formula identifies all nonunique centers through the maximum-stable-set coverage U(G), a structural combinatorial statistic, and determines exact path geometry and a sharp extremal dimension across every tree order. The elementary TU ingredient alone is not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
