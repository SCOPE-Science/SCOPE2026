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

Run `python verify.py` with Python 3 (standard library only). The program builds the complete face sets by checking every subset against all independent four-subsets, reconstructs the specified matching orders, and checks acyclicity using a complete directed Hasse graph topological sort. It confirms the critical-cell profile for both rectangles. See `verification_output.txt` for actual recorded results.

The independent bipartition size bound proves dimension at most five. Exhaustive matching verifies the integral homotopy conclusions for the two finite complexes. The code does not check any other grid width, is not an infinite proof, and does not independently verify literature novelty.
