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

Checked the full all-parameter proof directly. Two distinct ball centers at distance 1 have intersection their common coordinate line; at distance 2 the intersection is the two intermediate corners, and otherwise empty. A noncollinear triple in a ball therefore fixes its center. This excludes a full-minus-one trace on a noncollinear four-set in a ball, while a collinear four-set cannot have a two-point trace. For triples normalized at their center, the three noncollinear types are center plus two arms, three arms, and a double arm plus one other arm. In d≥3 the center-plus-two type uses a fresh coordinate to isolate the center and form the empty trace; for three arms the singletons are their tips, pairs use the two specified changes and the empty trace uses all three changes. For the double-arm type a fresh-coordinate change gives the empty trace, and adding it to each double-arm tip isolates that tip; the other tip isolates itself, the pair on the common arm is seen from one tip on that arm, and mixed pairs use the union of their two changes. For d=2 the center-plus-two type cannot isolate the center. For the double-arm type a center must avoid three first-coordinate symbols and two second-coordinate symbols to realize the empty trace; with q≥4 the same pair witnesses and a spare second-coordinate letter give the other traces. Unique-center counting gives the two cubic formulas. Pairs at distance at most two admit full and singleton traces; a spare coordinate or third symbol supplies the empty trace except in H(2,2), where every ball misses one point. In d=1 every ball is full; in higher dimensions each point can be missed. These are exact combinatorial arguments, not extrapolations from the original 13-case self-check.

## originality

FAIL

A distinct indexed finding, 6c82fc864f93, gives the identical polynomial for the same closed radius-one system and all q,d, including the low-parameter cases, unique-center classification and three geometric triple types. This is demonstrable equivalent coverage, not a priority judgment. Its catalogue date is later than the frozen record's date; the evidence does not establish that it predates the frozen result, determine priority or imply copying. No residual mathematical claim in the Finding was identified that is distinct from the compared exact coverage.

## value

PASS

As mathematics, the natural all-parameter census shows exactly how the low-dimensional cases differ and supplies geometric data that a dimension bound does not. The unique-center criterion is useful for counting and recognizing shattered subsets in the canonical closed Hamming system. This evaluates the substance of the theorem; it does not make the equivalent record a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
