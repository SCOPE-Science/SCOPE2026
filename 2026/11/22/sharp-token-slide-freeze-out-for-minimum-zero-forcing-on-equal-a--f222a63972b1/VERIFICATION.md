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

With at most two blue vertices, a first force needs an adjacent pair including a degree-two internal vertex. All such starts remain within a single arm plus its ends, with two white choices at each terminal. For triples with two terminals or all internal seeds on a single arm the same two-unused-arm obstruction applies. With exactly one terminal and seeds on different arms one seed must be its neighbor to start; completing that arm exposes the opposite terminal, after which the other seed can contribute precisely if it is an extreme internal vertex. With no terminal, a consecutive internal pair is necessary to start; the third seed must be on a second arm and extreme for the same terminal-exposure reason. These stalled configurations are closed supersets of the blue starts, so another force order cannot escape them. The successful cases fill one arm and then use a terminal with two blue adjacent arms to enter the third arm, completing the seeded arm from its end. The two classes give 18+12(ell-2) minima. For jumps, sliding a consecutive pair's window by replacing its trailing vertex (a jump, not a slide) joins interior sets to the terminal classes; carrying such a pair across the arm bridges the two types of terminal. For slides at ell>=4, an extreme seed moved inward ceases to be extreme, a pair loses adjacency or leaves a nonextreme seed after an outward terminal move, and a terminal moved to an occupied arm cannot make an adjacent pair of its extreme internal vertices. All other terminal exchanges or moves to unused arms violate the two classified classes. At ell=3 the unordered occupied-arm pair is preserved, and the listed cycle in each class has all ten states, each degree two. A separate bit-mask closure using one force at a time, pairwise symmetric-difference moves and BFS (`python -B /workspace/independent_replay.py 4`) corroborated the exact families and components for ell=3,4,5,8,13; in particular ell=3 has three 10-vertex degree-two components and ell=13 has 150 isolated slide states and one jump component. Frozen verification code was inspected only.

## originality

PASS

The supported distinct finding is the exhaustive ordinary optimal-set classification together with the jump connectivity and exact slide graph across subdivisions. Neither the number Z=3 alone nor the existence in other graphs of jump-connected but frozen minima is credited as novel.

## value

PASS

This biconnected subcubic family gives an explicit stability boundary under one subdivision of each arm: every slide edge disappears despite continued exchange connectivity. The full list of optimum seeds and exact small-length component structure make the obstruction testable and useful for comparing move rules, rather than merely producing another example with Z=3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
