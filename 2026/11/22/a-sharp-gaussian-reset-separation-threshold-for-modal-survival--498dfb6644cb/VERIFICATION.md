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

The accompanying `checker.py` is a standalone numerical reproducibility program using Python, SciPy and SymPy. Execute `python checker.py` in the same directory as the result. The program passed 213 deterministic checks, including a direct renewal-age integral distinct from the closed normal-Laplace formula, an independent positive Gaussian variance-mixture integral for curvature, Fourier-resolvent identities, sample sign changes, peak splitting and endpoint limits.

The mathematical proof of uniqueness of the inflection point uses a strictly increasing positive Gaussian-mixture likelihood ratio. The global mode count uses an explicit sign-change bound for the Gaussian convolution of a two-Laplace-mixture derivative. Limits and all-parameter assertions are proved analytically; numerical computations are finite diagnostics only. No independent scientific audit or experimental validation was performed.
