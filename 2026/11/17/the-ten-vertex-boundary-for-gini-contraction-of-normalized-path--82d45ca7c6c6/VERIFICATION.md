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

Execute the bundled `check_path_gini.py` using Python 3. The exact rational enumeration includes every proper cut modulo complement for each path size from 2 through 9: 1, 3, 7, 15, 31, 63, 127, and 255 cuts. Every generator derivative is independently recomputed from an explicit rational Euler step before taking the maximum. The expected logarithmic norms are `-2, -1, -1/4, -1/6, -1/9, -1/12, -1/16, 0`.

The script also compares the singleton endpoint-neighbor derivative to the exact formula for dimensions 10 through 100, and tests the positivity of the rigorous Taylor-remainder lower bound at the stated explicit time. These checks confirm selected finite instances of the large-dimensional identity; unrestricted correctness comes from the algebraic proof in RESULT.md. No independent external audit was carried out.
