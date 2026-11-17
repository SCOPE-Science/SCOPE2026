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

The known Chee–Etzion–Nguyen–Ta–Tran–Vu maximum/support theorem fixes exactly the cyclically no-11 n-words as Eulerian overlap edges, for all n>=2. Vertices beginning/ending 0 have indegree=outdegree=2; every other vertex has degree one with forced zero continuation. Every forced corridor reaches a branch, and contraction establishes a bijection on root-directed arborescences with parallel arcs kept distinct. Directed BEST has factorial product 1, so the root cofactor of (2I-A_n) is the complete rotation-class count. Independently constructed full-graph Laplacians at n=2..8 gave C_n=1,1,1,2,2,28,216 and 216 for n=8 (the sequence for n=2..8 is 1,1,1,2,2,28,216); none is an infinite proof. Numerical census beyond n=8 was inspected as source evidence, not independently rerun.

## originality

PASS

The maximum length L_n and uniquely determined cyclic support are prior results, and the matrix-tree and BEST ingredients are standard. The submitted all-order compressed-tree cofactor counts ALL optimal cycles rather than the lengths, the number of necklaces or a method constructing a subset; the directly relevant 2024 primary paper Section 4 was inspected and counts necklace/word populations and lengths, not all Euler circuits. No dominating full-tour enumeration was established by the actual Resultary search or inspected primary text. Historical priority of an unindexed exact census remains a genuine risk.

## value

PASS

The complete multiplicity of maximum run-constrained de Bruijn cycles is a natural exact combinatorial invariant for universal-cycle enumeration and constrained coding. The forced-corridor reduction from F_(n+1)-1 vertices to F_(n-1)-1 supplies a nontrivial structural formula and computable counts, beyond a routine redefinition of known maximal length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
