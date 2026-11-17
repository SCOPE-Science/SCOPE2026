---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Uniformly sampled vertices of the square doubly substochastic polytope are partial permutation matrices of sizes k=0..n, count M_n=sum C(n,k)^2 k!. A specified entry is occupied with probability mu=M_(n-1)/M_n; two disjoint entries with probability eta=M_(n-2)/M_n, and two sharing row or column with probability zero. This gives exact operator ΣY=(mu+eta)Y-eta(row+column sums)+(eta-mu^2)(all entries sum) and eigenvalues lambda0=mu-n^2mu^2+(n-1)^2eta, lambda_r=mu-(n-1)eta twice(n-1), lambda_i=mu+eta (n-1)^2. The positive distinct Laguerre zeros factor the matching-size PGF into a sum of unequal-parameter Bernoullis, proving lambda_r>lambda0 via strict variance concavity; eta>0 gives lambda_i>lambda_r. For D=n-K, the Laguerre PGF L_n(-z)/L_n(-1) and classical analytic-uniform Perron formula yield ED=sqrt(n)-3/4+O(n^-1/2), VarD=sqrt(n)/2-1/2+O(n^-1/2), and hence scaled eigenvalue limits 1/2,1,1 and condition number 2sqrt(n). Independently enumerated all n=2,3,4 matching vertices, computed rational covariance matrices and directly checked complete n^2-dimensional eigenspaces. The asymptotics rely on the cited classical theorem and complex-uniform differentiation, not the finite checks.

## originality

PASS

The matrix-symmetry decomposition and square covariance formulas can be obtained by algebraic diagonal specialization of the same-date rectangular p<q covariance operator formula, which is credited; the genuinely new surviving part is the **balanced joint-growth asymptotic**: three distinct powers with constant 1/2 and sharp 2sqrt(n) condition number. The rectangular published result proves fixed p, q->infinity, with condition number q+O_p(1), not p=q->infinity. Prior Heuer-Striker proves vertex structure and counts, not vertex-uniform covariance. Best-of-knowledge: no earlier exact sharp balanced limit located; same-date relationship and historical rook-statistics equivalences are risks.

## value

PASS

The canonical uniform discrete vertex measure of the matching polytope has a natural full-space inertia matrix. Its balanced high-dimensional degeneration is sharply quantified: constant and row/column directions fluctuate as n^-3/2, interactions as n^-1, with exact anisotropy 2sqrt(n). The genuine balanced-asymptotic result requires the nontrivial deficiency variance and differs from the fixed-height q growth theorem; it provides a meaningful exact benchmark for random partial permutations and discrete isotropic-position questions. Generic tensor diagonalization and vertex counts alone would not justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
