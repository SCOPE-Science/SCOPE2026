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

Translate by m times the constant vector to the weighted mean-zero space V. Jensen and strict convexity give a unique minimizer at 0 and strict increase along every positive ray. The closed sublevel is an interval when N=2, and is a ball in the weighted norm for any strictly convex quadratic entropy. Both have radial clipping equal to metric projection. Conversely, choose any u≠0 in V, budget E(m1+u)>η(m), and extrapolated candidate m1+(1+ε)u. If both operators agree, the normal cone condition demands that u be parallel to the gradient of the translated entropy in V. The gradient is nonzero by strict convexity at u≠0. Tangential derivatives therefore vanish on the connected weighted spheres for dim V≥2. In particular, the entropy restricted to each sphere is even. Taylor subtraction at ±tu has leading odd term η'''(m)t³ Σw_i u_i³/3, since the linear term is zero. The cubic sum is nonzero for some u: use (w_j,−w_i) on two unequal weights, or (1,1,−2) on three equal weights. Thus η''' vanishes at each m, giving a quadratic with positive second derivative. Independently recomputed the Simpson witness in integer-scaled arithmetic: all states have mean 1 and are positive, θ=5/6, E(y)=59/64, E(z)=2359745276177/2560000000000, and the squared errors are 1/300 and 2497/800000 respectively. Strict increase on the ray verifies that y is the radial output; z is strictly feasible and closer. Replay: python3 /workspace/reproductions/review_05_entropy.py (standard library). The frozen checker was inspected, not run. The necessity uses all means and budgets for each fixed positive weight vector, not identity at one mean or one point. This does not audit entropies on constrained physical domains, vector states, extra invariant-set constraints, or PDE stability.

## originality

PASS

The supported distinct statement is the sharp two-node/three-node boundary and all-positive-weights quadratic rigidity for global equality of a conservative radial limiter and the weighted nearest-entropy correction, with its exact positive-state separation. The underlying convex projection condition and conservative scaling construction are prior techniques.

## value

PASS

Choosing the largest feasible scale is common in mean-conserving nodal limiting; it does not answer whether one has minimized weighted data perturbation among all feasible corrections. The classification identifies precisely when this distinction matters as a function of dimension and entropy, not simply one arbitrary example. The small exact Simpson witness makes the first possible disagreement concrete while preserving positivity. No numerical scheme's entropy guarantee is contradicted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
