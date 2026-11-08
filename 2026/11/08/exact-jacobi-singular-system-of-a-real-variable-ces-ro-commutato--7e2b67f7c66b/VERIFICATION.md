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

The infinite-dimensional theorem follows from a pointwise kernel identity, two complete weighted Jacobi orthonormal bases, and one terminating hypergeometric integral identity proved in RESULT.md. The bundled `check_jacobi_svd.py` is a standalone standard-library checker. Run `python3 check_jacobi_svd.py`; it confirms 44 exact rational integral identities and 392 exact rational orthogonality identities, all without floating-point arithmetic. A separate finite telescoping check is included. The test covers finitely many degrees only, and does not certify all-degree or infinite-dimensional conclusions. Publication priority and independent mathematical review are not established.
