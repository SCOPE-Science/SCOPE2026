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

For host K4 square K4 (16 labeled vertices), a selected subset is a minimum identifying code iff each closed-neighborhood signature C∩N[v] is nonempty and the sixteen signatures are distinct; equivalently its mask hits all neighborhoods and pairwise symmetric differences. Code size monotonicity means checking no size-5 solution excludes all smaller sizes. Independently implemented a fresh exhaustive checker of all C(16,5)=4368 and C(16,6)=8008 subsets, obtaining 0 valid five-codes and exactly 2208 six-codes. Constructed all legal host-adjacent one-token slides and found 14976 undirected edges, exactly 1344 states of slide degree12 and 864 of degree16. Full BFS from each of 2208 states reached all other states with eccentricity exactly 6, proving radius and diameter6. Full code enumeration is a complete fixed-finite proof rather than extrapolation; two supplied independent Python/C++ algorithms separately encode signature criteria and transition generation.

## originality

PASS

PASS best-of-knowledge for the NEW adjacency-restricted slide graph on the fixed rook graph, not for min code size 6, code count 2208, unrestricted jump 28800 edges/diameter6, or frozen Shrikhande slides. The full 2026-10-26 prior result gives these excluded jump invariants but not which jumps exchange adjacent host vertices. Deleting 13824 edges may disconnect graph or increase distances; prior jump diameter supplies only a lower bound for slide diameter, not six-step upper bound. Mynhardt–Teshima defines this slide reconfiguration model abstractly and proves realizability on constructed graphs, not the given host’s slide spectrum. Foucaud et al determine optimum code size for line graph K4,4 but not exact slide mobility. No covering same-host slide invariant found; unindexed tables remain a residual risk.

## value

PASS

An exact finite, natural sensor-reconfiguration graph shows that imposing local adjacency deletes almost half the legal unrestricted jumps yet preserves connectivity and worst-case shortest distance. Complete vertex degrees, edge count and all-state metric provide a genuinely useful structural classification, even though the host is a motivated 16-vertex example rather than an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
