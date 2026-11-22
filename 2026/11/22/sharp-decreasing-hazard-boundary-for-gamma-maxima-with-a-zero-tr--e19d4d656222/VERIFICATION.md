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

Execute `python CHECK.py` in a Python environment with `mpmath` installed. It independently recomputes the gamma survival function, the analytic expression for the logarithmic hazard derivative, and the numerical derivative of the hazard at selected points. It checks the sign-switch examples for \(\alpha=1/2\) above the boundary and the increasing examples for shapes at least one. It also numerically minimizes the positive scalar threshold at \(\alpha=1/2\) on a wide finite interval. These checks support algebraic debugging and demonstrate particular signs; they are **not** a certified global minimization or a proof of infinite-domain monotonicity.

The global result is established by the integral representation, strict monotonicity of \(V\), endpoint expansions, compactness of a sublevel set and the exact pointwise sign identity in `RESULT.md`. The independent audit channel has not been performed.
