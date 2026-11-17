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

For isotropic M=σ[I_r 0], at every reached rank k with fresh Gaussian block b, residual X~χ²_{b(r-k)} and captured Y~χ²_{bk} are independent conditionally on full past. Therefore P(stop|reached k)=I_tau(b(r-k)/2,bk/2) and the finite stopping mass is p_j∏(1-p_i). True squared relative Frobenius error equals (r-k)/r. Chernoff entropy tail nD(u||tau), n=br/2, and uniform one-sided beta Laplace tail with u=tau+c sqrt(log r/r) produce exponent bc²/[4tau(1-tau)], with ~sqrt(r/logr) effectively competing k. This yields c*=sqrt(2tau(1-tau)/b) in probability and false tolerance acceptance tending 1. Independently checked integer beta/binomial identity and the r=2048 b=2 tau=1/4 false-stop probability 0.987911365509179. Fresh batches, fixed b, r multiple b, tau∈(0,1) essential; no claims for practical averaged-denominator HSS pipeline.

## originality

PASS

PASS best-of-knowledge for algorithm-specific exact entire FIRST-stopping-rank law and sharp sqrt(r log r) premature rank scale under fixed fresh batch b. A single Gaussian look beta ratio is classical and is in the antecedent Do–Chen algorithm; unrelated row-pruning chi-square minimum result is not the same process. No general algorithm guarantee is asserted.

## value

PASS

PASS: A first-stopping-rank law and sharp order sqrt(r log r) premature acceptance explain a concrete failure mechanism in a natural adaptive Frobenius stopping rule. This is a meaningful accuracy limitation of a numerical algorithm rather than a single cherry-picked counterexample; the fixed-b, flat-spectrum scope is explicit. Standard beta identities are tools, not the valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
