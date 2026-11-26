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

The original theorem and census are correct. Ordered neighbourhood assignments determine complete types by homogeneity and are realizable by the finite extension property; the adjacency channel is precisely disjoint pairs. An original replay (`python3 /workspace/independent_replay.py graph`) starts from triangle-free augmented graphs and deletes each possible marked edge. It counts extensions by three and four membership labels instead of the frozen subset-zeta procedure. For orders 1–5 it yields (decrease,tie,increase) = (0,0,0),(0,0,1),(0,0,9),(0,0,96),(80,0,1330), with two groups of 20 and 60. For the repaired connected-only result I also checked exhaustion structurally: the admissible endpoints have distance at least three, and the connected trees and possible 4- or 5-cycles give precisely the five rows in the repaired table. All five odds increase by exact cross multiplication. On six vertices insertion 03 into the given tree creates a 4-cycle, not a triangle. The hub/midpoint count and independently enumerated diagrams give 249 adjacent and 529 nonadjacent types before, 225 adjacent and 484 nonadjacent after, with exact drop 1491/551602. There is no claimed six-vertex census.

## originality

PASS

The original headline five-vertex claim fails the distinctness check: SCOPE-20261122-ceda5b31c1f9 states the same invariant, minimal order, exact two classes and counts. Same-day dates do not establish priority. The files under repairs/2 instead state only the sharp connected-base threshold and a six-vertex witness, credited against the companion theorem and proved by a small connected-only classification. This is a substantive narrowing; neither the matching same-day record nor the inspected general or analogous results gives the connected threshold.

## value

PASS

Connectedness tests whether the first drop can be attributed only to connecting previously disconnected components. The result shows that the change of normalization can reverse the sign even with a connected initial base, at the exact first order where it can do so. Neither isolate padding nor another count of the five-vertex classes answers that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
