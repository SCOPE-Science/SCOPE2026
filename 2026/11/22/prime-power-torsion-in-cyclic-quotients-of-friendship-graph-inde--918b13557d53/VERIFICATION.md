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

# Verification

The stated face counts and rotation fixed-subgroup arithmetic were checked by running the included standalone `checker.py` from the extracted package. Exact finite checks cover all rotation powers for orders 4 through 50 and full petal-face counts for orders 4 through 8. The final output is `PASS: all exact tests`.

The infinite proof uses the exact combinatorial identification of the independence complex with a cross-polytope boundary plus an isolated point, invariant-subspace counting for each group element, Armstrong's published orbit-fundamental-group theorem, and the elementary suspension homology isomorphism. Their hypotheses are checked explicitly in RESULT.md. The prime-order specialization also uses the classical cellular homology of lens spaces. Numerical experiments alone do not prove these infinite statements.

No independent mathematical validation has been performed. The statement concerns the actual geometric orbit space, not a naive vertex-orbit simplicial complex.
