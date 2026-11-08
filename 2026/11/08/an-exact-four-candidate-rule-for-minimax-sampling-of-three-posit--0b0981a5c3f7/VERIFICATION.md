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

The exact algebraic certificate checker is `verify.py`; run `python3 verify.py` from the extracted package directory. The checker uses Python standard-library rational arithmetic to verify primal and dual semidefinite certificates on 1000 strictly positive-definite rational correlation triples and reproduces the two illustrated exact rates and probability vectors. Its expected success message begins `VERIFY_OK`.

The proof of the all-parameter theorem is a semidefinite KKT argument with a complete rank-one/rank-two exhaustion, not a finite computational enumeration. An independent audit has not been performed. Published-priority checking remains qualified by the inaccessible full text of one historical E-optimal-design reference.
