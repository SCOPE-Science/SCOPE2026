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

For W_n=1-A_n, insertion of an independent uniform query point gives E[K_n W_n]=(E[K_m(K_m-1)]+E[U_m])/m, m=n+1, where U_m counts sample points with exactly one dominator. Indeed sum the skyline size after deleting each maximal point: K_m-1 original maxima remain, plus precisely the points uniquely dominated by the deleted point. A sole dominator is maximal by transitivity. Integrating the binomial probability over the product of two independent uniforms gives E[U_m]=H_m-1, and E[K_m(K_m-1)]=H_m^2-H_m^(2) by independent record indicators. With E[W_n]=H_m/m this yields the frozen mixed covariance with minus sign for A_n. Its strictness also follows from the frozen positive sum for Cov(K_n,W_n), with each s=1,...,n-1 contributing positively. For the variance, conditioning on the running minimum V_s gives E[V_t|V_s=z]=integral_0^z (1-u)^(t-s) du; integrating with V_s's beta law gives the stated covariance kernel, including zero for s=0. With m=n+1, summing the kernel over both indices reduces to the sum over j=1,...,m of (2j-1+1/j-2H_j)/(j(j+1)); telescoping gives Var(sum V_t)=2(m+2)H_m/(m+1)-H_m^(2)-4m/(m+1). The Dirichlet second moment then gives the frozen area variance. Independently I expanded the void probability for two uniform query points, separating the comparable and incomparable rectangle pairs. This gives E[W_n^2]=2 sum_{k=0}^n (-1)^k binom(n,k)(1+H_(k+1)/(k+1))/(k+2)^2; exact rational substitution confirmed Var(A_n) at n=1,...,10 (first values 7/144, 65/1296, 2567/57600). Finally Var(K_n)~log n, Var(A_n)~2 log(n)/n^2 and Cov(K_n,A_n)~-log(n)/n prove the stated Pearson limit. The frozen script was inspected, not executed.

## originality

PASS

The exact finite-n mixed covariance and the nonzero limiting correlation concern the whole dominated area. The closest verified exact result uses a fixed-threshold corner count, and the primary record results examined give marginal count information, not this mixed invariant. The verdict credits the supported joint result, not the use of record indicators or a claim of universal priority for hypervolume moments.

## value

PASS

Cardinality and dominated area are natural distinct summaries of the same skyline. The exact covariance provides both a finite-sample sign and its scale, while the area variance shows why standardized anticorrelation persists even though unstandardized covariance vanishes. This exact joint benchmark is useful for the square model without extrapolating it to other Pareto fronts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
