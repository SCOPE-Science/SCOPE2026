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
# Scientific verification

The proof reconstructs the pure-point reverse-well-order criterion, proves two explicit spectral-gap lemmas, and handles signed compact corrections via finite negative rank. It provides an explicit noncommuting infinite-rank positive example and a trace-class obstruction for infinite negative rank. The analytic proof covers general infinite-dimensional separable Hilbert spaces; no finite computation supplies spectral completeness.

`checker.py` executes independently with Python and NumPy and reports `ONE_SIDED_COMPACT_STABILITY_DIAGNOSTIC_OK 1278` on finite two-by-two and diagonal test families. Its floating-point assertions test the displayed examples and are not an exhaustive or formal verification of the theorem.

The scientific review compares full relevant mathematical source passages and the published prior result statements. Independent mathematical review and publication-priority certification have not been performed.
