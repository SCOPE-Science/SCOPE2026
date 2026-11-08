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

Run `python3 artifacts/verify_cartier.py` from the package root. This standard-library script independently forms the Kummer polynomial, the ten holomorphic differential indices, calculates each Cartier image by GF(2) derivative and square-root operations, and iterates its ten-dimensional matrix. Expected output is stored in `artifacts/verify_output.txt`.

These checks are exact computations; the proof of differential regularity, completeness, and the tame Kummer genus is in RESULT.md. Historical uniqueness and independent expert validation are not established.
