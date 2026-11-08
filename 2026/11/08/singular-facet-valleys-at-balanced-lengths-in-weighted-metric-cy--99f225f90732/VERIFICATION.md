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
The accompanying `cycle_wall_check.py` enumerates edge-difference active-set solutions using exact `fractions.Fraction` arithmetic, reconstructs Lipschitz potentials, and deduplicates vertices without assuming the binomial count. It then checks wall facet counts, active edge counts (facet sizes), and neighboring counts. Its twenty cases cover orders four through eleven, including equal-edge reference cases excluded from the novelty claim. The observed successful output ends with `ALL_WEIGHTED_CYCLE_WALL_TESTS_PASSED 20 critical_cases`.

The proof for all admissible dimensions rests on the parity obstruction, the independence of any \(m\) edge-coordinate constraints in the zero-sum hyperplane, and the explicit neighboring sign counts. Finite enumeration neither proves all dimensions nor supplies an independent mathematical audit.
