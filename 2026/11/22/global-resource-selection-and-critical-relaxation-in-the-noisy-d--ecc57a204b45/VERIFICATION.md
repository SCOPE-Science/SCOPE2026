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

# Verification of mathematical identities

The accompanying `check.py` is standalone and checks the payoff reduction, interior/boundary roots, the relative-entropy derivative identity and critical-noise algebra with symbolic arithmetic. It performs 18 high-precision illustrative IVP integrations for convergence and coordinate invariance. Exact identities and the analytic compact-set/LaSalle/center-manifold arguments in `RESULT.md`, not trajectory samples, establish the infinite-time claims.

Limitations: the package contains no stochastic-process proof, external validation or original source paper text.
