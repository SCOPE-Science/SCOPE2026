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

An ordered full binary shape is determined by the binary addresses of its forks. Starting with no forks, adding a fork at every possible leaf and deduplicating enumerates every shape: every nontrivial finite full binary tree has a fork whose children are leaves. To model pruning independently, for each terminal address delete its parent fork and remove the next address bit from every fork in the surviving sibling subtree, leaving other fork addresses fixed. Recomputed all source and receiver sets and all shadow incidence rows through six internal vertices, agreeing exactly with certificates.json. Checked the disjoint codebooks and all nonnegative primal/dual inequalities with exact rationals. For each size both objectives match, hence weak duality certifies P. The floor of P at every size equals the supplied code size, so M=(1,1,2,3,7,15), P=(1,1,2,3,7,205/13). The first positive gap is 205/13−15=10/13, and integer rounding remains tight. Replay with python3 /workspace/branches/replay145.py (PRUNE lines), output /workspace/branches/replay145.txt.

## originality

PASS

The Catalan shapes, pruning operation in related models, and LP method are not new. The inspected results neither state nor specialize to the table for exactly this one-prune channel. The close analogy to labeled tree deletion has the same number of leaves at the threshold but a different receiver, feasible code and fractional objective.

## value

PASS

The property is a motivated first threshold for the natural coding problem of undoing one unknown prune in ordered binary shapes. The result distinguishes two practical questions: the continuous LP stops attaining the exact code capacity at six forks, but its rounded bound remains exact. Exact input/output certificates and a matching integral witness make this a sharp finite benchmark rather than a numerical or arbitrarily chosen slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
