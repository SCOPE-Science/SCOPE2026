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

# Reproduction and mathematical limits

Execute `python verify.py` in a Python environment with `sympy>=1.13`. The exact check returns `MACLANE_CHAR3_INTEGRAL_SYZYGY_HILBERT_VERIFIED_OK`. It checks displayed syzygies by symbolic polynomial reduction modulo three, independence modulo quadratic multiples, exact Gröbner leading monomials, lcm inclusion–exclusion, the one-degree Hilbert difference, and all labeled triple determinant norms in the integral quadratic model.

The displayed primitive degree-six relation and fraction-field rank-two condition prove the proposed syzygy presentation has precisely that one relation; matching its exact Hilbert numerator to the full gradient ideal's Gröbner Hilbert numerator proves exhaustiveness over all degrees. Therefore neither a finite-rank table nor bounded experiment is being used as an infinite proof. The characteristic-zero resolution is attributed to Malara–Pokora–Tutaj-Gasińska, Proposition 2.1 (2021); its published proof is the external premise, not re-certified here.

This is a self-review only. No independent audit, external formal proof, or exhaustive historical priority review has been performed.
