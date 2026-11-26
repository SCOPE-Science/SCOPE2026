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

The centered balls give hub branches x and hS and leaf branches singleton O, pair P of coefficient a, and global G of coefficient h. On the positive cone take the two leaf-minus-hub differences. Their piecewise-linear Lipschitz constant is the largest spectral norm on full-dimensional strict cells: a generic segment splits into finitely many linear pieces, all other segments follow by continuity, and a small perturbation in a top singular direction realizes each active norm. Complex signals reduce by coordinatewise absolute value, a contraction for vertex ℓ². The independent selector certificate accounts for all 18 nominal tuples (including leaf exchanges). For a singleton hub, (O,O) and (O,P) are infeasible; (O,G) requires a+h<1. For a global hub, (O,P) and (P,P) are infeasible by h(1+a)>a and 2h/a−1>h, respectively. The latter inequalities use strict subadditivity and concavity of t^(1−α). The exceptional cell's edge rows (−1,1,0) and (h−1,h,h) give Gram entries 2,1,1,t_0 with t_0=1−2h+3h², and hence precisely the lower-exponent branch. For (G,G) with singleton hub the identical rows give H=2t_0. The (P,P) singleton-hub norm squared is ≤1, and (P,G) is bounded by its Frobenius square ≤H using a²+(1−a)²≤t_0 (use a<3h/2 and convexity on [h,3h/2] if h≤2/3, or t_0≥1 otherwise). For a global hub (O,O) has eigenvalues 1 and H−1, (O,G) gives t_0, (P,G) gives 2(a−h)²+h²≤H, and (G,G) is zero. A positive strict H-witness has S=1, h<x<2h/a−1 and y=z=(1−x)/2. For h<1−a, a small perturbation of (h,ah/(1−a),1−h/(1−a)) increasing x and making y>ax/(1−a) gives a positive strict exceptional witness; the G comparison remains strict. The exceptional norm dominates when h<1−a since h<1/2 gives H<2, whereas the off-diagonal entry 1 makes the exceptional eigenvalue >2. At equality a+h=1 there is no exceptional open cell, including for tie-boundary signals by continuity, and H is still attained. Independent bisection gave α*=0.212115088974130, left limit 1.593842169143955 and attained threshold constant 1.174412023763888. The frozen checker was inspected, not executed. Quantification is only over unweighted P3, counting-measure centered balls and the indicated two-input vertex-to-edge ℓ² norms.

## originality

PASS

Best-of-knowledge pass for the exact three-vertex fractional two-input phase law. The whole principle that an active-cell collapse can lower a sharp Lipschitz norm is already present on cliques, and the derivative-norm reduction is standard. The novelty credited here is the fully determined path-specific threshold, branch and equality laws; it is not an assertion of priority for discontinuity in the abstract.

## value

PASS

P3 is the smallest graph that exhibits both a two-vertex ball and a distinct full-graph ball, so it tests a feature absent on cliques. The exact calculation shows which mixed activation creates the sharp sensitivity, quantifies its loss at an interior fractional exponent, and proves actual attainment by positive inputs on each side, including the transition. This provides a reproducible sharp benchmark for how local linear pieces of nonlinear averaging control global perturbation stability. It makes no assertion about longer paths or weighted graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
