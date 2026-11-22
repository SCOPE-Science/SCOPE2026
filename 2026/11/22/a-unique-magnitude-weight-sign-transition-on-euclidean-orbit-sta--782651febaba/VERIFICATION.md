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

# Computations and proof limits

The analytic proof has four independent logical ingredients: (1) strict positive definiteness via a positive mixture of Gaussian kernels, (2) the exact two-dimensional weighting reduction and strictly convex exponential-sum sign criterion, (3) uniform Euler--Maclaurin expansion and a simple limiting root, and (4) strictly positive circular Fourier coefficients and divisibility aliasing.

Running `python3 center_magnitude_verify.py` from the extracted files produces a successful check of 102 polygon and twelve spherical-orbit direct linear-system solves, plus thirteen root/ordering profiles. The reference numerical values are \(t_\infty\approx1.36351481573219\), \(D\approx0.06794808738018\), and \(K\approx21.0141216788913\). The values validate expressions, not the infinite claims: their proofs are in the result text.

No independent mathematical audit or external formal certification has been performed.
