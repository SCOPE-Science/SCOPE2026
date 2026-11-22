---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the 24-square legal rook complex with row caps (1,2,2,2) and six unit columns. Independent column-state and row-combinations enumerations gave 6309 nonempty faces, f=(24,225,1020,2250,2160,630). The stated 24-vertex toggle order gives 3105 disjoint Morse pairs, 27090 cover arrows, a complete acyclic topological sort, and exactly one critical 0-cell plus 98 critical 4-cells. This yields the integral wedge of 98 S4 directly, not merely mod-two Betti. Sum of capacities seven ensures every <6-rook face can be extended, so purity in dimension five and non-shellability are correctly qualified. No torsion.

## originality

PASS

Full text of Limonchenko–Yu 2026-10-27 was inspected, including Theorems 1.2, 1.3, 5.5 and boundary examples. Its four-row family (2,2,2,m-5) assumes m>=7, so the m=6 point (1,2,2,2) is genuinely excluded and its torsion hypotheses do not directly apply. Resultary other four-row capacity cases (1,1,1,2), all-two rows, and 7-column rows are different. Reiner–Roberts homology/syzygies and general connectivity cannot imply this precise integral wedge. Limited risk of implicit unindexed table.

## value

PASS

At the natural six-column endpoint of a recently studied torsion family, the integral homotopy type and torsion-freeness are natural missing boundary data; nonshellability despite wedge below top dimension distinguishes behavior. A complete finite classification of the first excluded width has independent mathematical significance without needing a downstream general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
