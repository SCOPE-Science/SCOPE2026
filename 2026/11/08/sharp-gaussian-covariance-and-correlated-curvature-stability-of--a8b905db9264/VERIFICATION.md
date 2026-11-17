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

For iid uniform coordinate J and independent full-dimensional ξ∼N(0,I_d), the exact second-moment operator is T_h(S)=d^(-1)Σ_j(I−dh e_j e_j^T H)S(I−dh H e_j e_j^T), with additive 2hI. Direct expansion T_h(H^(-1))=H^(-1)−2hI+dh²diag(H_jj) and H-energy contraction proves constant-diagonal unique finite-variance stationarity exactly h<2/(da), with covariance H^(-1)/(1−dah/2); above boundary positive forcing produces energy divergence, with no claim about infinite-variance stationary laws. In d=2 the Frobenius self-adjoint positive-cone transfer and Sylvester/evaluation reduction give h*=1/λmax(K), K=[[a−c²/(a+b),c²/(a+b)],[c²/(a+b),b−c²/(a+b)]]. Correlated unequal diagonals strictly decrease λmax and improve stability; taking singular positive-definite limit yields sharp unattained gain (1+√2)/2. Independent symbolic 2x2 example H=[[1,1],[1,4]] gives K=[[4/5,1/5],[1/5,19/5]] and h*=(23−sqrt229)/30 ≈0.26224>1/4.

## originality

PASS

Ding–Li JMLR 2021 supplies exactly the same full-noise unbiased random-coordinate gradient estimator and conservative general Wasserstein convergence analysis, not sharp quadratic finite-variance stationarity, exact isotropically inflated H^(-1), or 2D correlation gain. The superficially similar Oct13 Resultary Gaussian-invariant classification is for a different coordinate-only noise kernel sqrt(2h/p_I)e_I ξ, not the present sqrt(2h)ξ in every coordinate. Full prior RESULT inspected, so its Gaussian-law theorem does not cover this generally non-Gaussian stationary law or mean-square threshold. Best-of-knowledge exact classification survives.

## value

PASS

Sharp finite-second-moment stability and exact stationary covariance are natural Gaussian sampling diagnostics. The counterintuitive strict stability gain from off-diagonal Hessian correlations and its universal unattained 1.207… envelope resolve a motivated parameter sensitivity question beyond conservative LMC conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
