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

# Verification and limits
The proof uses exact inclusion matrices and invariant-subspace blocks. `CHECK.py` recreates the matrix for every integer dimension from four through thirteen and checks the predicted full eigenspectrum within declared numerical tolerances, plus determinant magnitude and inertia. Run `python CHECK.py` with NumPy available. Numerical tests do not replace the exact all-dimension proof, and no independent mathematical audit has been performed. The spectral condition-number statement is an asymptotic law, not a uniform claim for all finite dimensions.
