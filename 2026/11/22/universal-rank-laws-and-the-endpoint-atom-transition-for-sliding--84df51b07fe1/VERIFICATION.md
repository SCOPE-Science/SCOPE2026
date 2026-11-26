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

With iid continuous inputs the union ranks are uniformly permuted. A common output must occupy one of w−ℓ+1 intersection slots. Conditional on its quantile, each exiting/entering pair must agree on its exceedance indicator, since exactly r−1 observations must exceed the output in every window. Choose k above-candidate pairs and r−1−k above-candidate shared observations and integrate their conditional probabilities, giving the factorial sum. Sum only admissible binomial indices, so no negative factorial is evaluated when a binomial vanishes. For two adjacent windows the only ways to retain the value are that both exclusive endpoints are below union rank r or both above union rank r+1. Counting these ordered pairs gives 1−p_{w,r}. Stationarity subtracts S(ℓ+1) from S(ℓ) for the start event, and the mean telescopes to 1/p; empty intersection rules out ℓ>w. On compact subintervals of (0,1), the finite fixed-r sum expands uniformly as s_r(ℓ/w)+g_r(ℓ/w)/w+O(w⁻²), with smooth g_r and s_r(t)=((1−t)/(1+t))^r; adjacent subtraction and wp→2r yield the stated survival. Differentiation gives the densities, and the two one-sided survival limits identify all endpoint masses. At ℓ=w only k=r−1 is admissible and the factorial products give C_r w^(1−r), in particular 1/4 for r=1 and leading 1/(16w) for r=2. An independent bounded replay enumerated permutations of the w+ℓ entries in windows −1 through ℓ−1, filtered on entry at zero and counted constant output for ℓ windows; all 13 cases at w=2,3 (2,652 permutation instances) agreed. This is separate from the 1,678 reported frozen checks; the supplied verifier was inspected, not run. For bottom ranks the symmetry is value reversal (negate the inputs), not reversal of time indices.

## originality

PASS

Credit the exact rank-one lifetime and quarter-atom law, and the already indexed all-rank entry probability. The distinct assertion is the full all-width plateau-entry law beyond extremal ranks and its fixed higher-rank survival and endpoint-atom comparison. The strongest bivariate overlap does not encode consecutive persistence once intermediate windows can return to the original output.

## value

PASS

Consecutive exact persistence is a natural stability observable for a sliding rank, distinct from agreement at two times or residual persistence at a random time. The full finite-width distribution and the sharp fixed-rank disappearance of the endpoint atom show why the extremal rule does not characterize nearby ranks. The result is useful at fixed width as well as asymptotically, without assumptions about the continuous marginal law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
