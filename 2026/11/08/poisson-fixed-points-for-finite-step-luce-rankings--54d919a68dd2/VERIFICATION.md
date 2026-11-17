---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The exponential-race representation of Luce sampling (independent Exp(w_j) clocks) makes label orders uniform independent within each class conditional on the class word. For H_{j,n} eligible positions of color j in its own consecutive label interval, the exact conditional joint factorial moments are ∏(H_j)_{r_j}/(n_j)_{r_j}. The empirical weighted-clock CDF converges to G(t)=∑ α_h(1-e^{-w_h t}); quantile convergence at class-block endpoints gives H_j/n_j -> λ_j=e^{-w_j t_{j-1}}-e^{-w_j t_j}. Bounded conditional factorial moments imply a joint vector of independent Poisson(λ_j), with TV convergence on the discrete countable state space. The diagonal permuton density integral reproduces Λ=Σλ_j, but permuton convergence alone is not invoked for fixed points. The two-block derivative with respect to rate ratio a/b is positive because dΛ/dc=v e^{-(c+1)v}/[u c e^{-cv}+(1-u)e^{-v}]>0. Independent exact enumeration of four-label two-weight Luce rankings verified 30 conditional factorial-moment relations, not the n->infinity theorem.

## originality

PASS

PASS best of knowledge. The Borga–Chatterjee–Diaconis primary Luce-permuton paper explicitly presents the limiting fixed-point law with diagonal intensity as an open problem in Section 5.2. The submitted theorem proves that prediction for every fixed finite positive step profile and establishes joint blockwise independence. A separate Resultary finite-spike theorem has weights growing linearly with n, outside the uniform bounded finite-step assumptions, and does not imply this law. Classical Poisson fixed points of uniform permutations are the d=1 special case and are acknowledged as such.

## value

PASS

The theorem resolves a stated open fixed-point question for a mathematically natural non-exchangeable subclass of Luce rankings, with explicit joint per-weight-block Poisson laws and two-block monotonic sensitivity. Rare diagonal permutation points are not continuous in permuton convergence; an exact conditional factorial-moment method is needed. It is a substantial probability result despite not solving the arbitrary-profile conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
