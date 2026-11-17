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

PASS: radial squared norm obeys logistic equation and converges to rho; rationally independent skew frequencies yield full product omega-limit torus whose intrinsic volume is (2π)^N rho^(N/2) sqrt(prod U_j). Spherical angular sampling turns squared rotation-block energies into Dirichlet(1,...,1) with extra odd-coordinate Dirichlet shape 1/2. Direct Dirichlet integration proves Mellin moments finite iff s>-2, and gamma multiplication gives independent Beta(1,b) product law for R². The Mellin transform at z=1 has pole order N-1 (even D) or N (odd D), producing sharp r² log^(N-2) versus r² log^(N-1) lower tails. Near the unique balanced maximum, the constrained quadratic form has Gram determinant N; the odd extra Beta(1/2,N) endpoint density adds an epsilon^(1/2) factor. Independent gamma/beta-product moment equalities and two analytically independent formulas for both sharp upper constants agreed for N=3,4,5. Monte Carlo in supplied verify_torus_volume.py is bounded corroboration only. Frequencies and nonzero radial law are scoped exactly; no mixing-time or resonant claims.

## originality

PASS

PASS best-of-knowledge with explicit general-product risk: earlier original oscillator source establishes the torus geometry but not its isotropic-sampling intrinsic-volume distribution; two-factor Dirichlet product formulas and general independent-beta-product distribution methods are known, but the inspected source statements do not explicitly supply this N-factor geometrical mapping, both sharp endpoint constants or the 2N versus 2N+1 parity transition. General beta-product formulas could imply parts mechanically; no unconditional priority is asserted.

## value

PASS

PASS: Intrinsic volume of a natural family of quasiperiodic invariant tori is a motivated geometric invariant, and its full sampling distribution and sharp opposite endpoint tails quantify the effect of one inactive ambient coordinate. The explicit parity shift and constants are useful to geometric-probabilistic studies even though classical Dirichlet/gamma tools are prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
