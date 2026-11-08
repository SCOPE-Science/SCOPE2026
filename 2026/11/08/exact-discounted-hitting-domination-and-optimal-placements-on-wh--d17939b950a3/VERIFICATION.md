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

The accompanying `verify.py` constructs the adjacency matrix of each wheel and solves, independently of the closed formula, the linear equilibrium equations with every chosen source pinned at one. It exhausts every nonempty source set for \(4\le n\le8\) and \(\lambda\in\{1/5,1/2,4/5\}\), comparing the directly computed worst support to the gap formula to absolute tolerance \(10^{-10}\). It then checks all fixed-cardinality maximin scores and exact counts of maximizers by explicit enumeration, and validates the \((n,\lambda,\tau)=(4,1/2,1/3)\) exceptional case using rational arithmetic.

Command: `python3 verify.py` (Python 3, NumPy).

```text
DIRECT_EQUILIBRIUM_OK 2961 source_sets
BALANCED_MAXIMIN_AND_OPTIMIZER_COUNTS_OK 105 cardinality_cases
EXACT_HUB_FREE_OPTIMUM_OK 2 configurations
VERIFY_OK
```

These finite checks are corroborating evidence only. The unrestricted correctness claim is supported by the explicit gap recurrence, the hub self-consistency equation, strict gap-sum concavity and cyclic-composition counting in `RESULT.md`. No independent mathematical audit has been performed; equivalence to any unindexed prior statement is not ruled out.
