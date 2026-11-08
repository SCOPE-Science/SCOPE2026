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

# Verification scope

Run `python verify_profile.py` with Python 3 and no external packages. The executable uses exact fractions for support and slice formulas, symmetry, both scale branches, sampled row-covering certificates, and uncovered-hole witnesses. On the recorded run it printed `EXACT_RATIONAL_OK: 12 analytical-branch samples, 120,000 slice point checks, 15,000 independent rational torus points`. The proof in `RESULT.md`, not finite sampling, establishes the exact conclusion for every real parameter. No independent mathematical audit has been performed.
