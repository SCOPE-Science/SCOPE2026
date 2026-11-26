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

The nonsource harmonic equations are contractive for 0<lambda<1. For hub value X the supports of unselected vertices in empty and singly selected pairs are dX and lambda(1+X)/2. These give the stated hub equation, with positive denominator, and the minima over each occupancy type. In the no-empty-pair case, monotonicity from exactly one source per pair gives X>=d, so the hub does not lower the minimum when a singleton pair remains. Multinomial weights count labeled placements. For d<tau<=lambda a feasible set needs to hit each pair, and the hub-free size-m pattern has minimum d, leaving only the two stated size-(m+1) patterns. Above lambda only the full set works. Evaluating the two remaining hub-free patterns gives beta_m and alpha_m; for example alpha_m-d has numerator 2 lambda^2(1-lambda) over the positive common denominator. The triangle and threshold equalities check out.

## originality

FAIL

The optimizer phase diagram is an exact q=2 specialization of the earlier clique-windmill theorem. The all-set polynomial is not printed there as a theorem, but its tests, weights, and hub calculation are mechanically obtained from the earlier general block equilibrium and hub averaging. The triangle edge case is already a complete-graph calculation. This is a coverage/implication finding, not a correctness or access failure.

## value

FAIL

Optimizer thresholds are useful on this natural family but already available from the windmill theorem. The remaining all-size presentation is a direct multinomial repackaging of its affine block tests in the two-peripheral-vertex case; it supplies no independent invariant not mechanically determined by those results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
