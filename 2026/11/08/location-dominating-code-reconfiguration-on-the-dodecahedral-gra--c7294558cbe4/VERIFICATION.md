---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For D=GP(10,2), the vertex-indexed 20-edge-neighborhood masks are exactly formed by outer ten-cycle, spokes and step-two inner edges. The signature predicate for x outside S equals the intersection with the closed ball (as x is omitted), so nonempty distinct external traces are exactly the location-domination requirement. Independent exhaustive enumeration of all masks of sizes zero through seven found no codes below seven and exactly 220 seven-vertex codes. For each of these 220 states every possible 7*13 token exchange was tested and every accepted jump also used a host edge, establishing R_J=R_S, with 570 unoriented edges and degrees 120*4, 40*6, 60*7. Complete BFS from every state establishes one connected component radius8 diameter9. The package Python and C++ sources were inspected and their record Git tree reconstructed exactly. All work is an exhaustive finite proof, not an infinite extrapolation.

## originality

PASS

PASS best-of-knowledge. Exact equality of all 570 legal token-jump moves with slides on the minimum open-neighborhood locating-dominating sets of the dodecahedron was not found in searched records. General girth>=5 locating-domination work supplies size bounds but no enumerated optimal-state exchanges; generic reconfiguration papers distinguish moves but not this exceptional equality. Resultary results on dodecahedral minimum total-domination and disjunctive total-domination have different predicate and different mobility. Only current result matched exact counts. Unindexed dedicated dodecahedral code tables remain possible.

## value

PASS

PASS. The twenty-vertex dodecahedral graph is a canonical finite cubic host. The surprising equality of locally constrained token sliding and unrestricted token jumping on *all* 220 optimum locating-dominating placements, and the exact connected 570-edge metric, is a natural complete finite configuration-space classification relevant to sensor-placement mobility. It is not merely a small-instance test of a generic conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
