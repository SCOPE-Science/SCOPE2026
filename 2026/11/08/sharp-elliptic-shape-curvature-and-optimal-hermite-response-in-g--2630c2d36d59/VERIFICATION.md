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

# Reproducibility and mathematical checks

The primary analytic verification does not rely on numerical interpolation: disk eigenvalues are \(\lambda_n(s)=\frac1{n!}\int_0^s e^{-v}v^n\,dv\), with unique leading eigenvector \(h_0\), second-level gap \(s(s+2)e^{-s}/2\); the directly differentiated ellipse Gram matrix has \(P''_{00}(0)=-2s^2e^{-s}\), \(P'_{20}(0)=s^2e^{-s}/\sqrt2\), and \(P'_{n0}(0)=0\) for all other \(n\ge1\). Substituting in the complete perturbation formula gives \(\lambda_{\max}''(0)=-4s^2e^{-s}/(s+2)\); the eigenvector derivative is \(\sqrt2s/(s+2)h_2\). A ninety-degree rotation sends \(t\) to \(-t\) and forces evenness, giving the remainder \(O_s(t^4)\).

The independent finite-section checker `check_elliptic_stft.py` requires Python with NumPy and SciPy. Run `python check_elliptic_stft.py`; the observed output on the packaged source was `ELLIPSE_STFT_CURVATURE_CHECKS_PASS 148`. The implementation directly integrates the Fock Gram matrix on the transformed disk by Gaussian quadrature. It checks disk diagonalization, the complete selected derivative column, diagonal second derivative, invariance under opposite stretches, convergence of normalized top-eigenvalue losses, and convergence of the eigenvector's Hermite-2 component. Four area parameters and three deformation magnitudes are tested. These assertions are numerical with explicit error tolerances and cannot themselves prove an infinite-dimensional theorem.

Unproved limits: no claim for finite non-small \(t\), no uniformity as \(s\) varies, no higher-dimensional signal theorem, no alternative window, no independence or external certification. First-public source dates are from initial arXiv postings, not journal revisions.
