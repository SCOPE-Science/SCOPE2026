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

Run `python3 check_angles.py` using Python's standard library. It independently enumerates all objective-coordinate permutations for ten pairs \((r,s)\), checks their induced orientation histogram against the factorial-angle formula and verifies \(t=2,3,4\) collision expressions. Four \(K_{2,s}\) comparisons check the exact single-edge correction. Expected marker: `SPLIT_ANGULAR_CONE_EXACT_PASS cases=10`.

The asymptotic coefficient, Dirichlet limit, multinomial law and collision condensation are proved by direct counting and a factorial-composition lemma in `RESULT.md`; the enumerations do not establish those infinite claims. Checks assume exact integer arithmetic and no external numerical data.
