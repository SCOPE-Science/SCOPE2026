---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The actual RESULT.md fixes N>=2, a strictly positive mass, spring stiffness and endpoint damping, positive independent reset rates and diffusivities, plus independent endpoint Gaussian thermal inputs. The Dirichlet chain eigenvectors do not evade endpoint damping, so its response is exponentially stable. For every site l, the left-wall velocity response has nonzero positive leading term (k/m)^l t^{2(l-1)}/[2(l-1)]!; its positive-real Laplace transfer is positive by the irreducible M-matrix inverse. Conditional on independent reset-clock histories the velocity is centered Gaussian. The last-reset-age conditional variance H(a) has derivative 2D G(a)^2-(4D/r)g(a) integral_a^infty g(t)e^{-r(t-a)} dt, with strictly negative first nonzero small-a term. Thus the random variance is nonconstant at every site, independent right-wall and thermal contributions cannot cancel it, and cum4(v_l)=3 Var(Sigma_l)>0. Matching Brownian-reset and OU two-time covariances proves equality of quadratic observables but Gaussian OU has zero fourth cumulant. The source-checker derivation of the four-time wall input and Taylor coefficients was read, not substituted for the infinite proof.

## originality

PASS

The 2023 reset-wall chain study numerically observes finite-chain positive kurtosis but does not establish an all-site all-positive-parameter strictness theorem; its full accessible text/appendices are compared with the actual proof. A 2025 resetting-wall four-time connected cumulant is explicitly acknowledged as prior input, not new. The 2026-10-26 result concerns the slowly resetting scaling limit and universal trough, not arbitrary positive reset rates and every finite site. Best of knowledge: the conditional-variance nondegeneracy theorem is distinct and not implied by these sources.

## value

PASS

A rigorous uniform all-site sign theorem for non-Gaussian stationary fluctuations is substantively stronger than a plotted or numerically inferred kurtosis sign; the covariance-identical OU control demonstrates why two-point transport does not diagnose non-Gaussianity. The theorem treats all positive chain parameters and independent finite Gaussian heating, a natural robustness question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
