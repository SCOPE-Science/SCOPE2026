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

The proof is fully contained in `RESULT.md` and uses spherical-cap geometry, a rank-two skew map, and elementary Lipschitz estimates. In particular, the infinite-dimensional and arbitrary-metric quantifiers do **not** rest on numerical enumeration.

Run `python3 checker.py` with a standard Python 3 installation. Its deterministic finite diagnostic checks 20,136 conditions across ten tolerances, 20,000 cap-geometry samples, and several planar skew increments. The expected output is `HILBERT_CAP_FINITE_DIAGNOSTIC_OK 20136`. This program is only a computational cross-check; the analytic argument proves the theorem.

The claimed uniform error is a supremum (not necessarily an attained maximizing functional inside the strictly open cap). The skew witness attains the supremum value and the index as defined. In the scalar case the cap includes the unique norming functional and no approximation error occurs. No statement is made for complex targets or for a universal exact index of arbitrary nonisometric references.
