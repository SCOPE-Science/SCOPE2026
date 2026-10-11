---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Metric distance and adjacency are automorphism invariants, so distinct listed classes cannot merge. Conversely, two ordered off-diagonal pairs with the same distance and adjacency bit induce isomorphic two-point metric-graph substructures; strict homogeneity extends that two-point isomorphism to a global automorphism. The finite-extension property realizes both adjacency choices at every canonical distance level. Singleton homogeneity gives one diagonal orbit. These steps prove exhaustiveness and nonemptiness directly from the primary construction.

## originality

FAIL

The claimed orbital decomposition is an immediate implication of the defining strict-homogeneity theorem and extension property in Kubiś--Pech--Pech. In any homogeneous relational metric structure, two tuples lie in the same automorphism orbit precisely when the induced finite substructures have the same quantifier-free finite type. For ordered pairs here that type is exactly equality, distance level, and the graph bit. The fact that the source does not print this low-arity list verbatim does not make the corollary original under the audit rule.

## value

FAIL

The pair-orbit decomposition is a routine first exercise once strict homogeneity of the exact relational metric structure is known: identify the two-point finite type and invoke extension. It adds no new structural lemma, boundary, difficult invariant, or motivated classification beyond spelling out the immediate low-arity consequence. Under the shared value standard this is useful exposition but not a separate worthwhile mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
