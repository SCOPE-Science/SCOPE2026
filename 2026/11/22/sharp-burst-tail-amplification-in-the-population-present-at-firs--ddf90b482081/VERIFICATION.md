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

For the density-based conditioning at t>0, the marked-batch intensity for a designated binder of age u carries weight z rho(u) psi'(w(u)+z ell(u)). Its independent background contributes the Poisson generating functional; at z=1 the age integral is 1-psi(q(t)). The binder accounts for the extra one in the mean. Monotone differentiation from below is valid even with infinite second moment: the possibly singular integral is bounded by mu-psi'(q(t)), by changing variables from age to binding probability. Uniform convergence of the short-age marks then gives the normalized pgf psi'(z)/mu and reduces the mean to the difference quotient of psi'. If J=1 almost surely, the triggering-batch sibling term vanishes identically. For the tail exponent between one and two, the rescaled sum has integrable bounds proportional to x^(-alpha) min(x,1), and integration by parts gives Gamma(2-alpha)/(alpha-1). At alpha=2, truncating at j=floor(1/F) and replacing 1-(1-F)^(j-1) by (j-1)F costs O(F) including the upper tail; the lower sum has leading c F log(1/F). The erfc asymptotic and the bounds exp(-dt)P(H<=t)<=F(t)<=P(H<=t) give the displayed constants. Finite ordinary mean follows by domination by total production. Inspected both frozen scripts without executing them. A separate finite check, python3 -B /workspace/review-evidence/independent_checks.py 2, passed 12 uniformized exponential-hitting generator comparisons; it does not attest to Brownian or infinite-tail limits.

## originality

PASS

Credit the same-model survival marginal, standard Palm weighting and regular-variation tools as prior. The checked sources do not cover the joint live count, its early size-biased limit in the stated batch immigration model, or its sharp Brownian mean crossover. Same-day related records are compared on their statements, not presumed later.

## value

PASS

The actual population present at binding is distinct from ordinary occupancy or mean first-passage time. The finite-time integrability versus early-time divergence and the change from an essential singularity to an inverse-time law and then a finite limit identify exactly when marginal population averages are misleading for this observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
