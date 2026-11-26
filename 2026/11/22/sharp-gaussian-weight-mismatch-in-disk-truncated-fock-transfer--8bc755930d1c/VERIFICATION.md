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

Angular orthogonality in the target measure gives positive diagonal coefficients u^n∫_0^x t^n e^(−t)dt/n!=u^n q_n(x); factorial tail bounds give every positive Schatten exponent and positivity gives injectivity. Writing p_k for the Poisson masses, q_n/p_{n+1} is 1 plus a sum of strictly decreasing positive terms in n and tends to 1, so q_{n+1}/q_n decreases strictly to 0. It follows that only a single degree or two adjacent degrees maximize. At a tie the norm-attaining vectors form the span of the two normalized monomials, not just two lines. The ratio q_0/q_1 gives the exact first threshold and its stated expansion. Independently, if p'_k is the mass of Pois(ux), then e^{−x(u−1)}a_n=Σ_{j≥1}u^{−j}p'_{n+j}. The largest Poisson mass is asymptotic to (2πux)^(−1/2); this supplies an upper bound multiplied by Σ_{j≥1}u^{−j}=1/(u−1). Taking n=floor(ux), each fixed j attains the same leading mass, and geometric domination gives the matching lower bound. For n≥(u+ε)x all terms have exponentially small masses. For n≤(u−ε)x the terms with j≤εx/2 have exponentially small masses and the remaining geometric tail is exponentially small. Thus every maximizing n_x/x tends to u, with no lattice prefactor. The displayed radial Toeplitz symbol has the same coefficients by rescaling the radial integral.

## originality

PASS

The supported distinct content is the quantified modal transition and the sharp fixed-mismatch maximum with its prefactor and moving maximizing mode. The raw spectrum is already an immediate implication of the generic radial moment formula after explicit unitary dilation, and u=1 is explicitly known; neither is credited independently. Standard Poisson estimates and log-concavity furnish ingredients, but the inspected sources do not give the maximum, its exact threshold or the norm and degree result for this weighted family. In particular a local tail equivalent does not alone control the maximum over all degrees.

## value

PASS

A concentric cutoff is a natural regularization of an otherwise unbounded cross-weight inclusion. The exponentially small first transition interval, exact neighboring-degree thresholds and the nontrivial power and coefficient multiplying the fixed-mismatch exponential distinguish the behavior of its worst mode. These are useful sharp data beyond a known diagonalization or exponential-order estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
