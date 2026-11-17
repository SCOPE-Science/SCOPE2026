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

The analytic identity is established by an angular half-circle anchor partition for three independent, non-identically distributed rays, followed by an exact one-dimensional integral reduction. The proof states the endpoint restrictions, differentiates under the integral only for fixed radius below one, and derives the contact cusp from a uniform bound on the singular integral's regular remainder.

For reproducibility, run `python mixed_circle_check.py` (NumPy and SciPy). The checker evaluates the exact profile by adaptive one-dimensional quadrature and independently samples Euclidean points, computing triangle containment with oriented cross products. It verifies five finite-radius probabilities, both endpoint values, a local Taylor expansion, and the approach of the logarithmic boundary coefficient. Empirical finite-sample and finite-precision checks do not prove asymptotic statements.

Historical priority was compared against the two full Marckert papers and the closest accessible related studies. A complete search of historical sources cannot be guaranteed; no external independent mathematical validation is claimed.
