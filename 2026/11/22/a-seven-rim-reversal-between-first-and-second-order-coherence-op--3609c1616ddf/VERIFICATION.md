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

# Verification and reproducibility

Execute `python3 verify.py` using the ordinary Python 3 standard library. Observed output: `PASS 127 checks`.

The checker verifies seven exact-rational separator pairs with Gauss–Jordan elimination using `fractions.Fraction`, then compares independent full-wheel pseudoinverse trace calculations with the cycle Fourier reduction at four sizes. It also runs clearly supplemental numerical bisection checks for finitely many sizes and asymptotic illustrations. The exact finite checks do not rely on floating-point tolerances; the numerical convergence diagnostics do not certify the infinitely many remaining sizes. The all-size inequality and scaling claims are proven symbolically in `RESULT.md` using strict convexity, a Poisson-kernel identity, rational bounds, and a limiting integral. Independent audit has not been performed.
