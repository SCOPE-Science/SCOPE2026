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

# Verification of sharp quasi-triangle modulus

The finite-dimensional theorem and \(\ell_1\) endpoint are proved analytically in RESULT.md. The decisive steps are the polar norm dual ball \(\{z:\|z\|_\infty\le1,\|z\|_1\le t\}\), a feasible equal-tail dual vector, the exact two-summand equality witness, and the infinite-dimensional equality obstruction. The exceptional parameter boundaries \(t\le1\) and \(t\ge d\), the one-dimensional norm case, and real/complex phases were checked.

Run `python check.py` using Python's standard library to reproduce the exact-rational finite diagnostic. Its expected success marker is `QUASINORM_CUBE_CROSSPOLYTOPE_CHECK_OK 88221`. The script samples rational vectors and checks exact extremal ratios in each nonconvex finite-dimensional test. These finite computations are not exhaustive and are not an infinite-dimensional certificate; no empirical assertion is used in the proof.

No independent mathematical audit has been performed. Bibliographic completeness is not certified.
