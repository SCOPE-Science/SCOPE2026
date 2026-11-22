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

The standalone script `verify_chiral_probe.py` requires Python 3, SymPy, NumPy and SciPy; invoke `python verify_chiral_probe.py` in a directory containing that file. It checks the Hermitian matrices and spectral cubic identity, the target amplitude, the Laplace-transform rational probability, the sharp square-factor identity for two positive forward optima, and the exact reverse derivative with its unique positive optimum. It independently computes 14 exponential-duration probabilities from direct numerical integration of 3-by-3 unitary matrix exponentials (seven rates and both circulations), then tests strict positivity and global upper bounds on 150 sampled positive rates per orientation. The recorded output was `PASS: exact symbolic identities and 614 direct numerical assertions;`.

The universal proof is algebraic, using the displayed sum-of-squares factorization and positive-quartic derivative. Numerical integration error tolerances do not certify untested rates. Both rates use the same ideal re-preparation protocol; matrix conjugation models flux reversal. External publication priority and experimental feasibility have not been independently validated.
