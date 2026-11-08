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

# Reproducible checks and their scope

Run `python3 check_jets.py` with Python 3.9 or later. This standalone standard-library program checks exact rational polynomial identities at truncation lengths \(1\le L\le15\), using five deterministic examples per length. It verifies isotropy, the six pairings, recoverability of the chart parameters, and the lower-bound parameter counts. Expected final line: `ALL_EXACT_POLYNOMIAL_CHECKS_PASS`.

The all-length proof uses the injective algebraic parameter family in RESULT.md and the published bound \(\dim J_L(X_{3,4})\le13L/2\); it is not based on extrapolation from code. No exhaustive computer classification of jet components, independent audit, or claims about arbitrary coefficient fibers are implied.
