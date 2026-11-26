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

The orthogonal error projectors have rank one. The norm squared of their product equals the product of the squared cosines of successive direction differences, none zero here. Each parity of successive pairs uses disjoint iid index blocks; two strong laws yield the expectation of the pair cost, including when some masses are zero. Ordered pairs account for the factor of two in R=pᵀWp. For c=cos(π/5), d=cos(2π/5), c³−d=(4−√5)/8>0, hence b>3a>0. On four consecutive occupied indices the zero-sum direction (1,−1,1,−1) has zᵀWz=2(b−3a), so the average of the two feasible small perturbations improves the value. This excludes supports of both sizes four and five. Every triple has either two b-pairs with common center or two a-pairs with common center. Holding the center mass x fixed, the two leaf masses must be equal at the maximum with that x. The first case gives 2bx(1−x)+(a/2)(1−x)² with unique interior maximum at x=(2b−a)/(4b−a), value 2b²/(4b−a). The second case is at most (b/2)(1−x²) since 2a<b, and b/2 also bounds supports of size at most two. Thus precisely the five rotations attain the sharp value; the gap to b/2 and the smaller uniform value follow by subtraction. The one-step factor is the top eigenvalue of the trace-one mean projector, namely (1+|Σ p_j exp(2πij/5)|)/2. Uniform makes the modulus zero; for each rate maximizer it is x−2y cos(π/5)>0 because x/y>5/3>2 cos(π/5). This verifies the claimed strict comparison, not a claim about the asymptotic annealed optimizer set. Independent algebra and numeric substitution reproduce the reported values, including factor 0.5263771970. The frozen checker was inspected, not executed; it supplies finite corroboration only. The directions are equally spaced projectively, not pairwise equiangular (an informal descriptor in the frozen self-review, not a hypothesis of the theorem).

## originality

PASS

The rank-one exponent formula and the reduction to a generally nonconvex quadratic design objective are known and excluded from the originality credit. The distinct supported result is the exact pentagonal weighted quadratic maximum, all five maximizers, and their strict separation from one-step worst-direction optimality. The strongest inspected planar comparison has an expressly different stochastic objective.

## value

PASS

Five equally spaced projective lines give a natural symmetric tight planar frame, not an arbitrary chosen matrix slice. On this frame the usual uniform tight-frame design is strictly suboptimal for typical trajectories, while every sharp typical design drops two rows and is worse on the one-step worst-direction criterion. The exact support/equality classification and rate gaps explain the distinction of practical sampling objectives; they are not supplied by the known rank-one representation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
