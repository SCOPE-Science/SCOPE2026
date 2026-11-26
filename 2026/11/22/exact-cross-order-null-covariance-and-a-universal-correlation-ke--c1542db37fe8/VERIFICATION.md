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

There are n linear gaps and N_r=n−r+1 complete windows. The squared pair-difference identity gives the exact factor 2n²/(N_r−1), with A_r annihilating constants. For rate-one independent E_i, D_i=E_i/S is independent of S; dividing the quadratic-product expectation by E[S⁴]=(n)_(overline 4) transfers it to the Dirichlet law. Centering E is allowed because A_r 1=0. The three moment pairings and fourth cumulant six yield t_r t_s+2w_rs+6v_rs and the mean denominator (n)_(overline 2). I reproduced exact mixed moments from raw pairwise-difference monomials without starting from that trace derivation: python3 /workspace/review_checks/4.py; e.g. Cov at (n,r,s)=(4,1,2) is 8192/4725 and at (6,2,3) it is 232/49. For fixed orders, empirical-mean centering and endpoint terms are O_P(1/n) before scaling and expansion of (n/S)² contributes −2r times the sample mean of Z_i=E_i−1 inside the influence sum. As a separate check, expanding and summing the influence functions gives coefficients r on Z_i²−1−2Z_i (variance four) and 2(r−h) on Z_i Z_(i+h), 1≤h<r. Different lag products are orthogonal in the summed covariance, as are the single-site terms and products. With the outer factor two, this gives 16[rs+sum_(h=1)^(p−1)(r−h)(s−h)]=8[rs+p²q−p(p²−1)/3]. It also proves correlation strictly below one for distinct orders from the unequal highest nonzero lags. The stationary finite-dependence CLT and Cramér–Wold give the joint law (possibly degenerate when r=s); fixed-order trace asymptotics give the same actual covariance limit, not just a CLT variance. In the prescribed sequential limit the leading terms are p²q−p³/3 and (2/3)(pq)^(3/2), giving sqrt(u)(3−u)/2; the O(sqrt(p/q)) bound covers u=0, and direct fixed-p expansion gives the separate s^(−1/2) coefficient. No triangular-array limit follows.

## originality

PASS

The previously defined statistic, diagonal marginal limit, and general Dirichlet moment calculation are not alone new. The supported distinct claim is the explicit mixed-order dependence for the specified same-sample overlapping windows, especially the evaluated fixed-order covariance and sequential scale kernel. Two older spacing references remain access risks; their reported scopes are not treated as independent full-text exclusions.

## value

PASS

Two spacing orders are computed on the same sample, so their individual null laws do not calibrate a combined diagnostic. The exact covariance gives dependence at finite n and the explicit leading kernel shows how redundancy varies from nearly zero at separated scales to one at equal scales. This is a natural mixed-order invariant of the existing test family and not merely a recomputation of its diagonal. The result supplies no simultaneous growing-order CLT, combined-test critical values, fitted-null theory, or power claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
