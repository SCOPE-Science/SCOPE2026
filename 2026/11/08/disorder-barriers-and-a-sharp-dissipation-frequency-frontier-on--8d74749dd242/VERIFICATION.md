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

The exact symbolic characteristic-polynomial identity and exceptional-point rank calculations were checked by the standalone `checks/verify.py` using SymPy. The same checker tests an extensive finite grid of rational edge-activity triples and admissible biases against the entropy Jensen inequality and spectral formulas, and tests inverse entropy-budget calculations by bisection.

Command from extracted package root: `python checks/verify.py`.

Observed result: `PASS: 2274 deterministic assertions; 3x3 symbolic identity and Jordan tests verified.`

**Limits:** Finite numerical tests do not prove the universal assertions or originality. Those assertions rely on the explicit analytical determinant, eigenvector argument, convexity and monotonicity proof in `RESULT.md`. No independent audit or external formal certificate has been performed.
