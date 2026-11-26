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

Use iid continuous priorities; the first pivot in an interval compares the endpoints iff it is one of them. The success probability is 2/u and the variance is 2(u-2)/u². In disjoint intervals the priorities are independent. For strict containment, conditioning on a successful outer minimum removes an outside endpoint without biasing the inner relative order, giving joint probability 4/(uv). In shared-endpoint containment the two possible outer minimizing endpoints give (1+2/s)/ell. For touching intervals the minimizing label must be one of the three endpoints, giving (2/v+1+2/u)/(u+v-1). In a strict interleaving only the two outside endpoints are eligible, giving (2/v+2/u)/t. Subtraction of 4/(uv) yields the displayed exact kernel. For mutual independence, remove an inclusion-minimal interval J from a compatible family. Every remaining interval is disjoint from J or strictly contains it, so their indicator vector is measurable with respect to the numerical minimum inside J and the entire priority vector outside J. Exchangeability makes the minimizing label uniform and independent of that information. Thus I_J is independent of the entire remaining vector, not just each component, and induction gives the product generating function. Conversely, in lengths >=3 all incompatible endpoint cases have strict nonzero covariance. Adjacent ranks are deterministic ones and must not be used in the converse obstruction.

## originality

PASS

The distinct assessed content is the interval-resolved dependence result culminating in a necessary and sufficient condition for mutual independence. The standard priority representation, marginal and variance of total cost are antecedents. In particular, novelty is not inferred merely from known total-variance analyses using different proofs.

## value

PASS

The intervals correspond to natural direct comparisons in a standard randomized algorithm, and the result supplies the exact signed kernel for arbitrary weighted comparison counts. More structurally, it identifies exactly which nonconstant comparison families have a factorized law and proves that no higher-order dependence survives in precisely those families. This is not a recomputation of the known unweighted total variance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
