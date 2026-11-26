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

For the matching's positive chords, each crossing forces their equality blocks together. Chord unions for distinct crossing components are disjoint connected sets in the disk; alternating endpoints would force two such sets to meet. Thus crossing-component endpoints, with the other endpoints singleton, give the finest noncrossing partition satisfying the positive queries. Joining different blocks at adjacent boundary vertices preserves noncrossing: their convex hulls joined by the boundary side form a connected set disjoint from the other block hulls, so no alternating endpoints are created. With t negative matching queries there are at least 2t boundary transitions if t>0, at most t forbidden; negative endpoints are singleton, so any other merger preserves every negative. With no negatives there is a parity switch exactly if the closure has more than one block. A shattered query graph is acyclic, and a spanning tree forces one block on all positives and two with one negative, ruling it out in either stratum. A boundary path of length n-2 uses no queries at the spare vertex, which can be joined along the boundary to switch parity. Narayana symmetry exchanges k and n+1-k at even n. An independently written recursive enumeration confirmed all matching counts at 4, 6, and 8 points and all 455 three-query supports at six points (371 even, 375 odd).

## originality

PASS

The closest unrestricted shattering result and the exact classical enumerations do not supply the parity-selective realization and obstruction. Bounded comparison supports the distinct parity-restricted classification, not priority for the connected-chord numbers or the Narayana formula.

## value

PASS

Block parity is a natural rank restriction, and perfect matching supports test each point exactly once. The theorem gives a uniform geometric obstruction and an exact missing-face count in that family, separating classes that have both the same VC dimension and the same total number of concepts. This is stronger than an isolated small-order contrast or a re-enumeration of chord diagrams.

The dated certificate retains the supplied scientific assessment, sources and limitations.
