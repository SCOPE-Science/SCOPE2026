---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

Pinned RESULT.md proves dF/dt=(kappa+lambda*x) z F for the cubic field, then derives r^2=a^2+cos(phi), phi_dot=-r^2(kappa+lambda*r*cos(theta))/2 and theta_dot=-c*r^2*sin(2theta)/2. Strict positive winding for the open parameter interval excludes other closed trajectories. Integrating dt along theta=0,pi,pi/2,3pi/2 gives the three minimal periods; linearizing theta gives mu±=exp(-2c integral 1/(kappa±lambda*r)) and unstable mu0. Pairing integrands yields log(mu+mu-)=-8pi*c*kappa/sqrt((kappa^2-lambda^2*a^2)^2-lambda^4). At the unique critical zero r(0)=R, kappa-lambda*r=epsilon+(kappa/(4R^2))*phi^2+smaller terms, producing square-root period and log-multiplier coefficients 4pi/(R sqrt(kappa)) and 4pi*c*R/sqrt(kappa) by dominated convergence. Remaining denominators stay positive. At equality theta=pi has one equilibrium and its complementary trajectory homoclinic; no ambient-normal multiplier asserted. Independently reproduced exact rational cofactor identities and numerical integral/product identities; these bounded checks do not establish the limit.

## originality

PASS

The four meridians and alternating relative stability are covered by Jana and are explicitly credited; the new claim is quantitative original-time clock ordering, stable multiplier product and selective endpoint arrest. Prior full published Oct-11 torus result has a z-dependent affine cofactor and a common clock/simultaneous arrest, not the x-dependent three clocks. The closest earlier primary literature inspected does not give the claimed quantitative formulas; priority is best-of-knowledge.

## value

PASS

An explicit geometric separation of physical periods despite identical invariant meridian count is a motivated stability/period invariant. The exact multiplier product and isolated critical nonhyperbolic degeneration distinguish time reparametrizations and provide useful sharp boundary behavior without claiming a general torus classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
