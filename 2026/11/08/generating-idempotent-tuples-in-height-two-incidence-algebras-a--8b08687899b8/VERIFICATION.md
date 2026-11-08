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

# Verification
The standalone `verify.py` program tests the ORIGINAL multiplication and idempotency equations in the star incidence algebra, independently computes unital generated-subalgebra dimension by linear closure, and matches the exact coefficient formula for six cases: the field orders are 2 and 3; the leaf counts are one and two; and the tuple lengths are two or three. Additional weighted-codeword calculations verify the closed coefficient formula for \((r,k,q)=(3,4,3)\) and other examples. Exact rational arithmetic checks the leading asymptotic factors for \((q,k)=(2,30)\) and \((3,35)\). Running `python verify.py` ends with `VERIFY_OK`.

The finite checks do not cover composite prime powers, arbitrary heights, or all parameter values. The proof uses field-generic algebraic identities and a generator criterion with its published mathematical proof. No independent audit has been conducted.
