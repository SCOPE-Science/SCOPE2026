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

Reproduce the algebraic and finite numerical diagnostics by running `python check.py` with SymPy, NumPy, and SciPy. The checker verifies the exact center-action identity, the stable-mode matrix identity, and the sign structure of the rectification forcing. It integrates the full four-dimensional ReLU differential equation over one unperturbed period at several positive outer excesses, separately in the single-graze and double-graze cases. Its finite numerical outputs approach the exact analytical leading constants as the excess shrinks.

The \(n^{-2}\) convergence statement is supported by the proof of the return map and invariant cone in `RESULT.md`; numerical integrations do not independently certify the infinite-time theorem. Independent mathematical audit has not been performed.
