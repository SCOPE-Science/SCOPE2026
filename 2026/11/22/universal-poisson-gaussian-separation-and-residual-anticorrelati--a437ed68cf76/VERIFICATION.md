---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

Run `python3 verify_subdivision_gas.py` using only Python 3 standard-library modules. The script builds the incidence subdivision explicitly and independently evaluates weighted independent sets, original-subset reductions and exact rational total-variation distances. Expected terminal line: `ALL_NEW_CHECKS_PASSED 590`.

The complete proof for arbitrary order rests on the exact conditional partition identity, a uniformly integrable product-Bernoulli tilt, weak convergence of degree-marked Bernoulli point measures, and a conditional binomial CLT. No finite enumeration is used to assert an infinite-system result. The explicit total-variation bound is valid for every simple host graph, while the point-process and normal limits require the indicated empirical-degree and edge-density hypotheses. Independent audit remains unperformed.
