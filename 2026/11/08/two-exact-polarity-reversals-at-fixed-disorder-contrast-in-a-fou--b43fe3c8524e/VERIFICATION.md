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

# Reproducible checks

The embedded `verify.py` and `COEFFICIENTS.json` are sufficient to repeat the exact calculation with Python and SymPy. Execute `python verify.py` in their directory. No network, datasets, or Monte Carlo trials are needed. The code uses the full sixteen-state generator and exact polynomial arithmetic: it checks generator conservation, stationary normalization, rational current reconstruction, a coefficient-wise positive denominator, all seventeen exact numerator coefficients, the exceptional-factor identities, a positive translation of one factor, the intermediate-scale negative witness, and exact rational current differences at three scales. The stated arbitrary-real-parameter proof additionally uses elementary inequalities and Descartes' rule, not sampling.

The numeric thresholds are approximations, while the signs and root count are exact analytical conclusions. Independent scientific auditing has not been performed.
