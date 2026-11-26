---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The sample map is invertible since the nodes are distinct on a proper arc. Independently prescribing the two complex sample phases attains the sum of Lagrange coefficient moduli at a fixed evaluation point. With x=(v-u)/4 and m=(u+v)/2, this quotient is cos((t-m)/2)/cos x between the nodes and |sin((t-m)/2)|/sin x outside. On the longer exterior interval the distance from m runs from 2x to theta+|m|, and 2x<pi, so the maximum is at the far endpoint or at distance pi, giving exactly the capped-sine expression. This also handles arcs longer than a semicircle and the degenerate exterior intervals at endpoint nodes. Balancing sec x and sin(theta/2)/sin x proves the unique optimal separation; the cap is strictly above sin(theta/2) for m≠0, so only the centered pair attains the bound. The endpoint norm and the monotonicity and limits of C_theta follow directly. Independent chord-sum grid comparisons at four apertures, including asymmetric and capped cases, were consistent (python /workspace/review_checks.py, check 5); the analytic argument, not the grid, verifies the continuum statement.

## originality

FAIL

The earlier Resultary record 71dc11a952c3 gives the identical complex two-node all-pairs minimax result, including the unique pair, optimum, endpoint formula and limits. Its equation (2) gives the pointwise formula for every pair, whose direct one-variable maximization is the frozen capped-sine profile. Thus neither the central finding nor its one extra closed-form presentation supplies a mathematically distinct result of the asserted scope.

## value

FAIL

The problem is useful, but the exact sharp stability gain, unique node locations and instability of endpoint sampling are already available in the identical two-node minimax theorem. The only presentational increment is the immediate elementary maximum of the prior pointwise formula. It is not an independent new exact invariant or a useful surviving new claim warranting repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
