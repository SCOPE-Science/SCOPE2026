---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I reconstructed the entropy derivative for arbitrary s,m rather than extrapolating the finite checker. In normalized shared and local concentrations u,v and stationary ratio t=T*/R*, the local consumer growth term cancels the current-biomass part of local uptake. Combining the remaining terms with the equilibrium supply offset leaves, per exchange pair after division by beta R*, the expression (1-1/u)(1-t-u+tv)+(1-1/v)(u-tv)-(1-t)(v-1). It is affine in t: at t=1 it is -(u-v)^2/(uv), and at t=0 it is 3-1/u-u/v-v=-P/(uv). The three positive terms 1/u,u/v,v have product one and are all one only at u=v=1. Direct consumption and the shared loss produce the stated shared square. Strict positive isolation (including theta_i=1) gives 0<t<1; the zero-dissipation set thus fixes all nutrients, and requiring invariance fixes every biomass from the local balance. Entropy sublevels are compact in the positive orthant, so continuation and LaSalle prove convergence and the equality set proves uniqueness. For hyperbolicity, the quadratic part of P is (du)^2-du dv+(dv)^2, and the positive entropy Hessian gives a nonpositive quadratic dissipation with kernel exactly the biomass subspace. In the Hermitian form, any eigenvector with nonnegative real part must be in that kernel, but the biomass-to-local-nutrient Jacobian is injective there. This proves strictly negative real parts and local exponential attraction, not a uniform global rate. The proof assumes a positive equilibrium exists, not that one always does. RESULT.md, VERIFICATION.md and verify_global.py were inspected without executing the supplied code; its rational 3-by-2 example does not prove the all-size identity or hyperbolicity.

## originality

PASS

The uptake mechanism and certain stationary and dynamical special cases are prior coverage. The supported distinction is the conditional global rigidity and strict hyperbolicity for arbitrary species and nutrients with genuinely species-specific positive isolation allowed, using the compartment entropy identity. No inspected stronger theorem was shown to apply with all these hypotheses.

## value

PASS

Existence by itself frequently gives little global dynamical information in multiresource competition. Here a model-specific entropy decomposition makes coexistence uniquely attracting despite simultaneous exchange and unequal isolation, and the local compartments remove invisible biomass modes even if shared uptake vectors are dependent. This gives a substantive all-size structural prediction and separates coexistence rigidity from the unaddressed boundary and existence problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
