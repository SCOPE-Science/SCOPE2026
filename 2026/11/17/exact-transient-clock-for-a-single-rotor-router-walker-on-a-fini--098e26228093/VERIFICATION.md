---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Read complete fixed-tree RESULT.md and both separately named functional-graph/direct simulation scripts in actual Git tree. The conserved offset p-k mod n reduces full rotor states to binary words updated by flipping bit indexed by popcount mod n. Explicit recurrent words A_j and B_j form a 2n orbit; monotone displacement potentials E_B, E_A count the upward/downward flips until entry, proving the statewise exact preperiod. Rearrangement proves maximal preperiod and exactly two optimizing words in each offset class; the rightmost-one tail sum and symmetry prove the mean. Independently enumerated all binary words n=3..10, computed true recurrence-entry from the complete functional graph and verified the formula, max count, recurrent count and exact mean. Finite census supports but does not replace the all-n argument.

## originality

PASS

Best-of-knowledge PASS for the exact labelled single-walker cycle preperiod function, sharp population and uniform expectation. Priezzhev et al and Holroyd et al establish eventual Eulerian recurrence and unicycle structure but no exact statewise first-periodic-entry clock; Pham gives orbit sizes, not transient depth. Resultary returned related paths/spiders and same cycle work, no broader prior covering ring statewise clock. Inaccessible original Yanovski network-patrolling literature remains a real priority risk.

## value

PASS

PASS: Statewise recurrence-entry time, extremal population and exact expected transient clock of the canonical rotor walk answer natural dynamical questions distinct from cover time and Euler-tour period; exact full-state statistics can be used independently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
