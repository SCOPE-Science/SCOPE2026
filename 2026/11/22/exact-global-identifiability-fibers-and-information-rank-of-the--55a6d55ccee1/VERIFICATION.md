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

Reproduce with `python check_identifiability.py` and SymPy installed. Exact symbolic assertions check the normalizer via the first two beta moments, the special \((\rho,\delta)=(0,1)\) beta-function shift, cancellation of \(\rho\) at \(\delta=0\), inversion of the normalized quadratic coefficients and both zero-tilt score identities. Three rational beta-shape examples plus three exact rational pointwise density comparisons support the special-fiber identity; all checks completed successfully. Independently of the checker, the full mathematical proof in RESULT.md covers infinitely many parameters by endpoint exponents, equality of normalized polynomials and linear independence of logarithmic and linear scores. No finite computation certifies uniqueness outside the algebraic proof. Source review used the 2021 preprint and the complete author-hosted journal article, with careful inspection of the density and identifiability propositions. No independent validation has been performed.
