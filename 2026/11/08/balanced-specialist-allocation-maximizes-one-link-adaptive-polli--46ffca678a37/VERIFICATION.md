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

# Reproducibility and limits

Run `python checker.py` using Python 3 with only the standard library. The script enumerates each surviving pollinator subset and tests actual injective assignments of three survivors to the three plants, counting whether at most one new edge is required; this procedure does not use the theorem's event characterization. Independently it evaluates the exact binomial formula and compares every positive ordered class composition with the balanced allocation for \(3\le n\le9\), \(p\in\{1/4,1/2,3/4\}\). All probabilities are exact rational numbers.

The observed output was: `PASS 252 exact matching-enumeration identities; 252 balancing comparisons`.

The computation is finite corroboration only. The universal claim is proved by the explicit event equivalence, disjoint failure cases, positive second forward difference and balancing transfers in `RESULT.md`. No stochastic population dynamics, dependent survival, exclusive rewiring, or empirical performance are checked.
