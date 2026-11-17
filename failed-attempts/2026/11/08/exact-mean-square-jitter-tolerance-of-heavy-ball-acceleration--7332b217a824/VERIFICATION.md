---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Modal diagonalization of an SPD H turns the common scalar iid stepsize noise into random scalar curvature A_k=lambda(1+xi_k) in each mode, with mean lambda and variance lambda²s². Each second-moment transfer uses only those two moments. Direct W=((1+beta,a),(a,1+beta))/D solves W=M W M^T+E; the positive two-step comparison sign equals vW11-1. Threshold decreases with lambda and is therefore governed by L. At boundary a fixed PSD covariance precludes convergence for all starts; above it positive-cone growth produces a diverging deterministic start. Substituting Chebyshev parameters yields 2/(sqrt(kappa)(kappa+1)); minimax GD gives 1/kappa. Independently verified exact scalar-cutoff algebra against the published random-curvature formula and the rational heavy-ball boundary.

## originality

FAIL

An October 13, 2026 published exact scalar stochastic-heavy-ball theorem already gives necessary-and-sufficient convergence for iid random scalar curvature with coefficient of variation v and any 0<=beta<1. With v²=s², eta=alpha, mean curvature lambda its exact threshold rearranges identically to the submitted formula. The submitted general SPD claim follows by orthogonal modal decomposition and monotonicity at L, independent of cross-mode dependence for summed squared error. Chebyshev and GD values are elementary substitutions. No noncovered substantive conclusion survives.

## value

PASS

Sharp multiplicative-jitter tolerance and acceleration-versus-robustness tradeoff on SPD quadratics are mathematically motivated and exact, including positive-step counterexamples; nevertheless they are algebraically inherited from earlier scalar random-coefficient theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
