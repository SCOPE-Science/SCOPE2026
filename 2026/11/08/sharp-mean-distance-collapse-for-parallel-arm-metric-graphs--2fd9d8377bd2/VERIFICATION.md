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

# Verification

The analytical proof applies to every positive arm vector with at least four arms, without sampling assumptions beyond independent arclength-uniform points. The critical steps are the same-edge and different-edge integrals, strict balancing at fixed minimum and sum, derivative factorization, and the compactification/unique-limit argument. The only nonattained endpoint is handled as a limit, not identified as an admissible graph.

Reproduction: install `numpy>=1.24`, and execute `python code/check_mean_distance.py` from the document root. It checks eight lengths configurations by direct shortest-path quadrature, including unbalanced graphs and ties, and independently tests 2,000 random choices for each arm number from three through nine. Successful execution prints `BANANA_METRIC_MEAN_QUADRATURE_AND_BOUNDARY_TESTS_OK`. Numerical integration accuracy is finite and is not evidence of an infinite proof. The m=3 case is compared only to clarify the sharp change at four arms. No independent audit or validation has been performed.
