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

I independently decoded every code 0000–3f80 as a dyadic rational, including zero and all 127 positive subnormals, and evaluated both exact expression trees with one rounding at each specified node (only the root for A). A neighbor-midpoint comparator and an independently specified integer-quantum rounder agreed at every node and every adjacent midpoint of the relevant table. The denominator of B is always positive and every successor is in-domain. Indegree peeling followed by residual cycle walks and reverse BFS accounted for all 16,257 states of each map. The (period, basin size, maximum transient) triples were A: (1,2,1), (19,16255,74); B: (1,2,1), (2,409,53), (6,5958,64), (21,9888,63). Both fixed cycles were zero. Exactly 1,371 successors differ. The little-endian SHA-256 values were 61a5e82b755d2663346b81fce98adced48bacb0933638361e4e29635e8a25d71 and eb02e69879f027f218499d3e54f21b936d0619cf219b386b5ab312721c106d4b, respectively. Replay: python3 /workspace/independent_bfloat16.py. The frozen checker was inspected, not run. It compares final successor arrays rather than each actual intermediate node directly; the independent replay checks these nodes too. This exhausts only the defined finite systems, not the real map or optimizations used by a particular processor.

## originality

PASS

The supported distinction is the complete census for this rational map and the two exact evaluation trees, not the discovery that rounding changes low-precision dynamics. No inspected source covers that conjunction.

## value

PASS

A motivated parameter taken from a published chaotic real trajectory and two plausible evaluation trees give a reusable all-state benchmark, rather than a selected orbit. The substantial change from one to three nonzero attractors, with exact basin sizes and transient maxima, is information a researcher comparing precise low-precision evaluation semantics can use. It does not license claims about real chaos, unspecified hardware or cryptographic security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
