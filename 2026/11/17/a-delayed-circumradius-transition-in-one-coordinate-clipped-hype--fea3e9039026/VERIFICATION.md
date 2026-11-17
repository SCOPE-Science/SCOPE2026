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

# Verification of the clipped-hypersimplex minimum enclosing ball

The symbolic proof in RESULT.md is universal over integers \(m\ge2\), \(1\le k<m\), and real \(0<t<1\). Its nonstandard steps are the complete vertex-orbit classification, the exact orbit-distance difference, and the global minimization of the envelope of two quadratics. Each is proved directly rather than inferred from computation.

Execute `python3 check_capped_hypersimplex_ball.py` with Python 3 standard library only. The program independently enumerates every vertex of each test polytope by setting all but one box coordinate to an endpoint, solves the resulting exact rational equality, deduplicates candidates, and then minimizes the squared-distance envelope by checking its stationary points and crossing points. It checks the predicted radius and center, contact multiplicities, radial slack, and barycentric optimality certificate.

Exact successful output:

`CAPPED_HYPERSIMPLEX_BALL_CHECKS_PASSED cases=308 enumerated_vertices=24761 contact_vertices=16802 screened_cases=146 boundary_cases=16 full_contact_cases=146`

The enumerated range is \(2\le m\le8\), all \(1\le k<m\), at eleven exact rational values of \(t\). These tests are not an exhaustive search over real \(t\), and no computational result alone proves the infinite statement. Historical originality remains provisional. No independent audit was performed.
