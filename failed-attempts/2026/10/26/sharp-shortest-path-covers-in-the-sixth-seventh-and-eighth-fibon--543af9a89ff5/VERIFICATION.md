---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Removing bits not in the target and then adding target bits gives an isometric embedding into the hypercube, so a geodesic uses each coordinate at most once. Each extreme-coordinate edge class has F_n edges (count valid words of length n−2 after fixing the neighboring bit to zero). One class gives the cover lower bound, and their disjoint union is in edge general position. An independent exact replay on the assigned geodesics.json (lines 1–402), using fresh inline Python rather than the supplied verifier, regenerated 21/34/55 vertices and 38/71/130 edges, checked the 8/13/21 paths for valid distinct vertices, unit steps and BFS shortestness, and reproduced the entire edge union in each graph. A set in edge general position uses at most two edges in each covering path, giving the matching upper bounds 16/26/42. The recorded package checks were inspected separately; neither the proof nor the replay covers n>8.

## originality

FAIL

A distinct indexed Resultary record states and proves both equalities for exactly the same three dimensions. It has different path lists, but there is no claim about a new property of the paths. This is exact mathematical coverage, not an inference about authorship from catalogue dates.

## value

FAIL

These dimensions would be a motivated finite extension of the conjecture and the covers would give useful exact invariants if missing. The very same finite extension and exact cover values are already established in the indexed result. No additional structure or useful property of the alternative certificates is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
