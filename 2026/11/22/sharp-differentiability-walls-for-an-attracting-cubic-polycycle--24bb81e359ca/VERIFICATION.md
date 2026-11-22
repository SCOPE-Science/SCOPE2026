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

The analytic certificate is the exact integral for the invariant squared radial graph, displayed as equation (4) of `RESULT.md`, together with the exact defect integral (5). Both are derived from the original-time cubic field. The strict positivity of the defect integrand when \(0<\varepsilon<1\) excludes cancellation of the leading power singularity.

Reproduction: install Python 3 with SymPy and mpmath, then run `python3 star_node_cusp_verify.py`. The script verifies the polynomial polar contraction/angular identities, the integrating-factor coefficients and the nonresonant quadratic coefficient, and evaluates representative high-precision integrals at \(\varepsilon=1/2\) for \(\omega=1,1/2,1/4,1/8\). The expected success marker is `STAR_NODE_CUSP_VERIFY_OK`.

The strict \(C^1\) and \(C^2\) classifications follow from the analytic endpoint integral and its differentiated asymptotics, not from the numerical sampling. Their sharpness includes both equality walls; the logarithmic \(C^2\)-failure at \(\omega=(1-\varepsilon)/2\) is an exact, nonzero term. Neither independent mathematical review nor an exhaustive literature priority audit was performed.
