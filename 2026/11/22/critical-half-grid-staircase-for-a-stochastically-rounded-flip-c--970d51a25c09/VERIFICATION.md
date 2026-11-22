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

The proof is analytic and covers every fixed real detuning. Exact rational arithmetic checks are performed with `python3 check.py`; the successful check compares finite transition matrices with detailed-balance products and tests exact finite stationary means and special values. Finite examples do not certify a parameter-uniform infinite limit; that follows from the fixed invariant core and the two-step generator proof in `RESULT.md`.

An independent mathematical audit has not been performed. Historical priority beyond inspected public sources has not been independently certified.
