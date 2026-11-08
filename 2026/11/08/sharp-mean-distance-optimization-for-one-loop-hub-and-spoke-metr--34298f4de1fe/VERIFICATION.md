---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The exact integral is reconstructed by partitioning pairs of uniform-arclength points into loop/loop, same-arm, distinct-arms, and loop/arm classes. For pairwise balancing, the coefficient of the length product is strictly negative because the loop remains positive. Differentiation and the quadratic sign tests prove the global unique minimizer in all integer arm counts.

Standalone `checker.py` uses standard Python only and performs independent shortest-path Monte Carlo, exact formula cross checks, length balancing inequalities, and optimum comparisons across 50 arm counts. Expected output: `ONE_LOOP_BOUQUET_OPTIMAL_MEAN_DISTANCE_OK`. Monte Carlo has limited precision; all infinite claims rest on the algebraic proof.

Historical priority is provisional: an older 1982 primary paper is available only by abstract/metadata in the inspected resources. Independent audit has not been performed.
