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

The joint law, moment formulas, strict sign and synchronization asymptotics hold. Independently, for a reset-free leg let H be the first hit of zero and W the piecewise occupation penalty. The contribution from absorption first is g(a)=E_a exp(-integral_0^H (r+W)dt); the reset-first contribution is h(a)=r E_a integral_0^H exp(-integral_0^t (r+W)ds)dt. Renewal gives F=g(a)/(1-h(a)). With C=cosh(mu a), S=sinh(mu a), K=C+(nu/mu)S, matching the killed diffusion solutions gives g(a)=1/K and h(a)=[r(C-1)/(r+q)+(nu/mu)Sr/(r+p)]/K. Thus F^{-1} is exactly (1), including p or q zero. Occupation at the single reset point has zero duration, and each trial has success probability exp(-z); the reset-first exponential moment is continuous at zero and strictly less than one there, while the success-first moment is bounded for tilts below r. This justifies the moments. For dimensionless alpha=p/r and beta=q/r the first derivatives of F^{-1} at zero are sinh z and cosh z-1; the Hessian entries are -sinh z, (z cosh z-sinh z)/2, and z sinh z-2(cosh z-1). Applying the Hessian of -log(F^{-1}) yields (2); the covariance coefficient (4^n-n-1)/(2n+1)! is positive for n>=1. Substitution into the normalized variance of the difference gives (3). In (1) normalized Laplace arguments are O(e^{-z}) and mu a=z+O(ze^{-z}), so the limit is 1/(1+s+t). The limiting pair is positive on the diagonal and the mean ratio tends to one, giving convergence of U/tau to 1/2 in probability. If A,B are the two normalized variances and M is the defect, 1-corr=[M-(sqrt(A)-sqrt(B))^2]/(2 sqrt(AB)); A,B=1+O((1+z)e^{-z}), M~4e^{-z}, proving (5). Replay uses the displayed renewal and derivative identities. The frozen check.py was inspected, not executed; its numerical checks would not prove any infinite-domain or asymptotic statement. No formal proof or expert attestation is claimed.

## originality

FAIL

Distinct catalogue coverage of the full residence law is established: the November 2 joint first-passage exposure result contains (T,R) with T=U+L and R=U. This is more than a matching model or marginal. An invertible change of random variables gives exactly the frozen joint law, and differentiation, normalization and expansion of that same transform give the claimed residence cumulants and defects. The frozen record isolates useful consequences not separately displayed there, but no distinct law or independently substantive mathematical remainder is established. This is a coverage judgment against the available corpus, not a claim that the November-labelled catalogue record predates the October-labelled entry or establishes historical priority.

## value

PASS

The absorption time is physically partitioned into two natural cumulative exposures, so strict positive cross-covariance despite disjoint instantaneous indicators and the leading coefficient of their normalized synchronization defect are informative, beyond a scalar mean capture rate. This assesses the scientific utility of the formulas, not novelty or additional value over a source that already determines them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
