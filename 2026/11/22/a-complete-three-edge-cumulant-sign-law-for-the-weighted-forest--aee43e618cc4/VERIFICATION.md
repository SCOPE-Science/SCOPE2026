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

# Reproducibility

Run `python3 verify_theta_cumulants.py` using only the Python 3 standard library. The verifier constructs the generalized theta graph from explicit terminal-to-terminal paths, tests each edge subset's cycle structure with an independent union-find detector, assigns exact rational product-Bernoulli weights, conditions on acyclicity, evaluates every distinct third cumulant directly from first, second and third moments, and compares its exact rational value against the three symbolic formulas. Seven graph/weight cases encompass 420 triples, including two-arm cycles, three-arm theta graphs and four-arm generalizations. Expected final output: `THETA_CUMULANT_EXACT_CHECKS_PASSED 7 420`.

This is a finite test of an independent computation, not a machine proof of the all-length statement. The complete mathematical proof and its strictness conditions appear in RESULT.md. All source files in this package are complete; no prior package is required. The claims of novelty and value are same-model assessments, without independent external validation.
