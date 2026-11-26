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

For an independent support S, a wrong-parity positive trace Y can be realized iff at least one vertex outside S can join Y, since any realization must contain such a vertex and just one corrects parity. The maximal wrong-parity traces are S itself or the single deletions from S, according to parity. Removing a vertex from a maximum independent set gives a universal corrector and the lower VC bound; at maximum size the only allowed correctors for single deletions must be external private neighbors. On odd paths the unique maximum set has no such neighbors. On even P_(2k), k private witnesses would exhaust the complement and rule out every 101 pattern, requiring n>=3k-2, impossible for k>=3. The cases n=1,2,4 agree with the listed explicit trace families. Online, a depth-alpha complete tree would have a maximum independent set along the all-positive branch, so it requires matching parity. On odd paths of order at least three, flipping the last answer would require a corrector adjacent to at most the last queried vertex of that unique maximum set; every external vertex is adjacent to two, so the leaf is impossible. Endpoint querying on P_n gives P_(n-1) with the same parity and P_(n-2) with opposite parity; the base cases and the four residue classes attain the corresponding upper bounds. Independently checked direct graph traces on all 1099 labeled graphs of orders 1–5 and solved exact finite path VC and complete-tree existence for both parities through n=12 (python3 /workspace/checks/finite_review.py 4; /workspace/checks/4.txt). This finite verification corroborates rather than proves the graph and path theorems; no general-graph online formula is asserted.

## originality

PASS

Fixed-weight, maximal-independent, and independent-dominating path theorems handle materially different hypothesis families. The private-neighbor terminology is standard; what is distinct in the available evidence is its exact equivalence to shattering maximum supports for parity-restricted independent sets, the full support criterion, and the all-length period-four online dimension. This is not a priority certification and the inaccessible comparisons are retained explicitly.

## value

PASS

Parity is a natural global restriction on the independent-set language. The trace criterion converts shattering into an explicit graph property, with a sharp one-unit VC dichotomy. The exact path ranks separate adaptive from static querying in an infinite family and show the parity of the advantage alternating modulo four; a rank for a single weight or a mere cardinality estimate would not reveal this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
