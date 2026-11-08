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

# Verification and reproducibility

Run `python3 verify.py` from the directory containing this file. The checker uses only the Python standard library and rational arithmetic, with a fixed seed for the finite random probes.

Observed output:

`VERIFY_OK universal_exact_rayleigh_checks= 9681 balanced_multipartite_exact_matrices= 36 unbalanced_bipartite_necessary_condition_checks= 156`

The checker independently builds all connected noncomplete labeled core graphs on three, four and five vertices and probes three heterogeneous stochastic kernels for each graph; for each nonadjacent core pair it evaluates the exact Rayleigh quotient. It constructs the full corona transition matrix for every \(2\le r,m\le7\), checks nonnegativity, stochasticity and symmetry, reconstructs the three exact spectral blocks, and checks the necessary positive-semidefinite inequalities at \(\pm4/5\). It also checks algebraic incompatibility of the forced balanced weights for unequal complete-bipartite side sizes from two to fourteen.

The theorem for arbitrary core size, arbitrary feasible transition matrices and all multipartite parameters is proved in `RESULT.md`; exhaustive finite testing does not establish these universally quantified claims. Independent external validation has not been performed.
