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

# Verification record

The standalone `verify.py` was executed with Python 3, SymPy and NumPy. It checks six symbolic critical-curve identities, three exact-rational renewal/mass-propagation cases, and two numerical long-time survival trajectories. The last reported output was:

```text
uniform_eps 0.5 asymptotic_ratios [(100, 0.904994569456295), (200, 0.9464910501315671), (750, 0.9840968315828418)]
uniform_eps 0.8 asymptotic_ratios [(100, 0.9619515003262962), (200, 0.9799913524860555), (280, 0.9854856683771888)]
VERIFY_OK symbolic_critical_identities=6 exact_renewal_cases=3 floating_mass_cases=2
```

The numerical survivor propagation truncates extremely remote geometric re-injection states; this cannot alter exact first-return coefficients within the checked time horizon but does limit the precision of long-time numerical ratios. Exact rational checks and symbolic differentiation are distinct from a proof for every iteration. The all-time conclusion rests on the explicit generating-function identities and complex singularity transfer in `RESULT.md`.

No independent audit or external verification is asserted.
