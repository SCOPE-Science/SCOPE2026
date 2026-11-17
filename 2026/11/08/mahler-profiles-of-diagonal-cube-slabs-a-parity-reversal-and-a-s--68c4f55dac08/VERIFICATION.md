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

PASS: Exact Irwin-Hall inclusion-exclusion computes volume of [-1,1]^d intersect |sum x_i|<=t. Polar is convex hull of cross-polytope with +/- t^{-1}(1,...,1); visible-facet exterior pyramids have disjoint interiors and give W_d(t)=[2^d+2 sum binom(d,j)((d-2j)/t-1)_+]/d!. For 0<t<=1 the polar volume is (B_d/t+C_d)/d!, while strict unimodality of uniform-cube sum densities gives odd-dimensional decreasing product and positive even-dimensional right slope. In d=3 exact branches give 32/3 minima at t=1,3, one interior local maximum at the unique Q-root, and unattained supremum 12 as t approaches 0. Independent exact Fraction checks verified all d=2..8 cube endpoint identities, nine d=2..10 small-width parity inequalities, and every sampled d=3 rational t. They do not prove universal dimensions.

## originality

PASS

Best-of-knowledge: exact published same-object claims and primary literature compared by statement/implication, with strong prior ingredients acknowledged and residual risks retained. The complete accepted contribution is not shown covered by the inspected sources.

## value

PASS

PASS: The exact parameter profile for a natural centrally symmetric clipping path is a meaningful geometric invariant. Odd/even thin-slab reversal and the full sharp three-dimensional turning-point/equality diagram are not mechanical restatements of the known Mahler bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
