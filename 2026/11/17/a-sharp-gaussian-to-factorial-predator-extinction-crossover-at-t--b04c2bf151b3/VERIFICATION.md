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

# Verification notes

Run `python check.py` with Python 3 (standard library only). This evaluates two strictly forward-positive example trajectories and tests convergence of the constant normalizations. The program produces diagnostics, not a proof of an infinite statement. The mathematical verification consists of forward positivity on a nonempty open set, convergent product formulas in the subcritical regime, a critical reciprocal-prey increment expansion, and the summability of the Gamma/log-squared predator normalization. All limiting statements are proved in `RESULT.md`.

Numerical diagnostics at four finite indices do not certify error bounds for arbitrary trajectories. The result makes no claim for nonpositive iterates. Independent audit has not been performed.
