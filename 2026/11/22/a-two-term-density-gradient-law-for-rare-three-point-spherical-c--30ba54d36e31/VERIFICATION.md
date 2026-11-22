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

# Verification of the three-point spherical-cap density-gradient law

Run `python3 CHECK.py` from the directory containing both this file and the checker. It requires only Python's standard library. The checker evaluates independent planar lens moment integrals and exact weighted spherical-lens identities for uniform, dipole, and quadratic Legendre sampling, at five nonzero radii, then evaluates their small-radius series.

These checks establish reproducibility of finite analytic identities, not an exhaustive or independent proof. The symbolic proof of the general \(C^2\) theorem uses normal-coordinate Taylor expansion, vanishing of the odd term under point reflection, dominated convergence at the Euclidean cluster domain, and the exact spherical uniform normalization. The exceptional tangent configurations have zero four-dimensional Lebesgue measure. The leading planar moment is \(9\pi^2\), and its second moment is \(15\pi^2\).

The direct finite-radius uniform formula is known from the Miles/Bürgisser--Cucker--Lotz literature, and is not claimed as original. The proposed additional term concerns nonuniform positive smooth spherical densities. Full references and scientific limitations are in `RESULT.md`. Independent mathematical verification has not been performed.
