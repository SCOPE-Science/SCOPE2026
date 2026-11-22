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

Exact mathematical check: run `python verify.py` with SymPy available. It builds the symbolic tilted three-state matrix independently from the exclusion transition rule; compares its characteristic polynomial to the displayed analytic cubic; substitutes simultaneous bias/counting reversal; and reproduces the numeric-site-rate current derivative exactly. These are symbolic equalities, not statistical experiments. The Perron–Frobenius identification and differentiation at the counting origin are justified analytically in RESULT.md. Only large-time cumulants and rate functions are asserted. The associated 2025 exclusion-process paper was examined for its model, symmetry analysis, and nonlinear-response discussion. Independent audit has not been performed.
