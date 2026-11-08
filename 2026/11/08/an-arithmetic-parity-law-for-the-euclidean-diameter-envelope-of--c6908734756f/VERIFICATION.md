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

# Verification of the Euclidean diameter envelope

Run the self-contained Python 3 file `verify.py` with `python3 verify.py`. It uses only standard-library integer and rational arithmetic and has no network or third-party dependencies. The execution completed with

```
EXACT_PASS instances= 240 pairs= 46920 sparse_subsets= 736 integer_lemma_cases= 14240 real_perturbations= 120
```

For each integer \(2\le d\le16\) and \(1\le m\le16\), it computes all unordered pairwise squared distances on the complete integer moment curve, checks the applicable formula, and verifies that the *full set* of equality pairs is exactly the predicted set. It checks 736 generated sparse subsets for the conditional equality criterion, 14,240 instances of the critical integer-pair inequality (including equality classification), and 120 rational counterchecks showing that the integer-scale envelope does not carry over to arbitrary real parameters in even dimension.

The source `RESULT.md` contains an all-parameter proof, with a separate integer separation estimate in the even-dimensional case. Finite tests do not establish the bound or uniqueness for untested dimensions and scales; that conclusion relies on the proof. No external independent mathematical validation has been performed.
