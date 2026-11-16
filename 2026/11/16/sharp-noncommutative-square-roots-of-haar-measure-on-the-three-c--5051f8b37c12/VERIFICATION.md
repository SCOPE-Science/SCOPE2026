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

The analytical proof uses the three-character Fourier inversion on \(C_3\) and the rank-one normal form of a square-zero complex \(2\times2\) matrix. It checks the exact atom eigenvalues, sharp commutator norm, trace-norm deviation, and both minimality obstructions. The included `check.py` confirms the three cyclic convolution identities, three characteristic determinants, and three commutator-square identities using SymPy symbolic simplification.

Run `python check.py` with a current SymPy installation. Observed output: `CHECK_OK symbolic_convolution=3 positivity_determinants=3 commutator_squares=3`. Symbolic identities supplement, not replace, the unitary classification argument. No independent validation or external certification was performed. The conclusion does not extend to an arbitrary finite group or a continuous convolution semigroup.
