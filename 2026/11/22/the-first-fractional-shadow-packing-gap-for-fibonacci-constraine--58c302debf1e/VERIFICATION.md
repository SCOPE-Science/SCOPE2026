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

# Verification protocol

Execute `python verify.py` (Python 3.9 or newer; no third-party dependencies). The program derives every permitted source and read word directly from definitions, checks all seven witness codebooks and six short dual covers, verifies the seventh-length rational primal and dual weights, confirms all eight confusability cliques cover all 34 inputs, and exhaustively computes the integer optimum and optimizer multiplicity by a complete bitmask recurrence. Its expected outcome is `PASS`, integer optima `[1, 1, 2, 3, 4, 6, 8]`, LP optima `[1, 1, 2, 3, 4, 6, 9]`, and ten length-seven maximizing codebooks.

The claim is for all and only lengths one to seven. The complete finite verification is a proof because each enumeration is exhaustive and independently justified in the mathematical argument. It does not certify any statement for longer lengths. Independently audited verification has not been performed.
