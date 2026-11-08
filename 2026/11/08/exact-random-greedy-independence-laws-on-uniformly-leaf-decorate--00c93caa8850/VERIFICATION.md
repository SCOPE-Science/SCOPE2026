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

# Verification of the finite-size law

The included `VERIFY.py` needs Python 3 and its standard library only. Run `python3 VERIFY.py` in the directory containing this file. The verified output is `VERIFY_OK 738 exact checks`. The checker derives exact distribution polynomials by a general arbitrary-graph first-available-vertex recursion, independently of the spine first-cell recurrence; it compares them for all test graphs of at most 16 vertices with decoration counts from one to six. It also checks the recurrence, normalization, support, expected cardinality, and maximum-output event for the declared domain, through spine length 17.

The proof, not computation, establishes the recurrence for every natural spine length and decoration count. The asymptotic remainder follows from the stated absolutely convergent exponential-series estimate. There is no claim of an independent external mathematical audit.
