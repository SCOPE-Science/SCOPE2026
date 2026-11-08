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

# Reproduction and limits

Run `python3 check_cycle_learning.py` with the Python standard library. The checker constructs independent-set concepts directly, compares unrestricted trace enumeration with the claimed VC formula for all eligible pairs through length twelve, compares exact finite online dimensions through length ten, checks each explicit shattered-support assignment through length fourteen, and validates the movable threshold blocks for an additional range of parameters.

Output from the executed file:

`FIXED_WEIGHT_CYCLE_LEARNING_PASS 45 32 284 203`

The counts refer respectively to VC parameter checks, online parameter checks, support-label realizations, and movable-block parameter checks. All tests passed. This code checks finite instances only. Unrestricted correctness relies on the edge-parity proof, segment completion lemma, class-size double count, and threshold-block construction in `RESULT.md`. The exact Littlestone dimension at arbitrary finite parameters is not claimed. No independent audit has been performed.
