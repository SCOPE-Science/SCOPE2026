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

Signed filter differences give W(u) at least every antichain sum of |u|. Dilworth on incomparable copies gives the chain-indicator convex hull for rational feasible z; downward rounding and closedness cover real z. With u_p=s_p v_p and z=|u|/W(u), the unit norm and z_p^2<=z_p give 1<=W(u)^2 H. Equality requires binary z supported on a heaviest chain because each inverse-square weight is strictly positive. Filters realize all chain suffixes; the unit-step suffix walk has range one exactly when the signs alternate. This also proves attainment, including a singleton. An independent exact diamond case, scales (2,1,1,2), tested all 624 nonzero integer normals in [-2,2]^4 and found precisely the four predicted rays there. This is finite corroboration, not a proof for arbitrary real normal vectors.

## originality

FAIL

The earlier alternating-chain rigidity record states the unscaled result, including every equality direction, and contains the ingredients that mechanically give the weighted extension. Specifically, let E be the enriched chain polytope and D the order-polytope difference body. The earlier record gives E⊆D, all signed maximal-chain inequalities for E, and the exact support on chain directions via suffix sums. For S=diag(s), the signed inequalities for SE have normals (±1/s_p) on their chains and right side 1; their smallest unit-normal distance is H^{-1/2}. The positively weighted maximizing chains are inclusion-maximal. SD contains that ball, and the earlier suffix formula, evaluated after S cancels the inverse scales, gives equality on every alternating maximizing chain. If a unit direction of SD attains the distance, it also supports SE at the same ball contact. An inequality of SE active at this contact has distance at least the ball radius; Cauchy–Schwarz forces its unit normal to be that same contact direction. The suffix walk then forces alternation. Thus the entire weighted equality result follows from the earlier package by scaling its stated inequalities, not merely from similarity to chain polytopes.

## value

FAIL

An exact anisotropic width and its minimizers are natural, but the original record provides no independent new invariant beyond applying diagonal scaling to the published signed facet description and reusing its order-polytope contact argument. The unscaled classification is already explicit. A fresh proof and finite checks do not remove this mechanical implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
