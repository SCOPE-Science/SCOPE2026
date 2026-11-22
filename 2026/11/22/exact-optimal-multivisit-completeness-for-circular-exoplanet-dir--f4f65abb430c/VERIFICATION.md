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

# Verification details

The checker `checker.py` evaluates inclination-integrated circular-arc coverage independently of the closed form, then compares it with the formula over five visit counts and eight visibility thresholds. It tests randomized competing visit schedules, perturbed evenly spaced schedules, the exact complete-coverage plateau, and the near-threshold asymptotic ratio. An actual local execution completed 577 assertions and reported PASS.

A finite numerical checker does not prove uniqueness, integral evaluation, all-parameter inequalities, or historical novelty. The proof in RESULT.md derives these analytically. The model omits flux/contrast, noise, orbital eccentricity, target uncertainty, multi-object scheduling, and confirmation requirements. The results have undergone self-review only; no independent audit or validation is asserted.
