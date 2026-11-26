---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On nonzero periodic amplitudes there is no visit to the absorbing zero. Substituting the two branches gives logistic amplitude and an independent action on sign (identity for -a, transposition for +a). Sign return requires a multiple of the amplitude period and, for +a, an even time. This gives the least periods and number of lifts, with zero counted separately. At odd n the positive-parameter fixed count is 1; at even n both counts are 2P_n-1. Taking formal logarithms gives the stated zeta products; the correction in the positive case has coefficient -(-1)^n/n. The full-tent conjugacy at a=4 gives an intersection with the diagonal in every one of the 2^n monotone full branches, and no duplicate periodic point at shared branch boundaries. This gives both rational zetas. The transfer operator averages over one inverse point per dyadic subinterval; the averages converge uniformly for continuous densities and in L1 for all densities by contraction and approximation. All powers have the unique arcsine ACIP after conjugacy and are mixing. The sign actions give two mixing ergodic ACIPs and their mixtures at -4, versus equal sign weights and the unique square-invariant conditional densities at +4. The latter measure is ergodic because the square is ergodic on each half and the halves exchange; its sign correlation is (-1)^n. The exchange is a mod-null statement, since endpoints mapping to zero do not literally swap. Entropy is log 2 by the invariant-half conjugacies (for the square in the positive case) and the iteration identity.

## originality

FAIL

The frozen family is literally the Cartesian product of L_a with the identity or transposition of a two-element set, with only the two states at amplitude zero identified. An inspected prior direct-product theorem gives the all-period and fixed-point assertions immediately; the collapsed fiber changes the zeta by the reciprocal Euler factor of the new orbit divided by that of the old fiber. Substituting the classical full-tent count gives the rational functions. The endpoint statistical claims are the standard direct-sum/product consequences of the classical full-tent mixing and uniqueness for the base and its square, with a constant sign permutation. This is failure by verified stronger coverage and immediate implication, not a finding that the formulas were printed in the 2022 exact-family paper or that the proof is wrong.

## value

FAIL

This is a useful illustrative example of a mixing map combined with an independent periodic sign, but the asserted exact invariants are mechanically forced once the two branches are written in amplitude/sign coordinates. The all-period and zeta formulas require only known product formulas and replacement of a two-point zero fiber; the endpoint tally and statistical contrast require only the standard full-tent formulas and a fixed two-point permutation. No additional coupled-dynamics result, obstruction, or nonroutine invariant is established by the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
