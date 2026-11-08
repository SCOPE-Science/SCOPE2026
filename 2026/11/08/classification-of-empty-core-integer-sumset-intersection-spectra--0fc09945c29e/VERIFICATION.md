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

# Verification scope
Run `python3 VERIFY.py` from a directory containing the embedded standalone verifier. It uses integer arithmetic and exhaustive enumeration of finite truncations for generating sets \(\{3\}\), \(\{3,5\}\), \(\{4,7\}\), and \(\{3,4,7\}\). It checks 38 length/case combinations in total and independently computes semigroup membership by dynamic programming.

The implementation directly constructs finitely many positive and negative integer generators from the explicit scale recurrence, then enumerates unordered tuples of exactly \(h\) elements and checks whether zero is attained. Exact agreement with the additive-monoid criterion confirms finite instances of the central lemma.

The infinite classification does **not** follow from these finite experiments. It follows from the modular least-index divisibility proof and the converse generator construction given in `RESULT.md`. Unindexed historical priority is a residual risk; independent mathematical validation has not been performed.
