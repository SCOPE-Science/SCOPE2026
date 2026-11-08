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

The proof uses the exact finite-group weight congruences, which are sufficient to establish lower bounds at every total degree and every cyclic order. The explicit degree-N and degree-2m invariants supply the upper bounds. The included CHECK.py uses only the Python standard library; running `python CHECK.py` prints `PASS 3016 assertion groups; finite checks do not replace general proof`. Finite checks include independent enumeration of allowed monomial weights for N from 2 to 16 and direct invariance tests for N up to 28. They are not a replacement for the general proof and do not constitute independent auditing.
