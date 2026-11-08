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

Run `python3 verify.py` with Python 3 and the standard library only. The local exact-fraction replay reported `exact_grounded_checks 1017`, `exhaustive_subset_checks 1656`, `strict_witnesses 3`, `limit_allocation_checks 930`, and `VERIFY_OK`.

The complete symbolic proof is in `RESULT.md`: two eigenspaces of within-part zero-sum vectors, one two-dimensional block, a balanced endpoint product inequality, and a fixed-parameter asymptotic discrete minimization. The computation checks finite instances only and does not assert exhaustive verification of all network sizes or a simultaneous parameter limit.

The literature comparisons and scientific limits appear in `REVIEW.md` and `AUDIT.json`. Publication priority and independent mathematical validation are not established.
