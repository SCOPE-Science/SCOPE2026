---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Translate the hub to zero. A direct check of the arm replacement uses the pairwise squared-distance formula for variance. Fix the other arms. The contribution within this arm is bounded by the sum of squared radial differences, which the straight ray attains. Up to a fixed term the cross-arm contribution is (1-P)∑_j p_j||y_j||²−2⟨∑_j p_j y_j,W⟩, where P is this arm's total mass and W is the partial mean off this arm. The bounds ||y_j||≤r_j are attained simultaneously on a ray pointing opposite W (any ray if W=0), and that same choice also attains the within-arm bound. Since (1-P)p_j>0, equality requires every radial distance to be saturated. Successive positive edge lengths and the triangle inequality then force all edge vectors on the arm to have one direction. Replacing one arm at a time shows that radial maps suffice, even in an infinite-dimensional Hilbert space, and equality forces every maximizer to be radial. For them the variance is R−||∑_i q_i u_i||². In a plane, the norms attainable by a sum of vectors of fixed lengths form a closed interval because the product of circles is compact and connected. Starting with one length, appending length w to a previous interval [L,U] gives extrema dist(w,[L,U]) and U+w. Inductively the minimum is max(0,2 max_i q_i−Q). The reverse triangle bound holds in any Hilbert space, and if the minimum is positive its equality forces the dominant arm to oppose all the others. The same arm argument works on the real line, where radial unit directions are signs and the optimum is R−η². Thus η=δ is exactly the line-valued optimum criterion; otherwise a plane is necessary and sufficient as the smallest possible affine dimension. Equal arm moments for a three-leaf unit star of uniform masses give the advertised 3/4 and 11/16 bounds.

## originality

PASS

The bare planar bound is directly covered even with arbitrary weights and lengths, and prior tree and separator results establish closely related optimizer geometry. The distinct supported contribution is the joint fixed-instance evaluation: the weighted arm-moment residual gives the sharp variance and the full maximizing direction condition, and the signed-partition residual evaluates the possibly smaller scalar optimum and decides precisely when a plane is needed. The strongest inspected weighted theorem gives an upper dimension bound or a worst-over-weights graph parameter rather than the fixed-data cutoff and scalar gap. This pass does not claim priority for planar existence, tree rigidity in general, or an uncited possible earlier scalar formula in isolation.

## value

PASS

The theorem computes both target-dependent extrema from simple weighted arm statistics and identifies when increasing dimension genuinely improves variance. In particular it isolates a discrete obstruction to attaining the continuous optimum on a line even when the arm moments close as a polygon. Straightness for every optimizing arm across arbitrary subdivisions yields an equality description rather than only a sufficient planar construction. The sharp fixed-data cutoff, not the already known treewidth upper bound, is the substantive consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
