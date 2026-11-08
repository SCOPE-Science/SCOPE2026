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

# Numerical and analytic verification

The self-contained numerical checker `acute_dimension_check.py` requires Python, NumPy and SciPy. Run `python acute_dimension_check.py`. It computes a beta-function form of the exact integral by adaptive quadrature and checks a separate Gaussian-normalized sphere sampler using direct tangent-angle dot-product inequalities. With seed 41, 450,000 independently sampled triples were used for each of dimensions 3, 5, 16, 128.

Numerical integral: dimension 3: 0.03415494309189718, dimension 5: 0.06068076694054449, dimension 16: 0.09204765692556618, dimension 128: 0.11372439114807631; independently sampled estimates 0.0341022, 0.0607022, 0.0922444, 0.1131489. Dimension 3 checks against the already known formula \(1/(2\pi)-1/8\). For dimension 256, the numerical defect times \(\sqrt{256}\) is approximately 0.127277, approaching the derived \(1/(\sqrt2\pi^{3/2})\).

Mathematical validation is the explicit analytic chain in `RESULT.md`: normalization of independent scalar spherical coordinates; exact tangent-angle sign characterization; measure-disjoint complement partition; four beta moment evaluations; and the pointwise third-moment remainder inequality for all integer dimensions at least five. Numerical values do not prove the all-dimensional claim, and no independent mathematical audit has been performed.
