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

# Reproduction and boundaries

Run `python3 verify.py` using only the standard Python library. `verification_output.txt` contains an execution of the bundled code; the proof in `RESULT.md` is self-contained apart from a finite, completely enumerated arity-four sign test, for which the code is provided. The checker reconstructs the three cubic rewrite rules from scratch and evaluates 120 arity-four and 1680 arity-five formal monomials. In the explicit example, it checks all ordered triples of the 15-dimensional base and 30-dimensional cotangent extension with exact integer coefficients, nonzero quartic product, and a distinction from a related symmetric-metric identity. All assertions were executed successfully from this package. The check is not an independent mathematical audit, is not an external certification, and does not investigate characteristic two or minimal example dimension.
