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

In a cactus with cycle blocks and at least one edge, deleting an edge leaves its cycle complement as the unique simple path between its endpoints. The remaining blocks are electrically pendant, so the relevant resistance is exactly the sum of reciprocal conductances on that path. In resistance coordinates the unit-detour constraints are affine and the expenditure is strictly convex. The threshold sum is continuous, increases strictly after the least price, and crosses 1 only with at least two active terms. Write q_i=√max(c_i,T) and H=Σq_i−√T. Then r_i=q_i/H is primal feasible, and the nonnegative multipliers H²(1−c_i/T)_+ sum to H², satisfy complementarity (including thresholds with ties), and give the stationarity identities c_i/r_i²=Σ_{j≠i}ν_j. Also Σ c_i/q_i=H from the threshold equation. Strict convexity proves uniqueness and the single-cycle cost H² at unit bound. At general bound d each cycle independently requires H_j²/d; summing proves feasibility and uniqueness at d=S/B and yields the budget split. Substitution at prices (1,…,1,t) gives the stated plateau condition and the two matching value formulas. Independent finite tests checked random heterogeneous cycles and solved for the failed-endpoint voltages on an explicitly assembled two-cycle cactus. The positive budget and cycle-block scope exclude the empty-edge vacuity: if the singleton graph were counted as a bridgeless cactus in the opening shorthand, its feasible set would be empty.

## originality

FAIL

The earlier 2026-10-12 directed-ring passage result e8c1669f972b is an exact equivalent of the central one-cycle optimization, including arbitrary heterogeneous prices, the unique optimum, the capped square-root law, and the plateau. The cactus extension is not literally stated there, but after the standard cut-vertex reduction it is mechanically implied by the quoted one-ring theorem and a scalar budget split. No substantial distinct claim survives in the frozen result. This decision rests on positive prior-coverage evidence, not on a literature search miss.

## value

FAIL

The fault criterion is natural and the network interpretation may be useful, but the frozen exact finding does not fill a distinct mathematical gap: the cutoff, closed form and nontrivial uniqueness already apply to an identical cycle optimization. Articulation decomposition and the scalar budget inequality account for everything added by the cactus. This is a useful reformulation and application, not a standalone new structural lemma or an unaccounted-for exact invariant under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
