---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The printed three-state PID recurrence gives V_t+K_d D_t=x_t-x_{t-1} after a completed update, so each SPD Hessian eigenmode satisfies u_{t+1}=(1-r lambda+beta(lambda))u_t-beta(lambda)u_{t-1}, beta(lambda)=alpha+K_d(1-alpha)lambda. Strict Jury inequalities imply exactly K_d L<1 and 0<r L<2[1+alpha+K_d(1-alpha)L]. The modal characteristic root product beta gives the sharp radius floor sqrt(beta), attained at r lambda=1+beta. Full four-state determinant factorization from the previously published independent theorem independently confirms the eliminated recurrence, with passive factors z(z-alpha). Source verification code was actually read, and an independently written exact polynomial-factorization check succeeded.

## originality

FAIL

Decisive published SCOPE/Resultary theorem dated 2026-10-04 covers the same printed 2018 PID recurrence and all the claimed sharp stability/rate results. The assigned result dated 2026-10-12 is not original despite a correct proof. No disclaimer or extra certificate can repair its published-coverage failure.

## value

FAIL

Every substantive structural formula, sharp gain ceiling, best attainable modal spectral radius, and heavy-ball interpretation is an exact restatement of the earlier published SCOPE-20261004-7b863d0a1163 theorem. The only added explicit observation, loss scaling H -> cH, is a routine one-line substitution into that theorem, without a separate motivated mathematical gap. This package is a known-theorem recomputation, not a new independently useful fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
