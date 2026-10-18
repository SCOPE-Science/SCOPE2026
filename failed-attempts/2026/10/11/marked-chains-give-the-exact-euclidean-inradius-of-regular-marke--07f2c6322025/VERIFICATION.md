---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

FAIL

The shifted facet/weighted-path proof was independently reconstructed and is sound for positive-dimensional regular marked order polytopes: marked/unmarked cover normals have norm 1, unmarked/unmarked covers sqrt(2); summation gives necessary marked-chain barriers, longest-path potentials give sufficiency, zero slacks tangency and dual extrema characterize incenters. BUT the quantified hypotheses as written admit P={a}, P*={a} with a single marked vertex (more generally all-marked antichain): it is finite, all extrema marked, regular vacuously (no cover relations), and the projected order polytope is a point in R^0. There are no marked interval chains at all, so the stated min_C is a minimum over the empty set and no finite Euclidean inradius is defined as claimed; in R^0 every radius-ball is that same point (infinite supremal radius by the ambient zero-dimensional convention). The theorem lacks the essential positive free-coordinate/nonempty-chain hypothesis. This is an actual boundary counterexample to the advertised universal statement, not a finite experiment extrapolated to an infinity claim. A correct restricted theorem survives, but no full corrected scientific files were supplied; do not mark original passed/repaired.

## originality

PASS

Best-of-knowledge, Pegel’s original marked-order source proves that regular cover relations are exactly the facets, but does not state the Euclidean inradius or all incenter solution; Fang et al. discuss deformations/transfer maps rather than this metric Chebyshev problem. Other published Resultary results for ordinary, lecture-hall and signed order polytopes involve special markings or different norm realizations and do not imply the general competing prescribed mark gaps. Generic weighted-difference-constraint longest-path duality is a significant algorithmic antecedent, however; no claim of originality for that general LP principle. The original scientific claim is nevertheless rejected solely for the included zero-free-coordinate boundary, not for literature access.

## value

PASS

The substantive nondegenerate theorem would give a useful exact metric invariant and the entire Chebyshev-center locus for marked order polytopes with multiple independently prescribed marking gaps, generalizing the ordinary single-gap order-polytope case. The marked-chain bottleneck and forced facets are naturally motivated and not just a random finite example. This value judgment does not rescue the false all-poset quantification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
