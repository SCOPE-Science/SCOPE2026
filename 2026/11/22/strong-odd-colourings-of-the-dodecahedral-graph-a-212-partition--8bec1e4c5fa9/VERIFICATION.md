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

Exact verification uses the complete twenty-vertex graph description in `RESULT.md` and two independently implemented, standalone integer enumerators. `verify_exact_cover.py` tests all \(2^{20}\) vertex masks and a least-uncovered-vertex exact-cover recursion; `verify_independent.cpp` generates independent sets recursively and performs a separate partition search. Both return odd-independent size counts \((1,20,100,120,90,0,10)\) for sizes zero through six, no four-partition, 212 five-partitions by profiles \((60,100,52)\), and two square-colouring partitions.

The lower bound is not inferred from failed optimisation attempts: all eligible colour classes are generated and all possible partitions are covered by the least-uncovered-vertex recurrence. A concrete five-colour certificate is in `RESULT.md`. Counts refer to unlabelled colour classes on fixed named vertices. The finite proof does not address any other generalized Petersen graph, and external independent mathematical validation has not been performed.

A third self-contained certificate, `verify_petersen.py`, enumerates all 1,024 vertex subsets of the ten-vertex Petersen quotient, verifies exactly ten singleton and ten triple odd-independent classes, and proves that six is its strong odd chromatic number with fifteen unordered optimum six-color partitions.
