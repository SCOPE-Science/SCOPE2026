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

# Reproducible verification

Run `python check.py` using Python 3 and its standard library. The program evaluates modified Bessel Fourier coefficients by their positive convergent power series, checks the exact one-step circular semicircle kernel integral against the Fourier expression, verifies strict submultiplicativity for selected positive parameters, and checks the leading spectral asymptotic for increasing iteration counts. These tests corroborate numerical normalization and do not replace the analytic all-concentrations and all-iterations proof in RESULT.md. The verification covers no independent audit.
