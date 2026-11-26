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

The independent gamma-block construction gives Y_i=√P_i√W in I and Y_j=√S_j√(1−W) in J, with the two Dirichlet proportion vectors independent of W and one another. The distinct I pair has E√(P_iP_j)=c_ic_j/A and E√P_i=c_iΓ(A)/Γ(A+1/2); the covariance therefore has the sign of Q−K_A. Interchanging the blocks sends r to 1/r, and for a cross-block pair an independent-copy covariance identity makes the product of the increasing and decreasing differences strictly negative. These statements include singleton blocks by vacuity for nonexistent pairs. For m_s=E W^s, local dominated differentiation gives r m_s'=−s(m_s−m_{s+1}); strict moment log-convexity for a nonconstant W gives m_2/m_1>m_{3/2}/m_{1/2}, hence strict increase of Q. At r=1 beta moments give Q=K_A/K_{A+T}<K_A by strict gamma log-convexity. The beta-prime density of V=L/H is proportional to v^(T−1)(1+v)^(−A−T). For T>s dominated inverse moments give order r^(−s); for T<s, u=rv gives the beta integral of order r^(−T). At T=s, on 1/r≤v≤1 the scaled integrand is proportional to 1/v with integrated error O(1), bounded by a constant times the integral of [v+1/(rv)]/v; the outer ranges are O(r^(−s)). These regimes give divergence of Q for T≤1, including the log endpoints. For T>1 its limit is K_AΓ(T)Γ(T−1)/Γ(T−1/2)^2>K_A. Strict monotonicity then proves the claimed unique crossings and ordering for every positive shape. The uniform S³ formula was corroborated by 50-digit independent quadrature and by bisection of the elementary uniform-beta moments for d=r−1>0: m_1=(r log r−d)/d², m_(1/2)=r arctan(√d)/d^(3/2)−1/d. These give 4.258066031391 and reciprocal 0.234848401276, diagnostic decimals rather than an interval certificate. The uploaded checker was read, not run.

## originality

PASS

The exact singleton-versus-rest model and examples of sign changes are not new: they are SDirIII from Leshilo (2024), whose full thesis was obtained and read for the comparison, beyond the bibliographic abstract used in the frozen record. The supported claim is the universal all-shape unique crossing and full two-block sign diagram for coordinate values. The inspected thesis formulas and example plots do not already settle that statement or its all-shape singleton specialization; no novelty is credited to the distribution in that specialization or to the existence of positive covariance in general.

## value

PASS

The theorem turns earlier selected sign changes for a known special case into a complete strict sign classification, including singular beta-shape regimes with divergent inverse moments. Dependence only on block totals and opposite unique crossing scales reduce the whole sign pattern to two scalar roots. The contribution is this structural result, not the baseline spherical moment or a computed four-dimensional example alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
