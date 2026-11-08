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

## Reproducibility

Run `python3 CHECK.py` from the directory holding the accompanying source. The checker uses only the Python 3 standard library and prints `VERIFY_OK 855 exact assertions` upon success. It enumerates all final permutations for five nonnegative displacement kernels through eight cars and directly simulates all preference lists through five cars; it also verifies recurrence values through sixteen cars and the unit-interval ordered-Bell specialization.

## Limits

Finite enumeration is not a proof for arbitrary car counts or arbitrary real-valued kernels; the general proof uses fixed-outcome factorization, maximum-label decomposition and an alternating subset identity. The historical-priority comparison covers named sources and related exact outcome-distribution results but does not establish absolute uniqueness. Independent audit has not been performed.
