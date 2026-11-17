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

The unconditional triangle indicator has probability 1/4. For a pair at shorter separation δ∈[0,π] the conditional chance that an independently sampled third vertex makes a central triangle is δ/(2π); δ has uniform density 1/π. Integrating for δ≤α=πq gives joint probability q²/4 and Cov(H_ijk,J_ij)=−q(1−q)/4. An overlap of only one point gives zero by rotation invariance; disjoint supports are independent. Exactly 3*C(n,3) pair-in-triple incidences yield Cov(T_n,E_n,α)=−(n−2) C(n,2)q(1−q)/4. Edge indicators sharing a point remain uncorrelated; Var(E)=C(n,2)q(1−q). Distinct central-triangle indicators sharing two vertices have covariance Var(δ/(2π))=1/48, with C(n,2)(n−2)(n−3) ordered pairs; their Bernoulli variances give Var(T)=n²(n−1)(n−2)/96. Division gives Corr=−sqrt(3(n−2)q(1−q)/n). For n≥3 and 0<q<1 both variances are nonzero. q(1−q) has unique maximum at q=1/2. Endpoints q=0,1 correctly exclude Pearson correlation. Independent exact rational overlap/variance checks at n=3..18 and several q values corroborate the algebra, not the universal proof.

## originality

PASS

Best-of-knowledge originality: the complete exact joint covariance and sharp right-angle anticorrelation of the unnormalized central simplicial-depth count and circular short-edge count is not obtained by the located marginal-depth and geometric-graph results. Generic mixed U-statistic covariance machinery gives the overlap method, not by itself this evaluated law; the two-point circular geometry and exact shared-index enumeration supply the specific formula. One relevant marginal-depth full text was not accessible and general U-statistic specialist literature remains a historical priority risk.

## value

PASS

Both observables are canonical statistics of the same uniform circular sample. The exact finite-n dependence, strong nonzero large-sample correlation −sqrt(3)/2, and intrinsic optimum at the chord length sqrt(2) distinguish their joint behavior from independent marginal calibration. The result addresses the natural entire continuous cutoff family, not an arbitrary finite table or parameter relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
