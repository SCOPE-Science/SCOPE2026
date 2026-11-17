---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

A linear binary order-five universal partial word has 32 distinct binary targets, one per window. For length L, 5<=L<=36; fixing exactly two wildcard positions a<b determines window cardinalities 2^{c_s}, whose necessary sum is 32. The actual C++ enumerator visits every L and wildcard pair, assigns all other bits recursively, and prunes only when a newly completed window-mask intersects previously covered masks; such duplication is irrevocable. At a terminal branch, 32 disjoint matches force all 32 targets exactly once. A separately compiled, reviewed rolling-state C++ implementation traversed 31,600,915 nodes and independently reproduced precisely 1328 words and per-length counts 26:8, 27:32, 28:32, 29:136, 30:352, 33:768, zero otherwise. Reversal and bit complement preserve the list and yield 332 orbits of four; source verifier analyzes all accepted strings. The finite search is exhaustive because the domain L<=36 and all assignments are covered, not a sample.

## originality

PASS

Chen–Kitaev–Mütze–Sun introduce universal partial words and exhibit binary order-five two-wildcard examples but their investigated theorems and example table do not enumerate every linear two-wildcard word, its length spectrum, or its 332 symmetry classes. The published 2026 order-four complete census concerns a different order, and the one-wildcard results do not imply this two-wildcard census. Qualified best-of-knowledge originality.

## value

PASS

The first genuinely nontrivial length-two-wildcard small-order complete linear u-word census is a natural finite combinatorial classification, including exact attainable-length spectrum and symmetry orbits. It improves example-only literature with a complete reproducible count. Finite scope does not make a mathematically motivated exact invariant trivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
