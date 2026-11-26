---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Condition on B: X_T is Gaussian with integrating-factor mean and variance. Under the scaling B_{Tv}=sqrt(T) times a unit-time Brownian path in law, physical backward lag y/T becomes y/T² in that path. For G≠0 the last fixed fraction of the unit path is bounded away from zero, giving an integrable exponential majorant on the corresponding y-range and a negligible T²-exp(-const*T²) tail. This yields TV_T→D/(bG²) and vanishing scaled initial mean on the scaling coupling, including a=0. Future W increments form a standard Brownian driver independent of the initial data; the environmental increment divided by sqrt(T) has squared uniform norm O_P(T^-2). With nonnegative drift, integration by parts bounds the convolution by twice the driver supremum. The drift difference bound can be taken as H times the uniform coefficient error times the tight solution supremum. The resulting continuous frozen solution map proves convergence in C([0,H]), not just of marginals. The conditioned Gaussian pair is stationary with correlation exp(-bG²u); no axis atoms obstruct weak convergence of the sign product, including u=0. Rescale g by sqrt(bu), use dominated convergence, and integrate the nonnegative arcsine series termwise. Independent 60-digit quadrature, integrating by parts after exp(-y²)=sin(theta), reproduces K=0.5388516236620413677555756… . The heavy tail and nonintegrability concern the sequential limiting sign process only.

## originality

PASS

The exact model, the one-time Cauchy result, and the Gaussian quadrant formula are prior ingredients. The specific temporal weak limit and sign law are distinct from those ingredients and not found as a covered result in the sources inspected.

## value

PASS

The inverse-age window is set by the model’s typical stiffness, not an arbitrary lag choice. The result specifies observable temporal dependence unobtainable from the Cauchy marginal and identifies how very small but positive frozen rates create nonintegrable sign memory without any conditionally slow algebraic decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
