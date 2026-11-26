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

Normalize the deleted graph edge to 01--23 by permuting the ground labels. Each new face contains both endpoints and a third selected pair disjoint from one endpoint. A selected pair disjoint from both would already have degree two in the faulted graph. Hence an external label occurs, and each pair containing an external label contains exactly one of them. Two such pairs with distinct external labels either give the same fixed endpoint two neighbors, or are disjoint from one another and each already has a fixed neighbor. Thus all new faces use exactly one external label. Independently enumerating all 1024 subsets of the ten pair vertices on five ground labels gives 261 intact and 285 faulted faces including the empty face; the extras by size are 4,12,8. Each of the twelve table rows has precisely its stated strict coface after earlier removals. Downward closure rules out intact cofaces of a new face and support uniqueness rules out cofaces in any other block. This proves the exact relative collapse and counts for all n>=5, not just the local case. The intact three-skeleton equivalence supplies the credited sphere-wedge corollary.

## originality

PASS

The supported distinct claim is the single-graph-edge relative collapse and its exact relative face count. The intact homotopy classification and intact structural results are prior coverage and receive no novelty credit. No distinct equivalent collapse was found in the inspected sources.

## value

PASS

The exact relative collapse answers a natural stability question for an established complex. It determines the map of interest, not just the agreement of two abstract homotopy types. The five-label localization explains why an edge fault can create linearly many faces without altering the simple-homotopy type and gives a reusable local certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
