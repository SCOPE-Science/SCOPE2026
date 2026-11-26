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

Independently used the three zero triples of Wolfram Rule 110, composed by literal synchronous updates, to construct labeled overlapping-input graphs. Every admissible output block comes from a path, and every such path specifies a finite predecessor block that extends bilaterally, so the language identity holds at all lengths. Determinizing from the full predecessor set and minimizing by inverse-transition splitting reproduces 7/41 nonempty reachable subsets and 5/20 accepting classes. The frozen transition tables and adjacency matrices agree under a state relabeling. Both accepted graphs are strongly connected and have a self-loop, so their Perron roots control the all-length deterministic transfer counts and spatial entropy. Recomputed characteristic polynomials are (x-1) times the frozen quartic and x^2(x-1) times the frozen P17. The A^60 1 integer inequalities, disjoint rational Perron brackets, and exact real-root counts reproduce, including one root in each interval and none above it. Independent full finite input-block enumeration through output length 12 gives equality through length 9 and precisely 0110110110 lost at length 10 (769 versus 768), consistent with Y2 contained in Y1. Replay: python3 /workspace/branches/ca_independent_replay.py 110. The submitted code was inspected without execution. This checks the full-shift synchronous spatial claim, not periodic-ring image counts, temporal entropy, or later images.

## originality

PASS

The bounded pass is for the evaluated Rule 110 second-image Perron polynomial, certified root, and quantitative first-to-second spatial entropy loss. The first-image quartic and the finite-loss threshold and witness are already covered and are not credited as new. No distinct source retrieved gives the main second-image invariant or implies it from a stronger stated result; inaccessible primary graph work leaves the specific risk recorded below.

## value

PASS

Rule 110 and finite-time spatial image entropy are established natural objects. Exact evaluation at time two resolves whether losing a block is accompanied by a strict exponential growth loss, which proper inclusion alone does not establish; it quantifies that loss with an algebraic root and exact all-length counts. The distinctive value is not the already tabulated detection of a first missing word or the conventional method of determinization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
