---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The full proof reconstructs G_{ij}=alpha_i(alpha_j+delta_ij)/(T(T+1)), K(x,y)=T(T+1)sum_i x_i y_i/alpha_i-T. It correctly reduces maximum L∞ evaluation norm to vertices, computes the beta tail and strict least-alpha order by conditional Jensen, and identifies the negative kernel mass. For fixed a>0 as T grows, TY_i converges to Gamma(a,1); the exact beta second moment gives uniform integrability, so L_T(a)/T tends to 2 a^{a-1}e^{-a}/Gamma(a), and for N equal a parameters norm/N tends to 2 a^a e^{-a}/Gamma(a). These are analytic deductions, not experimentally inferred.

## originality

FAIL

FAIL. A published November 2 all-parameter Dirichlet-weighted projection result states the identical norm, vertex selection, sign extremizer, negative excursion, balance, and nonattained envelope, AND exactly the symmetric fixed-alpha gamma limit. October 18 also proved the non-asymptotic theory. There is no novel final claim under a new title.

## value

FAIL

FAIL. The full purported theorem is a direct reproduction of a previously established sharp stability law and dimension-growth formula; alternative notation T/N and gamma density integration do not add a motivated independent invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
