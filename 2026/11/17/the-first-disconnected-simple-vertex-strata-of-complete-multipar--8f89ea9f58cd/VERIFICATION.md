---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact finite verification

The bundled `verify_multipartite_simple_connectivity.py` independently constructs and checks the complete finite census stated in RESULT.md. Invoke `python3 verify_multipartite_simple_connectivity.py` with Python 3 and the standard library; no floating-point computation, random choices, network requests or external packages are used.

The checker enumerates all 25 integer partitions with at least three parts through order seven; for each, all permutations of its labeled vertices are converted to acyclic orientation masks. It computes exact one-edge-reversal degrees of every mask, restricts to degree \(n-1\), and performs exhaustive component traversal. Its two exceptional component lists must match the exact assertions. Separate source-removal enumerators verify the acyclic-mask sets for \(K_{3,3,1}\), \(K_{3,2,2}\), and \(K_{2,2,2}\) without using a topological-order generator. A singled-out isolated orientation has its full six valid flips checked.

Observed passing sentinel:

`MULTIPARTITE_SIMPLE_STRATUM_PASS profiles=25 independent_direct_DAGs=3 exceptional_types=2 component_counts=(2,49) isolated_witness=1`

The finite certificate applies to graph order at most seven only. The independent primary-literature comparison is not a mathematical certification of historical priority, and no external audit is implied by the program's success.
