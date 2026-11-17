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

The finite test script `check_binomial_death.py` was executed with ordinary Python 3. It enumerated all nontrivial binary cuts at sizes \(n=2,\ldots,8\) for five rational thinning probabilities, checked rational semigroup matrix multiplication through \(n=13\), and verified the Dobrushin coefficient at \(n=2,\ldots,13\). All assertions passed.

The universal upper bound, small-survival estimate, and all limiting transitions are proved analytically in `RESULT.md`. Exhaustive checks on finitely many dimensions do not certify the unbounded-dimensional cases; a numerical limit is not treated as a proof. The exact norm for arbitrary finite dimension is not asserted.
