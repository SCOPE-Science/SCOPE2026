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

For a signed m-vertex face on S, the Euclidean foot has x_i=b_i+s_i(1−Σ_{j∈S}s_j b_j)/m on S and zero elsewhere. Positivity of the i-th signed barycentric coordinate for all sign choices is equivalent to (m−1)|b_i|+Σ_{j∈S∖{i}}|b_j|<1, because the signs at i and at the other coordinates can be chosen independently. The full-support inequalities dominate every smaller support and imply interior membership, giving exactly the stated strict kernel. Its closure is the corresponding weak ball by radial scaling. Each of the d·2^d given normals uniquely supports a facet at a point of the chosen signs with unique absolute maximum at its distinguished index. Signed order chambers give all possible vertices s/(d−2+|supp s|); the listed candidates are extreme because the active-normal differences generate d−1 directions perpendicular to the point (off-support flips and on-support changes of distinguished index), and one active normal supplies the last direction. The origin is interior. The order-difference coordinates give a simplex with volume 1/[d!∏_{j=1}^d(d−2+j)]; counting all 2^d d! chambers gives the volume and fraction. The central-binomial asymptotic at d−1 recovers 4√(πd)/4^d. At d=4 the volume is 2/45 and the fraction is 1/15.

## originality

PASS

The supported distinct result is the identification of the all-face Euclidean projection kernel for regular cross-polytopes in dimensions d≥4 and its resulting geometric probability law. The d=3 exact case is already known; the mixed-norm body and signed-prefix atom representation are covered much more generally by ordered weighted ℓ₁ geometry, so the norm-ball calculations are not credited as independent novelty.

## value

PASS

The natural all-face admissibility test ranges over exponentially many faces. In the original regular Euclidean embedding it reduces to two norms, and the exact volume determines how rare simultaneous relative-interior feet are for uniform anchors in high dimension. The point is this geometric identification and the associated probability, not a renaming of a known mixed-norm ball.

The dated certificate retains the supplied scientific assessment, sources and limitations.
