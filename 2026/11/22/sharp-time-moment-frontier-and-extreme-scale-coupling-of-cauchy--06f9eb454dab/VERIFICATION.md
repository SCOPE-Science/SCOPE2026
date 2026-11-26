---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For real a, lambda > 0 the Gamma integral gives the coefficient with modulus Gamma(2a+1) t^(a+1/2) / [lambda^2(1+t)^2+y^2]^(a+1/2). The two norm squares contribute Gamma(2a+1)Gamma(2a)/(2 lambda)^(4a+1), and the left Haar factor is dt dy/t^2; Gamma(2a+1)/Gamma(2a)=2a gives the stated constant. The change y=lambda(1+t)z including its Jacobian factorizes the joint density as beta-prime(2a,2a+1) times the normalized symmetric Student-type factor. The beta integrals for (1+T)^q and |Z|^q and Gamma duplication give the stated moments, including mass one at q=0. The first factor has moment threshold 2a+1, with logarithmic divergence at equality, and the independent second has threshold 4a+1; nonnegative integration rules out cancellation. With R=|y| and u=lambda t/R the rescaled marginal integral has kernel u^(2a-1)/[1+(u+lambda/R)^2]^(2a+1). It is bounded by its integrable pointwise limit of mass B(a,a+1)/2, giving both the coefficient and L1 convergence of the normalized conditional densities, hence TV. Gamma log variances give the log-scale result; symmetry and q=2 give the time variance. 'Necessarily' denotes conditional order in probability (the limit is positive, finite and nondegenerate), not a deterministic lower bound on T at a given y. Read RESULT.md lines 5–89 and verify.py; the recorded 39 checks are finite diagnostics, not the all-parameter argument. No uploaded code run.

## originality

PASS

Pass applies to the combined explicit ambiguity probability law, sharp fractional-moment frontier and exact displacement-conditioned scale limit, not the affine kernel, orthogonality, or general variance pullback. The strongest available comparisons concern distinct observables or reconstruct the starting coefficient, not the combined marginal and conditional result. The proof specializes standard integral and asymptotic tools; no new general moment or tail principle is claimed. Priority outside inspected material is unresolved.

## value

PASS

Analytic Cauchy windows are a natural uncertainty model. The scale and time log/ordinary variances have different finiteness regimes; for every real order the exact moment frontier says when the ambiguity-based time statistic can be used. Beyond computing a known kernel, the TV limit quantifies which dilations accompany extreme displacements and gives a usable conditional law, with a sharp tail coefficient for normalization. This is a narrow explicit family calculation, not a general uncertainty-minimization result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
