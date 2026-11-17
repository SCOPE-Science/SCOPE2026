---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n>=3, theta>0, ordinary Ewens fixed-point/descent covariances are covered by earlier result. The new comparison W=1{pi(n)>pi(1)} has marginal w_n=[binom(n,2)+2(n-1)(theta-1)+(theta-1)²]/[(n+theta-1)(n+theta-2)], with doubly fixed arrow correction. Conditioned on a fixed label, its probability is 1 at either endpoint, w_{n-1} otherwise. Thus Cov(F,W)=p_n[2+(n-2)w_{n-1}-nw_n], which added to known ordinary covariance factors as -n theta(n-2)(theta-1)(n+2theta-3)/[(n+theta-3)(n+theta-2)(n+theta-1)²]. All denominator factors positive; sign is sign(1-theta), including theta=1 zero without independence. Independent exact permutation sums n3..6 at theta 1/2,1,2,3 matched.

## originality

PASS

Best-of-knowledge after actual Resultary searches and material full published-source reading: The November 8 locality theorem proves the full ordinary covariance matrix for all theta and the October 26 theorem covers ordinary aggregates; the surviving circular comparison W is not among ordinary descent columns. Uniform theta=1 cyclic cancellation is earlier. Explicit new w_n endpoint correction is required for all-parameter circular sign formula. ['Same-day originality of the theta!=1 circular law may be affected by additional equivalent Ewens boundary-statistics studies. No claim of independent total-count random variables at theta=1.']

## value

PASS

The cyclic boundary observable is distinct from ordinary descents; its exact covariance sign reversal at theta=1 reveals a universal change from positive to negative dependence under cycle bias for all finite sizes. It is a motivated exact new dependence law beyond the known ordinary covariance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
