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

# Computational verification

Run `python3 verify.py` with Python 3.9 or later. The script imports only the Python standard library and reconstructs every full-word edge in each tested graph from the claimed alphabet, length and weight. It does not rely on any downloaded paper, earlier research package, or solver output.

The test suite checks twelve parameter triples, builds individual support-necklace components, counts all vertices and edges, verifies indegree equals outdegree, and independently computes each directed Laplacian cofactor with exact integer Bareiss elimination. It then compares those cofactors with the closed formula, uses the actual graph degrees to evaluate the BEST count, and checks the global product and binary necklace count. On three small cases it also independently enumerates Euler circuits with one fixed edge to eliminate rotation equivalence.

The actual run finished with `ALL EXACT CHECKS PASSED`. Tested parameters include \(q=2,3,4\), \(n=3,4,5,6\) (and \(n=5\) for \(q=2\)), with weights \(2,3,4\) where applicable. The checks use true integer arithmetic. They cover only the printed finite cases; the infinite result rests on the proof in RESULT.md. Neither a numerical log nor a finite range certifies every parameter or historical originality.
