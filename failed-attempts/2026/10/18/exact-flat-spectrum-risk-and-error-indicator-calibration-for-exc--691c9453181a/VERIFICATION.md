---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Let V be an orthonormal basis matrix for the range of P and g_i=Vᵀω_i. Then the g_i are independent standard Gaussians in R^r. For each J the Nyström matrix is λVΠ_JVᵀ, where Π_J projects onto the span of the g_j with j∈J; this follows from G_J(G_JᵀG_J)^†G_Jᵀ=Π_J, including the empty case. Thus f(B_J)=cVΠ_JVᵀ. For k≤r the added direction is the held-out residual, whose squared norm is χ²_d conditional on the other columns. To check the covariance, condition off the other k−2 columns, leaving two independent Gaussian vectors in q=d+1 dimensions. Their residual energies have independent squared radii times the same factor 1−U, where U is the squared directional cosine. Conditional on U the energies are independent and each has mean q(1−U); consequently covariance is q²Var(U)=2(q−1)/(q+2), since E U=1/q and E U²=3/[q(q+2)]. Exchangeability yields Var(H)=[Var(H_i)+(k−1)Cov(H_i,H_j)]/k and E S=[Var(H_i)−Cov(H_i,H_j)]/k. This verifies the risk, the calibration ratio, and the k=r limits at fixed c. At k=1 the marginal law gives the risk and there is no indicator; for k≥r+1 every leave-one-out span fills the active range and both estimator and indicator are exact. The argument is for raw Gaussian probes and does not require c>0. The frozen script was inspected, not executed; its residual checks do not independently verify the pseudoinverse identity.

## originality

FAIL

Resultary 4aed760e42f3 explicitly gives the exact unnormalized identity-matrix dependence, diagnostic calibration, and rank-budget cliff. The new notation A=λP does not give a new covariance law: in range coordinates the entire vector of leave-one-out estimates is exactly c times the identity-matrix vector at dimension r, and the squared diagnostic is c² times the corresponding diagnostic. The distinct same-day record 2a86145c3a4b additionally states the full scalar-identity FlexTrace formulas. This decision rests on exact earlier indexed identity-case coverage and the pathwise reduction, not on assigning priority between same-day records.

## value

FAIL

The exact unnormalized risk/diagnostic gap is a meaningful benchmark, but it is the existing benchmark at dimension r. The extra nullspace and the spectral function only replace n by the active dimension and multiply the estimates by c. They reveal no additional dependence, behavior, or usable calibration beyond the prior result. The endpoint extensions are elementary and are not a surviving substantive claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
