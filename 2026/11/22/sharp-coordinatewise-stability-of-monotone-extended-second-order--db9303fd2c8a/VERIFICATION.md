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
# Verification and limits

Run `python3 checker.py` with NumPy and SciPy available. The checker independently evaluates randomized pairs via a direct nonincreasing PAVA projection, checks that no sampled quotient exceeds the proposed sharp constant, and checks the two analytically constructed near-extremizing derivative configurations; it reports 5,675 successful numerical assertions on the recorded run.

These finite tests neither verify the global infinity-norm inequality for every input nor certify the literature priority claim. The proof in RESULT.md provides the universal bound and sharpness by active-block differentiation, a convex endpoint comparison, and local perturbation limits. The existing Euclidean Lorentz-cone result is the p=1 special case. No separate independent mathematical audit has been performed.
