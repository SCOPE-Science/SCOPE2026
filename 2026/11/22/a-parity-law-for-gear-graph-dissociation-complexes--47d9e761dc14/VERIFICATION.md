---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The selected-degree≤1 condition exactly characterizes the faces. The projection onto hub and original rim vertices is monotone, and every matched incidence toggles one subdivision vertex and is an actual face-poset cover. In a hub fiber at most one original rim vertex is selected; at least n−2 subdivision vertices can be toggled freely. Without the hub, a subdivision vertex joining two selected rim vertices is forbidden. The only pair exclusions left come from the two subdivision neighbors of an isolated selected rim vertex, so the pairs are disjoint. If any allowed subdivision vertex lies in no pair, its toggle matches the whole fiber. Otherwise all rim vertices are selected, or the proper cyclic word has no 00 (which leaves an isolated allowed vertex) and no 11 (a boundary of that run leaves one). This forces exactly the two alternating words for even n, and none for odd n. In each alternating fiber choose one endpoint of each forbidden pair in an ordered list and apply sequential element matching. Equivalently, toggle the chosen endpoint of the first pair whose other endpoint is absent. Only the face containing every other endpoint survives, of size n. The all-selected rim fiber also contributes one size-n face. Patchwork gives acyclicity; restriction to the ordinary nonempty face poset makes the singleton formerly paired with the empty face critical and retains the other pairs. Thus the Morse CW complex has one vertex and one or three (n−1)-cells, attached to a point, proving the sphere wedge without any coefficient assumption. The frozen self-review uses ‘critical facets’ loosely: for n=4 a legitimate alternating unmatched face {u₀,u₂,w₂,w₃} can be extended by u₁. The primary proof correctly says critical faces and needs no facet claim.

## originality

PASS

The discrete-Morse tools and graph construction are established. The identification of precisely two extra alternating fibers and the resulting full gear-graph homotopy formula are not supplied by the examined prior results. This assessment is bounded by the sources inspected.

## value

PASS

This is the homotopy type of a natural cyclic hub-and-rim family at its first higher-independence threshold, in unbounded dimension. A complete family classification with parity changing the number of spheres from one to three is stronger than Euler data or field homology; the proof identifies the exact cyclic-word obstruction using a short uniform matching. It neither promises higher-threshold results nor depends on such promises for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
