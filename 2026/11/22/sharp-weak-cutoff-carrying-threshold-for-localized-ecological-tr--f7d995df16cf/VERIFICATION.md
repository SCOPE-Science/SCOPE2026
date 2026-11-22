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

# Reproduction and limits

`verify.py` integrates the two exact mechanical-potential mass expressions using an endpoint-regularizing substitution, numerically maximizes the associated competition coefficient, and verifies its square-root diffusivity scaling. The script prints the limiting theoretical coefficient and sample numerical approaches at decreasing cutoffs. It also compares exact-quadrature masses with the analytic leading term at several fixed effective mortality values.

These numerical experiments support the calculation but are **not** certificates of uniformity, uniqueness, or a global maximum. The proof uses compact-uniform turning-point asymptotics and two analytic inequalities which exclude endpoint escape. The model is a deterministic sharp-cutoff population equation; no independent review or stochastic translation is claimed.
