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

The general existence proof uses only exact Gaussian KL addition, renewal-reward normalization, one-dimensional Laplace asymptotics and intermediate-value arguments. The closed expressions for the small- and large-rate asymptotic coefficients are derived in RESULT.md; both are strictly positive for any reset variance \(0<q<1\).

For the explicit example, execute `python3 sign_certificate.py` with a standard Python 3 interpreter. Its four strict sign assertions were actually executed successfully. All sign decisions use `fractions.Fraction`; printed decimal approximations are informational only. The infinite geometric tail and the exponential Taylor and Bernoulli/logarithmic bounds have certified finite error. An independent quadrature evaluation returned the same four signs, but supplies no proof and is not relied on.

The claimed crossings follow from continuity and the exact sign witnesses, not from sampling a finite grid. The certificate does not establish the complete number of roots, the smallest admissible scale separation, experimental thermodynamic work, or originality against all unpublished literature. Independent audit: not performed.
