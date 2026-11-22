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

# Reproducible integral checks

Run `python3 verify.py` with standard Python 3, without third-party dependencies. The verifier constructs the 56 exceptional Picard classes, verifies all 1540 pairwise products, forms the weighted Laplacian, checks the Geiser involution on every vertex and verifies commutation of its vertex permutation with the Laplacian.

For each of four different deleted root vertices, it computes the reduced 55-by-55 determinant by exact fraction-free Bareiss elimination. It also computes the base critical group by Smith operations modulo \(2^{115}\), \(5^8\), and \(7^{48}\). For each root and both signs, the code constructs the 55-by-110 presentation \([M\mid T-\epsilon I]\) and performs twelve exact prime-local rectangular Smith calculations per sign across the four roots. Precisions exceed all corresponding exponents in the base determinant, so no nontrivial invariant factor can disappear as a modulus-zero pivot.

The displayed subgroups follow from the canonical perfect monodromy pairing on the graph Jacobian, together with the fact that the Geiser action is an involutive graph isometry. The verifier confirms the Smith data but does not formally certify the standard duality theorem or demonstrate a specific geometric semistable smoothing. No independent external audit has been performed.
