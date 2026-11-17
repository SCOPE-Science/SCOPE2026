---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For positive definite H with spectrum in the inclusive [mu,L], the joint Gaussian target has an exact outer Y reflection; a conditional mirror or independent Gaussian refresh preserves the conditional X law. Along one eigendirection, the Bernoulli-averaged mean transfer has characteristic z^2-t(2-rho)z+1-rho. Balancing endpoint |t| and repeated roots gives unique affine minimax tuning eta=(mu L)^(-1/2), rho=1-q^2, q=(kappa^(1/4)-1)/(kappa^(1/4)+1), for kappa>1. Unconditional covariance errors evolve via (1-rho)Sym^2(M0)+rho Sym^2(M1), not Sym^2((1-rho)M0+rho M1), with the stated cubic. Its endpoint signs P(q)<0<P(1) guarantee an eigenvalue in (q,1). Positivity of the lifted map and L^2(Sigma)≺Sigma force all quadratic modes below 1, while positive cone comparison and the positive definite position-functional Gram matrix show a legitimate centered Gaussian initial covariance Sigma+epsilon I has position-variance defect of exact root rate r2>q. The kappa=1 all-refresh case is treated separately; no full L2 or TV assertion is made. Independent rational computation reconstructed the cubic at q=1/3, its two signs, and positive variance defects, giving r2≈0.4098522656577.

## originality

PASS

The classical critical-damping affine/SOR rate and Gaussian stationarity are explicitly credited; the retained claim is a strict second-degree covariance slowdown with a legitimate position-variance witness in an exact conditional-mirror/refresh Bernoulli kernel. This is not a consequence of fixed-coefficient Gaussian covariance tensorization or the inspected related findings. The original 2026 sampler paper could not be inspected in full because authorized access was blocked; priority remains provisional rather than an invented exclusion.

## value

PASS

A mathematically meaningful counterexample to the common inference that first-degree spectral optimization controls degree-two relaxation: the two eigenvalue optimizations separate at every nontrivial condition number, and a real position variance displays the slowdown. The result sharply identifies the role of shared Bernoulli switching without pretending to solve global sampler mixing or oracle complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
