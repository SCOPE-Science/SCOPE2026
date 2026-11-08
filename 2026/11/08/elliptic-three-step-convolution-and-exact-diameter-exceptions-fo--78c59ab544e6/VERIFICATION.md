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

# Verification procedure

Run `python3 check_hyperbola.py` in the same directory as the embedded standalone file. No dependencies beyond Python's standard library are required. The test constructs finite fields by explicit prime or quotient-polynomial arithmetic, enumerates all ordered two- and three-step sums, computes independent character-sum formula predictions, and searches all reachable layers for graph diameter. Tested orders: \(3,5,7,9,11,13,17,19,25,27\). The expected success marker is `SPLIT_HYPERBOLA_THREE_STEP_CHECKS_PASS`.

The precise infinite-field proof is the algebraic reduction and Hasse bound in RESULT.md; passing finite tests alone does not certify that general implication. A previous literature search does not prove priority and external independent review is not claimed.
