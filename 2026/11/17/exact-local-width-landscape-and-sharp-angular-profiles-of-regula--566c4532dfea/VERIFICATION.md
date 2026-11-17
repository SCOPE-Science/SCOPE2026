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

The analytical proof in `RESULT.md` handles every integer \(N\ge3\) and every real \(0<\theta<\arctan(w_{N,t}/\sqrt2)\). Critical derivations are the exact variance perturbation identity, the uniform cross-block angle condition, and the sharp zero-sum block inequality with equality vectors.

Run `python3 check_width_landscape.py` with Python 3 standard library. This replay performs the finite exact-integer inequality tests, combinatorial checks, and deterministic floating-point geodesic comparisons described under Verification in the result. Replayed output:

`SIMPLEX_WIDTH_LANDSCAPE_CHECKS_PASSED dimensions=15 orbit_ranks=135 exact_inequalities=10797 sharp_geodesics=135 angular_tests=5400`

Numerical comparisons check finite cases and do not certify universal claims. The all-dimensional result rests on the explicit proof. Historical priority is provisional; no independent audit or external certification has been performed.
