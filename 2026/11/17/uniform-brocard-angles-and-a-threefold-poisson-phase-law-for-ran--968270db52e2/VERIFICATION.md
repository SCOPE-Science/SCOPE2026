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

The mathematical proof uses the exact uniform-angle simplex, the circle parameterization of cotangents, the resulting Jacobian, an explicit cubic identity, and a standard evaluated trigonometric integral. All are derived in `RESULT.md`.

Run `python check_brocard.py` to reproduce standard-library numerical checks: five phase normalizations, several trigonometric identities, a Poisson-kernel comparison, and an independent 300,000-sample direct Euclidean circle simulation. Successful execution prints `BROCARD_UNIFORM_PHASE_CHECKS_OK`. Empirical checks are not used as a substitute for the proof.

The 2011 primary mathematical text was read for its Brocard/cone and Ceva classification; the 2015 random-triangle text was read for its uniform-angle/Gaussian distinction; relevant published fixed-Brocard-angle shape inequalities were compared in full. The literature search is not an exhaustive historical certification, and no independent mathematical validation is represented.
