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
# Reproducibility and limits

Run `python3 verify_path2.py` with the Python 3 standard library. The exact-order checker enumerates all 120+720+5040+40320+362880 = 409080 local rank permutations and independently traverses all 120+720+5040+40320 = 46200 global rank permutations for n=5,6,7,8. It asserts all stated rational covariance values, the positive long-run radial variance 4352/1575, and the exact finite-sample inertia formula. Each local enumeration exhausts an entire finite event space with equal-probability orderings; the unrestricted theorem also needs the mathematical locality reduction and Lindeberg blocking proof in RESULT.md.

The uniform-direction exposure measure is not uniform over vertices or polytope interior volume. Neither this arithmetic replay nor the self-review is an independent mathematical audit. Historical priority is provisional.
