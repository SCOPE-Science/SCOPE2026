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

The 1/2 distances satisfy the triangle inequality on distinct triples. Translations preserve the graph. In any proposed triangle with ordered part labels a<b<c, two ascending edges give net sheet increment 2 whereas the long edge gives increment 1, impossible modulo m≥2. Thus the middle-stage Rips complex is a graph, and no translation fixes a point of an edge because it preserves the distinct part labels and fixes no vertex. The quotient has exactly one edge over each pair of vertices from distinct parts, 2q vertices and 4·binom(q,2) edges; its cycle rank is b_q. The Borel projection to this graph is a homotopy equivalence by freeness. The orbit metric instead makes its entire flag complex, the join of q two-point spaces, the boundary of the q-dimensional cross-polytope. Below 1 the Borel space has 2q contractible components; at and above 2 the invariant simplex barycenter gives an equivariant contraction to a fixed point, hence Borel type BC_m. The Borel projection to BC_m at the middle stage classifies the cyclic covering. Lifting an oriented triangle of the base graph on three increasing parts and then returning along the long edge changes sheets by 1, so the cover is connected and the classifying map surjects on π₁ and on H₁ over any field. The cyclic resolution alternates 0 and multiplication by m with trivial coefficients, giving one target class in every positive degree exactly in characteristic dividing m. Together with the surjective H₀ merger and constant maps within scale ranges these facts give all stated bars, inclusive at 1 and 2. Read VERIFICATION.md and verify_voltage_graph.py as text; the enumeration tests finite graph properties, not the Borel persistence maps.

## originality

PASS

The possible failure of coherent lifts and the standard cyclic-group homology are already known. The inspected results do not supply the explicit all-degree persistent homology counterexample with free middle-stage action and full barcode comparison. The frozen binary metric demonstrates the comparison under actual freeness; its nontrivial scale is outside Alsulami's particular sufficient half-orbit-distance cutoff, so it should not be described as directly violating a claim restricted to that numerical cutoff.

## value

PASS

This explicit family separates the geometric and Borel notions from the flag complex computed by an orbit-distance algorithm in every prescribed degree ≥2, even when the action really is free on the relevant realization. Computing the transition maps and modular tails additionally clarifies why a later contractible Rips complex need not terminate all Borel persistence. The elementary construction answers a structural algorithmic comparison question rather than just enumerating a small complex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
