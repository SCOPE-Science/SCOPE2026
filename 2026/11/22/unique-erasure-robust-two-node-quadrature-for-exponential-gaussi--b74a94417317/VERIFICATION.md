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

Integrating the covariance gives the stated point-integral covariance W and prior integral variance. Conditioning on the reported success set and averaging its four probabilities gives exactly the displayed weighted sum of single-observation squares and the two-observation Schur complement. At coincident sites both successes give only one value; the continuous limit agrees (the difference of the integral covariances is O(gap), while 1-r is of first order in gap). For fixed half-gap u and C=cosh(v), writing the two-success gain as the sum of (w_s+w_t)^2/[2(1+r)] and (w_s-w_t)^2/[2(1-r)] yields the two stated derivatives. The first is strictly negative by zC<=exp(-u) and cosh u-exp(-u)cosh(2u)=(exp(-u)-exp(-3u))/2>0 for u>0; the two-success derivative has sign ze^u C-1<0 for u<lambda/2. Coincidence maximizes at the midpoint and maximal gap forces the center. Therefore a global optimum must be centered for every p, including p=1. On centered pairs A=1-z cosh u is positive and strictly concave, B=1-p/2+(p/2)tanh u is positive and concave, and 2 log A+log B has strictly negative curvature. At zero its derivative is p/(2-p)>0; at the upper endpoint A'/A=-1 and B'/B<=1-tanh u so the derivative is negative. Hence exactly one interior gap maximizes the risk reduction, and rearranging its first-order equation gives the stated root without a spurious denominator zero. The p derivative of the log-slope is sech²(u)/(2B²)>0, giving strict monotonicity including the endpoint. The small-p expansion follows by smooth inversion at zero; for u=lambda d and lambda->0 the limiting ratio is 8d/(1+4d), and for u=lambda/6+c and lambda->infinity it is exp(3c)/2. In each case fixed test points bracketing the limiting crossing are sufficient, since the log-slope has the sign of p minus the right-hand side of the root equation. Independent Schur-complement risk and two-dimensional numerical comparisons agree; at (lambda,p)=(1,1/2), the sites are 0.397545436261487 and 0.602454563738513, with risks 0.263244357475696 and 0.271304517104358 for the optimum and duplicate midpoint respectively. At lambda=0.0001,p=1/2, u/lambda=0.0833351273 near 1/12. Replay: python /workspace/branches/reproduce_frozen.py (erasures section). The uploaded checker and verification notes were inspected, not executed. Proof is for equal, independent process-independent deliveries of two precommitted noiseless queries and fixed other parameter in each limit.

## originality

PASS

The supported contribution is the complete stationary exponential covariance design for 0<p<1, including the all-design uniqueness, direction of movement and limiting laws. The prior p=1 solution is credited and does not count as novel. Gaussian conditioning, generic Bayesian quadrature, and structurally similar erasure problems with different kernels are established.

## value

PASS

With two salvageable observations of a standard stationary Gaussian process, losing one favors high individual information at the midpoint while having both favors separation. The exact result decides whether to duplicate for reliability or separate for information: duplication is never optimal for any positive common delivery probability, yet the two nodes coalesce in the rare-success limit. The quantified movement and distinct covariance-length regimes make the result a useful reference design, not just the known no-erasure boundary or an isolated numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
