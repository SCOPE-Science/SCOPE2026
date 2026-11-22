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

The full all-order claims have constructive proofs in `RESULT.md`: bijection with even boundary subsets, necessary and sufficient maximality gap constraints, and exact one-slack exchange classification. Finite tests are independently enumerative checks rather than replacements for these proofs.

The Python 3 standard-library `verify.py` constructs the blob graph of each path directly from all connected intervals, recursively enumerates all pairwise nonadjacent choices, and determines maximality and optima using direct pairwise graph compatibility. It then compares every coefficient of the two stated polynomials and every optimum-exchange edge with formulas derived separately from the interval and omitted-boundary arguments.

Verified command: `python3 verify.py` (from the artifact's own directory). Observed final output:

```
VERIFY_OK exhaustive_independent_sets= 8190  all_structure_tests=PASS
```

Orders \(1\) through \(12\) were checked in full. Nonzero coefficients, root counts and exchanges beyond these orders are established symbolically; no claim of exhaustive computation for all orders is made. Earlier literature may contain equivalent formulations; no independent review has occurred.
