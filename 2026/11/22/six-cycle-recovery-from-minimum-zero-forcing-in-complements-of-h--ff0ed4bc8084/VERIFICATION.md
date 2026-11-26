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

With four white vertices a first force can leave only three whites in one H-neighborhood; by the absence of quadrilaterals no other black vertex sees two of those in H, so forcing stops. Monotonicity rules out larger white sets. With three whites a legal first force is exactly an external vertex with two H-neighbors in the triple. After that force a second H-neighbor of one of those two whites distinguishes them (there is no quadrilateral), and the final white can be forced because H has no universal vertex. The same triangle/quadrilateral reasoning supplies a distinguishing vertex when starting with two whites. Existence of a successful triple follows by taking two H-neighbors of any v and one G-neighbor of v. For the distance-two graph J, each J-edge has a unique H-midpoint. Its triangles either have one common midpoint or three distinct midpoints outside the triangle, with the latter corresponding bijectively to six-cycles with a choice of alternating triple. Inclusion-exclusion gives (n-2)A-B+t(J) triples containing a J-edge. The nonforcing ones are exactly the H two-edge paths (midpoint white) and triples in a common H-neighborhood (external midpoint sees all three), counted by A and the sum of binom(d,3), respectively. This yields the stated coefficient and recovery identity, including disconnected H. The supplied Python/C++ files and recorded output were inspected as finite corroboration only. A separate memoized search through possible force sequences checked every white mask on every eligible labeled graph of orders 1–6 and on the disjoint and bridged C5/C6 examples: 12 C5 labelings with (c6,M)=(0,5), 60 C6 labelings with (1,14), and (1,79),(1,93) in the 11-vertex examples. Replay: /workspace/branches/zero_forcing_replay.py. The general result rests on the proof, not those tests.

## originality

PASS

Best of knowledge, the distinct contribution is the optimizer criterion and exact six-cycle-sensitive count across the full minimum-degree-two, girth-at-least-five family, including irregular graphs and disconnected underlying graphs. The scalar n−3 upper bound under complementary connectedness and the complete cycle special case, including the witness criterion there, are credited as prior coverage.

## value

PASS

This is an all-orders structural and enumerative theorem for a natural complement family. The zero-forcing number alone is constant at n−3 for fixed order, but optimizers encode a definite six-cycle invariant after removing computable local terms. In particular equally sized cubic complements can have identical scalar numbers and distinct optimizer counts explained exactly by their underlying hexagons. The result provides both a usable membership test and the complete set polynomial, not just a new instance of a scalar bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
