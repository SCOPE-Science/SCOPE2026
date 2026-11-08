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

The analytic computation is reproduced in `RESULT.md`. In the standard coordinate metric the full covariance has two contrast eigenspaces and one two-dimensional block. Both extreme eigenvalues lie in the two-dimensional block, so trace squared divided by determinant determines the condition number.

Running `python artifacts/verify.py` with a current Python interpreter requires no third-party libraries. It checks 879 enumerated binary vertices, 2315 individual rational covariance entries, 1170 further parameter profiles, and representative exact comparison identities, including the integer equalities at \((p,q)=(2,3),(6,4),(52,7)\). Expected terminal marker: `SPLIT_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED`.

An independent small-dimensional check, `python artifacts/verify_triangulation.py`, uses NumPy, SciPy, and SymPy. It triangulates four polytopes and calculates all polynomial moments from exact determinant-weighted simplex integrals. This checks volume covariance without invoking the beta-mixture derivation. Results are displayed for \((p,q)=(2,2),(2,3),(3,2),(3,3)\).

Finite computations corroborate, but do not establish, the cubic's all-parameter root count or exponential threshold limits. Those depend on the explicit sign inequalities and asymptotic calculations in the proof. Historical priority of equivalent statistical or polyhedral formulations is not independently validated.
