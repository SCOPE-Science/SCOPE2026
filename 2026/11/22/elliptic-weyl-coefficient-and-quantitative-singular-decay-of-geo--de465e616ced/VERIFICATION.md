---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and proof limits

`checker.py` uses NumPy and SciPy. It constructs finite triangular matrices, checks their inverse bidiagonal and tridiagonal Gram identities, compares SVD and tridiagonal eigensolutions, and runs finite tests concerning the leading elliptic coefficient and the Hilbert–Schmidt identity. The original verification record reports 80 numerical assertions. These checks do not establish the Fourier-mode decomposition for the infinite operator or validate the size or coefficient of the refined asymptotic. The infinite claims follow from the periodic form decomposition, the unitary Liouville change of variable, and the two-mode spectral estimate in `RESULT.md`.
