---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The increasing-label root-SET decomposition excludes exactly one unary chain at size r, so T_r_prime=exp(T_r)-z^(r-1)/(r-1)!, with u=exp(-T_r) solving u_prime=z^(r-1)u/(r-1)!-1. The integrating factor gives u=exp(z^r/r!)(1-F_r(z)); p_n=n[z^n]T_r. For |z|<3/2, |Im(z^r/r!)|<=9/8<pi/2, so Re F_r_prime>0; integrating over chords proves injectivity and exactly one zero of 1-F_r, the simple real rho_r in (1,3/2). Factoring u=(1-z/rho_r)g with g zero-free gives coefficient rho_r^-n+O(nR^-n). The large-r expansion follows from integral Taylor estimates; rho_{r+1}<rho_r by integrand monotonicity. Independently reconstructed exact-rational recurrence and enumerated labelled parent arrays for r=2..5 through n=8, agreeing with coefficients. Finite tests corroborate, do not establish complex/infinite proof.

## originality

PASS

No matching exponential zero-event theorem was found in relevant published results or inspected recursive-tree fringe literature. This is best-of-knowledge originality, not a proof of absolute historical priority.

## value

PASS

An all-length sharp rare-event absence probability for a fixed natural terminal path shape is not supplied by a central-limit theorem for occurrence counts; the common analytic zero-free radius, exact unit prefactor, and strict decay-rate hierarchy give a reusable enumerative tool.

The dated certificate retains the supplied scientific assessment, sources and limitations.
