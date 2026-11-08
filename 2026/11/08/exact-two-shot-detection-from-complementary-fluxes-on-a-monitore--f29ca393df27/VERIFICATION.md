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

Run `python verify_twoflux.py` with Python 3, NumPy, SymPy and SciPy. The checker defines the two independent \(3\times3\) quantum Hamiltonians in the site basis, forms the projective failure products, and compares against the exact two-dimensional projector reduction. It checks the exact optimal trace, determinant, characteristic polynomial, singular spectrum and global monotonicity identity symbolically; it also tests 1,071 finite numerical instances including nonrevival intervals, revival endpoints, fixed-flux dark survival, and iterated-cycle contractions.

Observed output: `PASS: exact symbolic identities and 1071 independent finite checks`.

The theorem's universal statements are proved in `RESULT.md`. These finite tests do not establish an infinite-dimensional claim, certify every sampling time numerically or constitute external independent validation. No independent audit has been performed.
