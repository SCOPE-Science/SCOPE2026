---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Connected semi-balanced graphs admit a layer functional ℓ(h)−ℓ(t)=1 and affine hull with coordinate sum zero and ℓ pairing one (dimension |V|−2). Projection of zero into this affine hull is c=ℓ0/s, s=||ℓ0||²; for every edge root v=e_h−e_t, ||v||²=2, ⟨v,c⟩=||c||²=1/s, giving radius² 2−1/s. A common vertex sphere is minimum enclosing iff c lies in the convex hull: convex averaging gives a sharp lower bound and strict separation gives a smaller shifted sphere otherwise. Edge convex combinations yield nonnegative unit flows. For A→B, c=(-1/p,1/q), radius²=2−1/p−1/q; flow marginals 1/p and 1/q are feasible iff proportional Hall p|N(X)|≥q|X| by max-flow/min-cut. Biregularity supplies uniform edge weights. These are valid under standard Euclidean realization and |V|≥3.

## originality

FAIL

FAIL by decisive published stronger-result implication. The complete prior Resultary theorem on rank-variance spheres of connected graded quivers proves the same all-vertex sphere, minimum-enclosing iff the center is a nonnegative unit edge flow, AND a stronger lower-ideal cut criterion for ALL graded quivers. Semi-balanced directed graphs with ℓ(h)−ℓ(t)=1 are exactly such graded quivers, up to reversing the sign convention on each root vector. The submitted bipartite proportional Hall inequalities are the two-rank specialization of that general flow/cut theorem. No independent original remainder survives.

## value

FAIL

The canonical sphere is a natural metric invariant, but the entire proposed center/radius/minimality/flow theorem was already published for all connected graded quivers, with a stronger lower-ideal criterion. The bipartite Hall inequalities are a direct elementary specialization of that preexisting general flow condition. No independent new exact invariant, motivated exception or new structural principle remains; a correct restatement cannot earn a value pass under the covered-claim standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
