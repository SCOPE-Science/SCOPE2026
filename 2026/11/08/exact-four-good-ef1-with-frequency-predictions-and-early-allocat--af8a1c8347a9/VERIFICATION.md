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

# Exact checks

The accompanying programs independently evaluate the finite four-rank game whose equivalence to the numerical claim is proved in `RESULT.md`. The C++ program checks all ordered-pair EF1 inequalities with rank values \(1,2,3,4\); the Python program separately uses the singleton-versus-double rank comparison. Both check the unrestricted win, first-two-distinct win, first-two-together loss, and first-three-distinct loss. The Python program also checks every branch and terminal of both explicit adversarial witness trees.

Execution commands and outputs are given in `RESULT.md` and `EXACT_CHECKS.txt`; every source program and the witness data are embedded alongside this document. The software proves only the finite minimax statements; transfer to arbitrary positive predictions, tie cases, and the implications for EF1 rely on the mathematical proof. No independent external audit is claimed.
