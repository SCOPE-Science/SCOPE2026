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

The result is a theorem for stationary size profiles, not a simulation-derived global stability assertion. Its critical steps are: (1) solve the stationary transport equation at fixed total stock; (2) show the recruitment closure is strictly increasing and onto; (3) differentiate the mature-to-total ratio; (4) prove positivity and strict increase of the logarithmic loss function using the monotonicity of \(s/\sinh(s)\); (5) invert the single critical equation and derive the high-stock asymptotic; (6) solve the midpoint condition with the principal Lambert function.

`CHECK.py` is a standalone Python 3 implementation (standard library only), testing direct flux and mature integrals, the root identity, the exact midpoint calibration and 380 representative parameter combinations. Run `python3 CHECK.py`; passing tests are diagnostics, not a substitute for infinite-domain proof. No separate independent scientific audit or external certification is implied.
