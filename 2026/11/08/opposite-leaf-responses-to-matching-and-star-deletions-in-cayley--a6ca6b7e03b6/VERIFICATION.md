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

Running `python check.py` using Python 3 and its standard library printed `VERIFY_OK 181 exact assertions`. Tests independently build the Laplacian from listed graph edges, compute spanning-tree cofactors by the fraction-free Bareiss algorithm, and derive expected leaves from the individual vertex-deleted cofactors. For small graphs, the checker also enumerates every edge set of the required size and tests whether it is a spanning tree. All equalities and inequalities are compared as exact rational numbers.

These tests cover bounded integer parameters only. The all-integer conclusions follow from the matrix-tree spectral argument, the leaf-extension bijection, Bernoulli inequality and strict Jensen inequality proved in `RESULT.md`. The checks do not establish literature uniqueness or independent audit status.
