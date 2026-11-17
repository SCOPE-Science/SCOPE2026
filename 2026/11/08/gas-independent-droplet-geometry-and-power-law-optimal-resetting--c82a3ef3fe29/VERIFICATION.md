---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Summing/differencing the stationary directional equations gives Sprime=-r*rho and Rprime=-(r+alpha)*sigma. Decay at infinity and continuity of transport flux at the interface imply conserved S²-(r/(r+alpha))R²=0 in both phases; outward sign yields sigma=sqrt(r/(r+alpha))*rho and inverse-flux ODE Fprime(rho)*rhoprime=-Gamma*rho. Strict increasing unbounded liquid flux fixes center and dense width, and F_gprime(0)>0 makes gas spatial tail infinite. Source current jump at x=0 and exact phase masses follow integration; gas mass 2F*/Gamma is independent of gas constitutive shape under fixed contact flux. Power-law F_l=c*rho^p yields b proportional (t^(-1/p)-t^(-1))/(p-1) or log(t)/t; differentiation shows unique maximizing t=p^(p/(p-1)) or e. Independently differentiated p=1/2 giving t=2. These are existence/uniqueness only within the imposed symmetric single-core phase arrangement.

## originality

PASS

Grange 2026 derives the original flux first integral and linear-core (constant-speed, p=1) optimal t=e; these are not new. Changing dense liquid constitutive flux to c*rho^p gives a genuinely nonuniversal optimized ratio and an explicit gas-law independence classification. The related two-rate and concentration findings use other parameters with original linear-core flux. Full original source not personally obtained in this run, so possibility of already stated general nonlinear-flux formulas remains a residual priority risk.

## value

PASS

A matched-flux invariance that fixes dense mass/width while the gas motility changes is a motivated phase-separation structural property, and the p-dependent optimum describes the effect of core slowdown on optimal local resetting. The p=1/2 optimum 2 instead of e is a sharp model-discriminating statement, not only a numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
