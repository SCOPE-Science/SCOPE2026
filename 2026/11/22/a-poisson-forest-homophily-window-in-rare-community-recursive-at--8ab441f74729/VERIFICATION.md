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

Conditioning on the birth word makes the endpoint selections independent and fixes the population counts. At the ith A birth the A-weight subtotal is (1-q_A)(r+i-1) while B contributes q_A(b+j_i-i); this gives the stated kernel including both endpoints (for escape, the B weight diverges uniformly off time zero). Conditional on K_n≤M and all A arrivals after εn, each B selection has mark probabilities a/(j+O_M(1)); the square-sum error of the multivariate generating function is O(1/n) and the means tend to a log(1/U_i). The A-parent decisions use disjoint trials. The founder indicator covariance sums are bounded off the diagonal, the diagonal sums are β_v log n+O_M(1), and bounded increments give the standardized multivariate Lindeberg limit. For fixed ε, omitted late founder terms have bounded variance and mean discrepancy O_M(1+log(1/ε)); the early truncated CLT is uniform conditionally and uses no trials determining any A marks on the cutoff event. Removing the cutoffs costs only the tight-count tail and at most cε (an arrival at the upper boundary has probability O(1/n)). At escape no A child remains, and integrating the conditional Poisson marks over uniform birth time gives c a^(k-1)/(1+a)^k by an elementary Gamma integral; the independent count laws follow by thinning.

## originality

PASS

The soft attachment rule, Poisson marking and the mechanism behind fixed-vertex logarithmic Gaussian fluctuations are not novel by themselves. The contribution is the critical two-parameter specialization as a joint finite forest with explicit conditional child marks and an independent founder vector, not a fixed-proportion degree law. No covering statement was established in the examined material.

## value

PASS

A tight community is essentially lost to an empirical degree histogram. Its entire ancestry, including the age-dependent inverse-size escape transition, and its degree marks give a precise alternative invariant. The independent founder fluctuations explain which large-degree effects do not track that ancestry, and the escape endpoint supplies a usable degree-class benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
