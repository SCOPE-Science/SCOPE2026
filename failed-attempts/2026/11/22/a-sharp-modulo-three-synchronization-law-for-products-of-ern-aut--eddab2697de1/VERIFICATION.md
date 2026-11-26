---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With the frozen shared alphabet and reading order, the image of the full product is the product of the two factor images. In C_n any letter a and any effective b advance a trajectory by one modulo n. If a word resets, initial state i has effective-b count h_i congruent to the common final state minus i minus the number of a's. These residues are distinct; some trajectory uses at least n-1 effective b's, with at least n-1 a's between every pair. The length is at least (n-1)^2, and equality forces that trajectory to use every b with exactly n-1 a's in each gap and none outside, yielding only W_n. Starting from the full state set, b followed by j blocks of a^(n-1)b yields the interval [0,n-j-2] on C_n. W_n resets C_n; the common prefix of V_n leaves {0,1} on C_n and its suffix a^(n-3) b a^2 b maps it via {n-3,n-2} and {n-1,0} to {0}. On C_3 the block a^(n-1)b collapses the initial pair {0,1} iff n is a multiple of 3 and otherwise leaves the pair invariant. For n=1 mod 3 the inserted suffix first preserves that pair then merges it by its final a^2 b; for n=2 mod 3 the suffix starts with a^2 b and merges immediately. This includes n=4 with one prefix block and proves both sharp bounds. Independent inverse-image breadth-first search from all singleton targets on the Cartesian product gave 10, 17, 25, 37, 50 for n=4 through 8; not the basis of the unbounded proof. The frozen comparison cites Proposition 3.4 for arXiv v1, but the corresponding statement in the inspected v1 PDF is Proposition 7 (p. 5); this is a locator error, not an error in the theorem.

## originality

FAIL

Distinct record 7df3c0143ebf contains the identical all-length threshold, explicitly includes the frozen witnesses as shortest words, and additionally covers n=3 and classifies and counts all shortest common words. The state numbering is a cyclic conjugacy that does not change any word. This is conclusive statement-level coverage. Shared calendar dating does not establish publication ordering or priority.

## value

FAIL

The fixed-three exact latency is naturally motivated, but this frozen result repeats the exact invariant and supplies a witness already indexed in the complete classification. No new bound, invariant, useful extension or distinct surviving common-reset claim is identified. A different elementary derivation of the standard single-factor lower bound does not change that conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
