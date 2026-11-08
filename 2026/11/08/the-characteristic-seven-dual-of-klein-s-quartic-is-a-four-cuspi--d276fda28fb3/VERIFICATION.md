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

# Reproducibility
Run `python3 verify_klein7_dual.py` with SymPy. Its polynomial identities, determinant witnesses, and local formal jets are exact computations over the seven-element field. The saved output is `verify_results.txt`.

The global implications are justified in `RESULT.md`: basepoint-free degree arguments prove birational normalization and the full dual equation; local two-generator cusp analysis and the arithmetic genus prove the complete singularity basket. No claim of independent external validation or of complete historical priority has been made.
