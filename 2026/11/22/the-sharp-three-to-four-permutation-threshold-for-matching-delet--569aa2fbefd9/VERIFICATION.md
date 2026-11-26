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

Each boundary contributes one defect precisely when the pair order changes. With three blocks the two changes that characterize nonedges become agreement in all three orders after reversing the first and third. The intersection is a poset, and applying the same reversal to a three-order realizer is the converse. In the family complement, the middle of three matched A vertices in any transitive clique order can neither point to nor receive an arrow from its match: one choice forces an edge to the earlier vertex, the other to the later one. For s=0,1,2 the proposed two orders agree within each shore and exactly on the deleted cross pairs. In particular at s=2 the common shore orders are a1,A′,a2 and b2,B′,b1, and the only cross agreements are a1 before b1 and b2 before a2, including when either primed sequence is empty. In the published four-block word, within-shore pairs switch twice; for a cross pair the first two orders agree and the last two differ only at a deleted match, where there are exactly two switches. The indicated restriction keeps exactly the required matching of cross nonedges and preserves all pair defects. At most two blocks always give a complete graph, so only K2 needs one block.

## originality

PASS

The three-block threshold-rule characterization and sharp non-comparability obstruction after three matching deletions are distinct on inspected evidence. The four-block crown construction, general permutational existence, and ordinary comparability/realizer correspondence are not claimed as new.

## value

PASS

The complement/realizer correspondence gives a structural test at exactly the shortest potentially noncomplete block count. Applied to a natural deletion family, it identifies the obstruction already present on three matched pairs and makes the known crown construction sharp, rather than just transcribing it. The answer holds for arbitrary shore sizes and not just the balanced crown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
