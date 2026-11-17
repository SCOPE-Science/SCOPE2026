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

Rabi evolution independently flips each spin with q(t)=a sin²(omega t); odd-N strict majority is B_N(q), so periodic Poisson integration yields exact per-cycle p_N. Unsuccessful cycles reset to same up state, and stopped-sum/renewal gives E[T_N]=1/(gamma*p_N), despite outcome-duration dependence. For a<1/2, Stirling first-success mass and geometric tail yield B_N(q)~sqrt(2/(pi*N))*sqrt(q(1-q))/(1-2q)*[4q(1-q)]^(N/2), uniformly near q=a. Nondegenerate Laplace saddle at t=P/2 adds N^-1/2, giving p_N~C(a)N^-1 exp(-N I(a)), I(a)=-1/2 log(4a(1-a)). For a_N=1/2-lambda/sqrt(N), t=P/2+y/(omega*N^1/4) gives q=1/2-(lambda+y²/2)/sqrt(N)+O(N^-1), hence central-limit integrand Phi(-2lambda-y²), dominated by e^(-c*y^4), so p_N~A(lambda)N^-1/4; direct Fubini gives F(0)=2^(1/4)Gamma(3/4)/sqrt(pi). Exact renewal transform E exp(-sT_N)=U_N(s)/(s/(gamma+s)+U_N(s)) with U_N(s)=E[e^-s tau J] gives gamma p_N T_N=>Exp(1) and variance ratio 1. Independent quadratures at fixed a=.2 and lambda=0 for increasing odd N approach both predicted prefactors. These numerical checks are not an infinite proof.

## originality

PASS

The primary 2022 Rabi-reset paper already gives exact majority transition integral and qualitative exponentially long finite-size lifetime, and the 2021 framework supplies general conditional reset renewal theory; these are credited, not claimed new. The sharp exact binomial LD prefactor, quarter-power scaling function and first-switch limit are additional mathematical analyses not found in inspected primary material.

## value

PASS

Quantifying a natural sharp finite-size collective threshold from exponential rare switches to quartic-saddle polynomial switches with constants and a waiting-time limit is a motivated physically interpretable asymptotic boundary, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
