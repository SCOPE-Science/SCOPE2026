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

The underlying draws, not the draws conditioned on their stopping count, are independent uniform marks. Independent rate-one Poisson streams give n exp(-tau_n) tending to Exp(1); conditional on the last first-arrival time and its index, there is one compulsory singleton and the other counts are independent positive-truncated Poisson variables. On compact positive windows of n exp(-tau_n), the conditional multinomial variances divided by (log n)^r tend uniformly to n exp(-tau_n)/r!, the scaled off-diagonal terms are O((log n)^((r+s)/2)/n), and the largest centered scaled summand is O((log n)^(-1/2)). The conditional characteristic-function expansion therefore has uniform vanishing remainder, yielding the joint Gaussian mixture when the window restriction is removed. The exact conditional mean minus the Poisson center is the singleton correction plus (n exp(-tau_n)-1)q_r(tau_n), negligible on every claimed scale. The independent rate-n clock has squared error H_n/n; the derivative of the center is O_p((log n)^r), so replacing tau_n by W_n/n incurs o_p((log n)^(r/2)) for fixed r. Exponential integration produces the stated characteristic function. For R>=2, distinct squares have positive covariance 1/(r!s!), although conditional coordinates are independent; for R=1 the dependence remark is vacuous. The frozen finite checker was inspected, not executed, and is not used as a proof of the limit.

## originality

FAIL

Distinct indexed record 0d3ee5e36129 already states the joint observed-time-centered mixed-Gaussian limit for all fixed finite vectors of cumulative low-frequency counts. Differencing and the successive log scales give the exact-frequency limit, with the same mixing variable and observable centering to the required precision. Integrating the Gaussian mixture gives the Laplace formula without additional asymptotics. The academic first-order and deterministic-time results alone would not support a coverage verdict.

## value

FAIL

The second-order fluctuation question is substantive and the accessible Laplace description has explanatory merit, but the submitted theorem adds no new limit or parameter regime to the indexed cumulative result. Finite differencing at separated logarithmic scales and the exponential transform give the entire description routinely. The frozen claim does not supply a new quantitative error bound, uniformity regime, or different occupancy phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
