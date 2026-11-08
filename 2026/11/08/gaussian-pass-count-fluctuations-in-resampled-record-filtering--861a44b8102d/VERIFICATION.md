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

Exact rational and enumeration checks: `python3 verify_rds.py`. Execution yielded 146 passed assertions, including enumeration of independent permutations through length seven, and rational transition and potential identities through length thirteen. Finite assertions verify implementation consistency, not the asymptotic limit.

The proof of the limit relies on a positive potential correction with expected total at most \(O(\log n)\), predictable quadratic-variation convergence after a large-state/small-state decomposition, and a fourth-moment Lindeberg bound. The paper source was checked for the resampling model and for its non-resampling theorem, and comparison was made with related record-retention and card-merging models. Independence, authorship, and historical priority are not independently certified.
