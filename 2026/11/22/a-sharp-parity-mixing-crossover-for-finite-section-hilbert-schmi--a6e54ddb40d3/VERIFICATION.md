---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Gauge averaging preserves each squared commutator norm under conjugation and yields a feasible diagonal with no higher energy. The quadratic form is strictly convex on supported matrices: a compact K commuting with S² satisfies norm(K S^{2m}e_j)=norm(K e_j) for j=0,1, while the left side tends to zero because the shifted unit vectors are weakly null. Commutation then gives K=0. Thus the minimizer is unique and diagonal. Its exact energy has steps of length two with conductance one and steps of length one with conductance ε², with all indices beyond the support grounded. Each chain reaches a boundary even at ε=0, so the maximum principle puts the scalar harmonic solution in [0,1]. For N=2L the chain pins are x_0=1 and x_L=y_L=0, while y_0 is free. At zero coupling the even linear profile and the identically zero odd profile give 1/L. At ε=c/(2L), the scaled rails give exactly 2 times the squared H1 seminorm of the two interpolants; the two weak edges per cell jointly give c²∫(x−y)². Bounded scaled trial energy gives compactness in the uniform norm; weak lower semicontinuity and sampling the smooth limiting minimizer give the two bounds on the limiting minimum. With u=(x+y)/2 and v=(x−y)/2, fixing their initial values a and b gives energy 4(a²+κb²), where κ=c coth c and κ(0)=1 by continuity. The optimal a+b=1 gives a=κ/(1+κ), b=1/(1+κ) and the stated linear and hyperbolic profiles, which obey 0≤u−v≤u+v≤1. The unique limiting minimizer gives uniform convergence of the full sequence. κ increases strictly for c>0 because sinh(c)cosh(c)>c. Monotonicity in ε sandwiches the two off-critical regimes against fixed c/N; the diagonal d_j=1−j/N independently gives N E_N(ε)≤4−3/N+ε² for the upper supercritical bound. This proves the asserted constants and restrictions without appealing to numerics.

## originality

PASS

Condenser capacities and diagonal reduction are established, and the uncoupled value is exactly the known one-gap path capacity in squared units. The supported distinct claim is the coupled finite-section scaling law for these pins, together with both limiting profiles and scaling regimes. The closest coth formula identified concerns a different optimization objective and periodic boundary; neither that formula nor the qualitative modulus theorem determines this crossover.

## value

PASS

At ε=0 the parity rails decouple. For small positive ε the competition between longitudinal gradients and mixing depends on the support scale, and is invisible to the qualitative vanishing of the usual modulus. The theorem gives the sharp crossover from 2 to 4, not merely its exponent, and identifies where the odd-parity profile develops. This is a natural finite-section benchmark distinguishing a supported tuple energy from unconstrained asymptotic moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
