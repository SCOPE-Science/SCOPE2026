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

# Reproducibility

Execute `python3 verify.py` with Python 3 and NumPy. The verified execution returned `PASS 2869 finite assertions`.

This includes independent enumeration of the hard-core rim law for cycle lengths 3–13, full weighted sunlet independent-set enumeration for cycle lengths 3–6, direct covariance eigenvalues, Fourier formulas, numerical maximization comparisons, and auxiliary stationary binary distributions. The checker uses actual formulas and an independently enumerated finite Gibbs measure, not a saved transcript.

All-dimensional validity rests on the self-contained transfer-matrix, Fourier-ordering, and semidefinite tangency proofs in RESULT.md. Finite computations do not certify that published literature lacks equivalent statements. Independent audit was not performed.
