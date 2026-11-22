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

The attached `verify.py` checks the complete facet tables through exact symbolic determinants and root counts on the full open parameter interval, confirms origin containment, derives all squared facet distances, and checks the rational inequality factors and transition parameter. Execute with Python 3 and SymPy: `python3 verify.py`. It prints `VERIFY_OK` on success. This is an exact finite symbolic check of analytic inequalities, not a sampling proof or an independent audit.

The claim assumes the explicitly specified nine points, one deleted vertex, and the open triaugmented-prism chamber. Its adversarial one-erasure minimax conclusion is relative to that family. Publication priority and independent correctness review remain open.
