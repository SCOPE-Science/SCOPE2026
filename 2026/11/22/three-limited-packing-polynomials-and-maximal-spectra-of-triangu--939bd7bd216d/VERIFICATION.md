---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

In the selected-edge graph H⊆K_n, the neighborhood of each root pair uv contains d(u)+d(v)−1_{uv selected} selected edges; the test includes missing root edges. Degree ≥4 fails at an incident edge. Degree three forces every positive-degree vertex to be a leaf adjacent to that same center. With maximum degree two, all degree-two vertices are adjacent pairwise, so there are at most three; 0, 1, 2 and 3 yield a matching, one P₃, one P₄, or one triangle, with remaining edges a disjoint matching. All satisfy the inequality. Labelled core weights are 3/3!, 12/4!, 1/3! and 4/4! for P₃, P₄, triangle and lone star; the first three multiply the matching EGF while the star permits isolates only. For maximality, a matching extends when n≥3, and P₃ can close to a triangle. The star is saturated. A P₄ or triangle has at least two degree-two vertices, so increasing any of their degrees gives a forbidden non-star configuration. If no degree-two vertex is touched, an increased degree-one vertex could not be adjacent to all the preexisting degree-two vertices, so an extension must join two isolates. Thus zero or one isolate is exactly the condition for maximality. Multiplying the core weights by perfect matching counts on the other roots and by the isolate factor mandated by parity gives the stated coefficients (with a single full triangle at n=3). The coinciding size-three contributions at n=4 and n=5, the maximum formula, and the parity-dependent facet spectra all agree.

## originality

PASS

Bounded comparisons support the exact closed-capacity-three classification and both labelled enumerators. The closest same-host polynomials concern distinct tests, and the same-day closed-capacity-three rook result has a different root graph and no corresponding triangular facet law.

## value

PASS

On the natural Johnson family the classification yields every labelled coefficient, not just a maximum. The facet polynomial exposes a strong qualitative gap: even orders have only a fixed-size star stratum and the largest stratum although their cardinalities separate arbitrarily far. Those exact multiplicities and the odd-order alternatives are useful data not supplied by general packing bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
