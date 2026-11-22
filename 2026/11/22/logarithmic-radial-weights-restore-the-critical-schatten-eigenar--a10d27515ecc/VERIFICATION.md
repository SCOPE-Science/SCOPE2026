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

# Mathematical verification

The proof in `RESULT.md` derives the diagonal channel formula from the published Kraus representation, derives the first-difference moment asymptotic from the same radial integral with one extra factor, compares the unique nonreal boundary eigenvector product with the moment product, and uses the exact power-log series test. No unavailable computation or external certificate is required to complete this analytic proof.

A numerical cross-check for \(b=1\), \(\gamma=-2\), \(\theta=\pi/3\) evaluated the normalized moment integral with numerical quadrature, recursively constructed the diagonal eigenvector up to index 256, and found the ratios \(|x_n|/\sqrt{\omega_n}\) equal to approximately 2.92418, 2.94506, 2.95503 at indices 64, 128, 256. These numbers support—but cannot establish—the positive limit. The actual proof covers all indices and all claimed parameters.

The gamma-negative endpoint is proved through \(\sum_{n\ge2}[n(\log n)^{2}]^{-1}<\infty\) in the example. No claim is made about non-diagonal eigenvectors, real endpoint eigenvalues, or independent audit.
