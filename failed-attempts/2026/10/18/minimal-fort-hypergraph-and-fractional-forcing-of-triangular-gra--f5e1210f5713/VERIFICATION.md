---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For an absent base edge uv, the number of selected neighbors in the line graph is d_F(u)+d_F(v), without double counting. Thus a nonempty edge set is a fort iff it covers all base vertices or has no degree-one vertex. Every edge cover contains a minimal edge cover; such a cover has a degree-one endpoint on every edge and is a spanning star forest. No proper subset still covers all vertices, and a nonempty proper subset, being acyclic and nonspanning, has an isolate and a degree-one vertex. Conversely, a nonspanning fort contains a cycle, which itself is a nonspanning fort with no proper fort subset. Isolated edges have only one realization per pair; larger star components have one choice per center. The exponential formula and the unoriented cycle count give the exact total. A matching or a matching plus a three-vertex star attains the edge-cover minimum; proper triangles exist for n≥4, giving the claimed minimum size. Summing minimum-fort LP constraints over all base permutations gives the exact uniform optimum; Steiner triples partition the base edges and attain the size upper bound on fort packing for the specified orders. The frozen code and outputs were read, not run. The n=7 check draws 80,000 random subsets and conditionally tests the fort ones, not 80,000 guaranteed forts; the exhaustive candidate total includes the empty mask in each board's tally but the code tests only nonempty forts. These reporting details do not affect the proof.

## originality

FAIL

The distinct 2026/10/13 Resultary theorem covers the same minimal-fort classification on a broader domain and gives a stronger cardinality-marked enumerator. Its specialization at weight one gives both terms of the frozen total, and its stated smallest sizes agree. The scalar fractional formula follows mechanically from this covered minimum size and vertex transitivity, regardless of the inaccessible Johnson failed-forcing paper. The packing equality at Steiner orders is not stated in the inspected matching catalogue Finding, but it needs no new packing result: use the covered triangle class and minimum size with the classical Steiner triple decomposition and the immediate cardinality bound. No independently valuable non-covered claim survives as a repair. This is statement coverage and implication, not a claim about historical priority.

## value

PASS

The original mathematical content as a whole is substantial for a natural line-graph family: the complete obstruction hypergraph distinguishes structurally different types and supplies a labeled enumerator useful beyond the scalar minimum. These valuable components are covered, however. The two routine optimization consequences by themselves do not provide a valuable narrowed repair under the same standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
