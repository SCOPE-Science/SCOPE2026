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

# Reproducibility and verification limits

The exact matrix proof uses only the golden-ratio identity, the six written real vectors, the unit-modulus phase and normalized complex-sphere moment formula. `CHECK.py` runs with the Python 3 standard library and checks the six equiangular lines, unitary matrices and Hilbert–Schmidt Gram numerically. Numerical checks test the finite explicit certificate; they do not prove the exact equalities, which are derived in RESULT.md. The infinite-continuum sup-norm lower bound is proved using the Takagi factorization. No independent audit has been performed.
