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

The proof's analytical requirements are the regenerative stationary representation, locally uniform limit, hypoexponential partial-fraction formula, termwise Mellin transform and nonzero Fourier coefficients. These are supplied in RESULT.md.

A separate `VERIFY.py` checks finite hypoexponential mixtures against Laplace transforms, the exact infinite-mixture survival formula against limiting sums, the phase scaling identity, and approach to the stated probability asymptotic. It also verifies the explicit first-harmonic gamma factor is nonzero. Tests use 50-digit arithmetic and are not substitutes for the limiting arguments or a claim of independent validation.

Reproduce with `python VERIFY.py` (Python 3, `mpmath`).
