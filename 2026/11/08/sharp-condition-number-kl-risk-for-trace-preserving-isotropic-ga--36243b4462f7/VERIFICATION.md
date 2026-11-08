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

In a clean directory, run `python3 verify.py`. The checker uses the Python standard library only. It returned:

`VERIFY_OK {'exact_identity': 385, 'vertex_enumeration': 3048, 'random_matrix_spectra': 18900, 'derivative_sign': 14000, 'continuous_critical': 180, 'large_contrast': 16}`

The exact rational identity tests the KL product-of-means expression at every tested endpoint multiplicity. The interior and derivative tests are numerical diagnostics; they neither replace the analytic proof nor prove global optimality, uniqueness, or asymptotics. The full universal proof is in RESULT.md. There is no numerical claim about a particular Lanczos simulation. The orientation of KL, trace normalization, finite dimension, and condition-number scope must be kept intact. Independent audit has not been performed.
