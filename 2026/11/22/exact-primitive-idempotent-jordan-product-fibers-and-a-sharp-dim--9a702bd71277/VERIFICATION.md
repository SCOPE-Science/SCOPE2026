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

Run `python verify_idempotent_products.py` with Python 3. The standalone checker builds norm-one vectors and directly multiplies each ordered pair of primitive idempotents without using the proof's orthogonal-hyperplane parametrization. It checks every target against the closed expression, including zeros, and records the supported vector outputs and number of distinct nonzero fibers. See `idempotent_output.txt` for the complete results in \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\) and \(\mathbb F_9\). The extension field is implemented directly and no third-party packages are required. This is finite corroboration, not all-dimensional proof or an independent mathematical audit.
