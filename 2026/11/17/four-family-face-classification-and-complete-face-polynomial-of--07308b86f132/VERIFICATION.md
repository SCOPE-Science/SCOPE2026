---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Root differences within each part, together with r_11, span the full (p+q−1)-dimensional zero-sum space; singleton signed rectangles expose every generator as a vertex. For potentials h,g the opposite-orientation maxima are max h−min g and max g−min h. A strict winner exposes just its extremal rectangle. In a positive tie, the two potential ranges share a midpoint; both nonzero widths give two rectangles with disjoint support, and exactly one zero width gives the corresponding constant-part case. Assigning the proposed extremal values realizes all listed data; projecting the two signed rectangles back to the parts recovers their labels, so the classification is disjoint. For Type II the internal direction spaces are disjoint and the sum over S_+ distinguishes the components, giving the independent join direction. In Types III–IV the two components share the constant part's zero-sum direction space, have independent direction spaces on the split part, and the sum over the first part distinguishes forward from reverse vertices. This gives the dimension shifts in the four generating terms and containment of signed vertex sets gives all incidences. The coefficient of t is 2[p binom(q,2)+q binom(p,2)]+4 binom(p,2)binom(q,2)=pq(pq−1). The top coefficient is 2+(2^q−2)+(2^p−2). At rank two Type I gives the listed simplex products, Type II is a point joined to an edge, and the constant-part cases contribute quadrilaterals only for a part of size two. In particular (2,2) gives the face vector (8,12,6), with all six two-faces quadrilateral. The nested verification/verify_bipartite_faces.py was located and inspected, not executed; it uses numerical supporting hyperplanes and ranks and checks integer counts at eight finite pairs. The all-parameter judgment is based on the exact support and dimension proof, not those numerical tests.

## originality

PASS

Existing facet potentials, connected face-subgraph criteria, edge counts, and Ehrhart invariants substantially overlap the setup and some ranks. Pass applies to the disjoint signed-vertex classification, dimensional enumeration and closed all-rank polynomial, not to those inputs or special counts. The comparisons support that distinction without settling historical priority.

## value

PASS

This is a complete classification for a natural two-parameter graph family, not an arbitrary small-rank sample. Recovering actual signed vertex sets supplies incidences and distinguishes faces with the same dimension. The polynomial gives a direct alternative to reconstructing and deduplicating all facet intersections for each graph; the same rank analysis accounts for the exceptional quadrilateral contributions when one part has size two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
