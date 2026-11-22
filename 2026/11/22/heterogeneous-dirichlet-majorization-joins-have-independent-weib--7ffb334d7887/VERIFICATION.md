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
The claimed asymptotic law is proved analytically in `RESULT.md` under strictly positive fixed Dirichlet concentration parameters. The key cross-rank probability bound has exponent strictly greater than one, implying that a single sample cannot simultaneously produce the rank extremes in the limiting window. The finite argument also proves that the least concave majorant is inactive with probability tending to one.

Run the self-contained standard-library script `python3 check.py`. It checks integer-special-case Beta-tail coefficients by exact rational arithmetic; validates all finite subset-pair exponent inequalities in four independently specified parameter vectors; tests the uniform-parameter reduction; and performs deterministic-seed Monte Carlo diagnostics for the \((1,1,2,4)\) example. A successful replay yields 809 passing assertions, an approximate concavity frequency of 0.9975 and an approximate distinct-witness frequency of 0.8625 for the stated finite simulation design. The latter frequency need not be near one at that finite size; its limiting behavior is proved separately.

The finite checks are not an exhaustive proof and do not constitute independent validation. No Lean or external certificate is claimed. The theorem does not include a finite-sample error rate or growing-dimensional inference. The primary source and closest comparable theorems are cited in `RESULT.md` and the scope of their implications is assessed in `REVIEW.md`.
