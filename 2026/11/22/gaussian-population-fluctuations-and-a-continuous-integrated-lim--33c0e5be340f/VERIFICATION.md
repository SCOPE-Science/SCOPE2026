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

# Verification notes

The proof is self-contained once the normalized Itô excursion entrance law is accepted as stated in the primary source. The critical finite-intensity identity is \(\mathbf n(\xi>t)=\sqrt{2/\pi}\,t^{-1/2}\), giving \(\kappa=2\rho\sqrt{2/\pi}\). For \(s\le t\), direct overlap integration yields \(K(s,t)=\kappa(\sqrt t-\sqrt{t-s})\).

The finite-dimensional Gaussian step is proved for arbitrary fixed real coefficient vectors, using the compensated Poisson characteristic exponent and the bound \(|e^{iz}-1-iz+z^2/2|\le |z|^3/6\). The \(L^2\) norm of each scaled integrand is invariant, and its \(L^\infty\) norm tends to zero. The identical argument for time-integrated kernels yields finite-dimensional convergence of \(H_T\). Its continuous sample paths and uniform \(L^2\) increment estimate establish tightness in the uniform topology. In particular, there is **no** claim of path-space convergence for the instantaneous count, which has densely many infinite values.

The standard-library command `python3 checker.py`, executed from the directory containing these files, passed **1017** finite numerical and structural consistency checks. They cover the bivariate Poisson overlap decomposition, integrated covariance double quadrature, self-similar kernel, increment bounds, local tangent, positive semidefinite Gram tests and seeded Poisson sampling. They are not proofs of asymptotics or historical novelty. All theorem statements rely on the analytic reasoning in RESULT.md.

Scientific limitations and priority risks are documented in RESULT.md, REVIEW.md and AUDIT.json. An independent mathematical audit has not been performed.
