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

Execute `python3 verify.py` with Python 3.9 or newer from the directory containing the script. The program performs an exact finite-state closure check (16 raw states), deterministic minimization (five states), eight transition-potential inequalities, and complete direct shattering checks for lengths 0 through 11; it additionally verifies sharp support constructions for weights 2 through 44. The captured `verification_output.txt` is the actual output from replay. Symbolic elimination of five generating-function equations and the explicit potential inequalities are documented in RESULT.md, which proves the unrestricted-length claim; finite enumerations provide corroboration only. No independent audit is asserted.
