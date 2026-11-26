---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The one-step probability update eliminates x for n≥1 and gives θ_(n+1)=(1−δ)θ_n+δa tanh(θ_(n−1)). For δ≤1 the two-step sliding maximum contracts because the nonnegative coefficients sum to 1−δ(1−a)<1. For δ>1, y_n=(−1)^nθ_n gives a cooperative recurrence with u=δ−1, b=δa. If u+b<1 the same contraction applies; if u+b=1 the maximum is bounded and limsup L obeys L≤uL+b tanh L, forcing zero. For δ_c<δ<2 the strictly decreasing tanh(r)/r supplies the unique positive constant solution of the transformed recurrence, hence a primitive physical two-cycle. Its one-step physical Jacobian has a negative root greater than −1 and a positive root less than 1 because b sech²r<2−δ and a sech²r<1; both cycle points have the same Jacobian. The cycle is in the physical interior, giving an open basin. For δ≥2, choose θ_0>0, x_0=1/2: y_0,y_1>0 and the recurrence with u≥1 cannot approach zero. At δ_c the positive-cone quotients q_n converge to one by the vanishing-error iteration of G(q)=u+b/q: on [u,u+b/u], (G²)'=b²/(uq+b)² is uniformly less than one. The exact difference of w_n=y_n+b y_(n−1) is b(y_(n−1)−tanh y_(n−1)); q_n→1 gives w_(n+1)^(-2)−w_n^(-2)→2b/[3(1+b)^3]. Summation and odd symmetry yield nθ_n²→3(1+3a)/(4a) only in the stated strict sign sectors. The cubic coefficient is independently checked by critical_cubic() in /workspace/branches/independent_replay.py; that finite formal expansion is not a replacement for the ratio and telescoping proof. This is a deterministic probability-law result, not a finite-sample stochastic one.

## originality

PASS

The convergence through the exact endpoint is verified prior coverage under Hong–Ma's scalar singular-M-matrix specialization, independently of the later Oliveira–Teixeira theorem. Neither convergence sufficiency nor its endpoint is credited as new. The supported distinct result is the fixed-delay adaptive Markov phase diagram's nonlinear remainder: the explicit attracting flip for δ_c<δ<2, nonconvergence beyond the interval, and especially the exact critical squared-amplitude constant on the specified physical sectors. Closest qualitative flip-and-rate results concern different update laws.

## value

PASS

Even with instantaneous frozen mixing and a uniformly strongly convex loss, the coupled plant's delay can induce a stable alternating response at steps for which the stationary-reduced gradient map still contracts. The rigorous flip and critical squared-amplitude constant make this distinction quantitative, providing useful benchmarks for adaptive transfer models near loss of stability. Neither a generic flip analogy nor re-proving the known attractivity condition would alone supply this value. The critical rate is not asserted for every initial pair, and the cycle theorem does not classify all attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
