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

# Reproducibility and proof limits

Run `python checker.py` after installing the versions of NumPy and SciPy specified in `requirements.txt`. The checker constructs principal triangular matrices, tests the exact inverse bidiagonal and tridiagonal Gram identities, compares independent SVD and tridiagonal eigensolutions, checks the proposed elliptic coefficient at three parameters, and checks the finite cutoff of the Hilbert–Schmidt identity. The completed checker passed 80 numerical assertions. Finite sections are corroboration only. The complete infinite singular-value asymptotic and its stated remainder follow from the block-counting and tail proof in `RESULT.md`; no independent audit is represented.
