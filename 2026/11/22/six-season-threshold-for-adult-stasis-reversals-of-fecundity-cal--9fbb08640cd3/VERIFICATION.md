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

# Verification and limits

The analytical proof derives a closed-stage-walk identity for the trace of an arbitrary period product, an order-invariant determinant, monotonicity of the positive Perron eigenvalue in trace, and the six-season factorization. No numerical extrapolation is used to establish an unbounded-period assertion.

Run the self-contained Python 3 script `checker.py`. On the delivered source, it completed with `PASS: 14432 exact-arithmetic diagnostic assertions.` The tests cover every permutation of distinct fertility labels for periods two through six at four rational survival settings, all pairwise sign comparisons for periods through five, the exact six-season switch, three arbitrary adjacent swaps, and two independently scaled survival-threshold witnesses. Reproduction requires only the Python standard library.

The finite checks are diagnostic, not an exhaustive proof for arbitrary positive real parameters or unbounded period. Scientific priority is supported only by the accessed sources specified in RESULT.md and REVIEW.md. The 1977 primary study was not available in full text. Independent audit has not been performed.
