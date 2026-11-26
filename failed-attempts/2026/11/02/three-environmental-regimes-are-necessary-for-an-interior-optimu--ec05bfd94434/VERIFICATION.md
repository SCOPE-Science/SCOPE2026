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

The stationary environment marginal is independent of the speed. With row generator qG and s_i=c_i+e_i, the occupied joint masses solve (diag(s)−qGᵀ)u=diag(π)c. One regime is constant. In two regimes the positive determinant s₁s₂+q(bs₁+as₂) gives a fractional-linear function of q with derivative sign that of (s₁−s₂)(c₁/s₁−c₂/s₂), including both constant cases. For equal off-diagonal rates the rank-one structure gives u_i=(c_i/n+qP)/(s_i+nq); summing yields the claimed weighted ratio. An independent exact solve of the full six-state stationary equations reproduces P(q)=5/8+9q/[8(9q²+39q+28)]. Thus the two endpoint limits, strict improvement at all positive finite q, unique maximum by the sign of 28−9q², and the attained value are all correct. The limits do not assert ergodicity at q=0.

## originality

FAIL

The threshold and even the complete-symmetric, equal-endpoint witness reduce to already indexed results under exact relabeling. Most decisively, a separate two-habitat result gives the same chain, the same complete-generator ratio and a numerator interpolation construction. Using that construction for the polynomial q instead of a polynomial with two interior roots generates the exact frozen rates and occupancy excess, as detailed below. The reservoir theorem also gives the general two-state obstruction and sharp reversible onset after identifying stationary first-moment equations. This is a statement-level coverage finding, not a historical priority judgment based on the catalogue dates.

## value

FAIL

An interior occupancy gain with identical fast and slow limits is a sensible ecological question. Here the regime-count boundary transfers from an equivalent response, and even the refined witness is just a low-degree choice in an existing construction for the same model. No separate new ecological mechanism or mathematical boundary remains. The result can serve as an illustrative example, but not as an independent scientific finding under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
