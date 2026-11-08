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

# Verification record

The included `checker.py` was executed against the finite examples in its main function. For each checked model it enumerates every possible set of directed cross-color arrows, computes the exact one-step target-type support condition, and cross-checks the product census. It computes three-valued atoms, negation, weak conjunction, belief and nested belief formulas directly on all nonempty faces; same-signature faces agree in every sampled formula whenever support uniformity holds, and each specified target-type diamond formula detects the existence of a matching neighbor at a singleton face. The checker independently sums Bernoulli weights exactly as rational numbers at probabilities \(1/3\), \(1/2\) and \(2/3\), agreeing with the product formula. Its success marker is `ALL_CHECKS_OK`.

The proof, not the finite checker, verifies all modal depths, arbitrary finite colored vertex sets, and the two limiting random thresholds. Generality requires cup completeness, the stated three-valued semantics, type-defining atomic literals, and independent directed arrows in the probabilistic model. Historical priority and any external or independent review have not been established.
