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

# Reproducible checks and limitations

Run `python checker.py` with Python 3.9 or newer; no external modules are required. The script reconstructs the moment contractions \(\mathbb E[x^2]=1/d\), \(\mathbb E[x^4]=3/(d(d+2))\), \(\mathbb E[xyz]=\mathbb E[x^2y^2]=1/d^2\) as explicit finite-dimensional rational calculations and checks the derived fourth-degree variance and third-moment expressions. Using fixed-seed standard Gaussians normalized to the sphere, it independently evaluates the exact tangent-angle area, comparing means and second and third centered moments across four dimensions. The output marker `RANDOM_SPHERICAL_TRIANGLE_AREA_MOMENTS_OK` denotes checks passed, not external certification.

The analytical verification rests on exact spherical tangent-angle formulas, a uniformly bounded Taylor remainder near orthogonal Gram triples, beta moment bounds for independent sphere vectors, and exponential concentration on the complement. The Gaussian limit uses the coordinatewise multivariate CLT. Numerical finite samples are not used to infer or certify the infinite-dimensional assertion. Independent validation and a comprehensive historical-priority audit have not been performed.
