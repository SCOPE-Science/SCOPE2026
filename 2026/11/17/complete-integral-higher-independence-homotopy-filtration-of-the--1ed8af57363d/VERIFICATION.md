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

Run `python3 verify.py` with a standard Python 3 installation and compare the entire output with `verification_output.txt`. The program enumerates all 32768 masks, constructs complete induced components, pairs all available faces using one fixed order per threshold, and builds the full directed Morse Hasse graph. Kahn's traversal visits all nodes at each threshold; every computed critical dimension, matching cardinality, and reduced Euler characteristic is asserted. Every threshold 1 through 15 is proved exhaustively. The result is a finite homotopy classification; the code does not claim any infinite-tree extension or independently performed audit.
