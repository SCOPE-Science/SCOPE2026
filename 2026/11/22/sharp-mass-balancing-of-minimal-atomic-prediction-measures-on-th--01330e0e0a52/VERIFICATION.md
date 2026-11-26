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

For the repaired claim. The frozen literal minimum of the number of distinct positive-mass atoms over all optimal probability measures was false: its own Poisson probability is optimal and nonatomic. The replacement RESULT.md in repairs/2 states explicitly that the minimum of n+1 is a support-cardinality minimum among finitely supported optimal measures, and distinguishes that from the prediction optimum over all probabilities. Recheck: z^n/R^n attains the upper bound for Poisson moments via orthogonality to a basis of the vanishing-at-R subspace, and equality in its disk integral forces circle support. A polynomial vanishing on at most n support points rules out smaller finite supports. The rational Cayley transform of the Herglotz function is inner of degree n+1, with precisely the atomic support as its level-one fiber. Its value and Taylor coefficients force the Schur transform after factoring z to be lambda*z^n; the converse yields a probability with the required moments and exactly n+1 nodes. The orthonormal family follows because weighting by |z-a|^2 cancels the Poisson density on the circle and the moments give orthogonality to the constant. The exact Laurent quadrature then gives the diagonal kernel reciprocal at the nodes. Its weight is strictly largest near 1 and smallest near -1. The increasing phase increment is odd about each reference point; relative phase u gives nearest angular distance equal to the inverse increment at min(u,2pi-u). It has a unique maximum at pi. Hence -1 and (-1)^n are the claimed phases, including n=1. Integration of the phase uses the continuous branch with real denominator 1-a cos(t)>0 and gives both angle equations. For fixed a the endpoint increments have a cubic remainder with bounded coefficient and positive linear term of size n, establishing the stated O_a(n^-4) angle errors and the mass limits. Factoring the two n=2, a=1/2 cubics gives pairs with real parts 3/4 and -1/4, respectively, and the listed exact masses. Replay: repaired RESULT.md, proof steps 1–4. The frozen NumPy diagnostic was inspected, not run; its finite checks do not certify the continuum of phases or arbitrary degree.

## originality

PASS

The finite-support clarification preserves the actual finite-fiber extremal problems. Credit prior prediction optimality, Szegő/paraorthogonal parameterization, and the kernel identity. The separate aligned-Blaschke result treats angular mesh gaps, not pointwise masses, and supplies different optimizing fibers for the corresponding objectives. Supported originality is the unique extreme-mass optimizers, with exact values and their parity compatibility, within the smallest-support prediction family.

## value

PASS

For the finitely supported optimal designs of least support, weighting is the remaining design choice once prediction performance is fixed. Exact uniqueness for both complementary extremes and the parity obstruction distinguish when an experiment can simultaneously avoid the heaviest and lightest allocations. This is an all-degree design classification, not merely a known quadrature construction or a sampled phase comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
