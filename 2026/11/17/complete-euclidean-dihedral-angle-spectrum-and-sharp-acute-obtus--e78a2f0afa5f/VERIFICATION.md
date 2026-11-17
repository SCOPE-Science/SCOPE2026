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

# Reproduction and mathematical limits

The exact formula is proved in `RESULT.md`. To corroborate it computationally, install SymPy and execute:

```bash
python verification/check_angles.py
```

The checked program was executed on the embedded source content and printed:

```text
CYCLE_LAPLACIAN_DIHEDRAL_PASS exact_n=3..11 facet_pairs=219 direct_normals=yes large_n=50,101,300,1000
```

It computes the cycle Laplacian for each order three through eleven, independently inverts its regularized rational Laplacian to obtain the pseudoinverse, and compares every normal Gram entry to the formula. It separately reconstructs facet normals directly from all supporting vertex equations and checks the finite angle-sign classification and multiplicities. Large orders check only integer sign counts and their agreement with the asymptotic fraction. Neither finite enumeration nor numerical approximation is an infinite proof. The self-contained analytic proof derives the cycle Green kernels from their difference equations, treats the cyclic boundary, and uses exact finite sums and weak-convergence arguments. Its scope is unweighted simple cycles in the standard ambient Euclidean metric; it does not include weighted cycles or general graphs.
