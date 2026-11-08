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

The analytic proof derives the independent-binomial law, an explicit hypoexponential tail, finite exact-rational evaluations, and a fixed-bundle-size extreme-value asymptotic.

Run `python check_efx_survival.py` with SciPy installed. The checker computes the rational sum independently from the integral quadrature, verifies the two-good harmonic identity, and samples directly from the original agent–good valuation distribution. The included checks cover only stated finite cases; no finite computation proves the limit theorem. In particular, the comparison against numerical quadrature is separate from the direct-random-sampling comparison. The general statements require the full proof in `RESULT.md`.

Independent audit: not yet performed.
