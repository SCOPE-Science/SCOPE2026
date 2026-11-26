---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Counting empty and singleton traces, marked nonsingletons, and outside witnesses separately gives m+1+(m-a-b)+h. The full incidence graph is a forest with a+b+c+h vertices and at least 2h edges, so h<=a+b+c-1 and the total is at most 2m+c. At 7q for m=3q, equality forces c=q, a=b=0, every marked component to have exactly three vertices, and h=q-1. The incidence forest has 2q-1 vertices and 2q-2 edges, with each outside witness of degree two; its suppression is the block tree, also valid for q=1. The converse construction supplies exactly one vertex per trace, including an unmarked vertex beyond a private leaf for the empty trace. The triples recover the partition, the internal pairs recover the centres, and the remaining pairs recover both the block tree and labelled attachments. Counting these choices gives the stated factorial/Cayley product and small values; 7q vertices are necessary simply because all 7q traces are distinct. A separate bitmask DFS adding only edges between disconnected endpoints found 36961 labelled forests on seven vertices. Marking the first three vertices yielded 288 saturated hosts and exactly three distinct trace families, one per possible centre. The submitted checker was inspected, not run. Its comment about two reduced tree shapes at q=3 is inaccurate if shape means an unlabelled tree: all the q=3 block trees are paths, with different labels at the centre. That comment does not affect any check or theorem.

## originality

FAIL

The prior Theorem 2 proof and construction of Berthe–Foucaud–Lehtilä–Parreau already yield the classification at zero rounding slack by taking equality in their displayed inequalities. Their construction gives every proposed choice, with minimum order. The only extra outside-incidence observation is immediate from the auxiliary forest in that proof, and the census is the direct labelled count of the resulting choices. The exact formula need not have been printed previously for this to be covered as a routine corollary. This is a demonstrated mathematical implication, not a judgment based on missing access or on shared keywords.

## value

FAIL

The census concerns a natural invariant and may be convenient as an explicitly stated corollary. As an independent finding, however, it supplies no nonmechanical refinement beyond the zero-slack equality of the known proof and the direct labelled count of the known freely parametrized construction. Its exact minimum order is already realized by the earlier construction and needs only one vertex per trace for the lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
