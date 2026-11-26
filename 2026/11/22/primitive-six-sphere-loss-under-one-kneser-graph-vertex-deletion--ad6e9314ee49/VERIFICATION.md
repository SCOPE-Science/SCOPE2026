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

Independent proof: send each nonempty face of the neighborhood complex to the union of its duads. The full support poset P consists of subsets of sizes 2, 3 and 4 of the six-element ground set. The punctured support poset P' deletes exactly v and its complementary four-set W: no face uses the vertex v, and a support of size four can fail only when its unique witness is v. For smaller allowed supports there is a surviving disjoint witness. On either poset the reverse map assigns all surviving duads contained in a support. Its union is that support, and applying reverse after forward enlarges a face. The order homotopy lemma gives equivalences on both levels, and the forward maps commute with inclusion. The order complexes of P and P' are two-dimensional and simply connected. To see this, start with the poset of nonempty subsets of size at most 4 (remove W first for P'); its realization is a subdivided 3-skeleton with the complete 2-skeleton retained. In the punctured case, remove v next: its link is the suspension of the subdivided K4 on its strict supersets, hence simply connected. Now delete the singleton vertices. A singleton link is the poset complex of subsets of the five remaining labels of size 1–3. In the punctured case it is missing either one singleton or one triple. For a missing singleton, strip that label from every subset, an order deformation to a full 2-skeleton on four labels. For a missing triple, choose a base vertex outside it; all triangular relations through that vertex remain and kill the fundamental group. These links are connected and simply connected and other singleton deletions do not change them. At each deletion the removed star is a cone with that link as intersection, so connectivity and simple connectivity are preserved by van Kampen. The order-complex face vectors are (50,210,180) and (48,190,156); thus the free H2 ranks are 19 and 13 and the absolute wedges follow by Hurewicz and homology Whitehead. In the pair the omitted supports v and W are incomparable, so the relative chain complex splits into the two cone-link pairs. Each link in P is a subdivided K4: above v, take singletons and pairs of its complement; below W, take the incidence of triples and pairs in W, dual to the same graph. Each gives H2=Z^3 and no other relative homology. The pair long exact sequence now gives a primitive injection with quotient Z^6. Transitivity covers any v. An independent finite enumeration over duad collections reproduced both recorded neighborhood face vectors and the support-poset counts; the proof does not depend on replaying the frozen collapse, Tietze or chain certificate.

## originality

PASS

The intact nineteen-sphere case is explicitly prior work. The distinct graph-vertex puncture and its natural primitive six-class loss are not covered by the inspected same-graph edge fault, the Kneser independence-complex puncture or the intact neighborhood-complex matching. A support-poset reduction matches neither the deletion model nor the ranks in the inspected punctured Boolean-poset theorem.

## value

PASS

KG(6,2) is the first two-dimensional wedge case of a standard Kneser neighborhood-complex family. Its unique type of vertex fault tests actual robustness of the graph construction, not just homology after removing a simplex vertex. The rank and saturation of the natural map distinguish the two roles of a graph vertex as member and witness; on the support model each accounts for three relative degree-two generators. This is a motivated exact invariant of the canonical graph and inclusion, not an existing absolute Betti number or an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
