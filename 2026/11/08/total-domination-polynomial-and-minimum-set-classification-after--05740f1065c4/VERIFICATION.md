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

# Reproducibility

Run `python3 verify.py` in the directory containing this document and `verify.py`; only the Python standard library is required.

The verifier constructs the polynomials by an integer recurrence for the labelled graph exponential formula. Separately, it tests all edge subsets of \(K_n-ab\) and checks that every remaining edge has a distinct adjacent selected edge, exactly implementing total domination on its line graph. Every cardinality coefficient agrees for \(4\le n\le7\): the largest case enumerates \(1,048,576\) edge subsets. It further enumerates every candidate of sizes one less than and equal to the proved minimum for \(n=8,9\), and checks the stated tree-classification multiplicities for \(4\le n\le9\).

Observed console markers:

```
FULL_POLYNOMIAL_EXHAUSTIVE_OK 4 32
FULL_POLYNOMIAL_EXHAUSTIVE_OK 5 512
FULL_POLYNOMIAL_EXHAUSTIVE_OK 6 16384
FULL_POLYNOMIAL_EXHAUSTIVE_OK 7 1048576
MINIMUM_EXHAUSTIVE_OK 8 4 90
MINIMUM_EXHAUSTIVE_OK 9 5 1680
CLASSIFICATION_COUNTS_OK n=4..9
VERIFY_OK
```

These are finite corroborations, not an exhaustive test over all graph orders or independent mathematical certification. The arbitrary-order result requires the combinatorial proof in `RESULT.md`. No external source is needed to run the verifier.
