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

Run `python verify.py` with SymPy, NumPy, and SciPy. The script constructs the *actual* mass-action equations, checks the equilibrium, limiting characteristic polynomial and exact fast Schur identity, derives the first-order coefficient for arbitrary positive fast-rate ratios, isolates the relevant Hopf polynomial root, and compares six finite-rate eigenvalue calculations. Its success marker begins `VERIFY_OK`. Symbolic identities and the proof, not finite numerical eigenvalue samples, support the universal conclusion. Scientific priority and all infinite-parameter claims have not been independently audited.
