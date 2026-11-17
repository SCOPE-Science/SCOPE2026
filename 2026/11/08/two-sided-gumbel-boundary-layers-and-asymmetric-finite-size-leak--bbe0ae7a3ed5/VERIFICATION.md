---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The exact known stationary conditional-Gaussian representation has v(u)=v_-+Delta u and h(u)=v(u)u^(alpha-1)(1-u)^(beta-1)/[vbar B(alpha,beta)] for 0<u<1, with v_-=D/mu1<v_+=D/mu2, alpha=r1/(2mu1), beta=r2/(2mu2). For M_N=max of N signed coordinates, F_N(x)=integral h(u) Phi(x/sqrt(v(u)))^N du exactly. Gaussian Mills bounds at a_N=sqrt(2L)-(log L+log(4pi))/(2sqrt(2L)), b_N=1/sqrt(2L) and changes u=v_-s/(Delta L), 1-u=v_+s/(Delta L) yield the lower and upper fractional-Gumbel integrals with L^-alpha and L^-beta probabilities. Uniform exponentially integrable upper estimates justify dominated convergence and conditional weak limit of scaled latent U. At the *unshifted* lower endpoint, the transition s~(log L)/2 gives (A_-/alpha)(log L/(2L))^alpha; the upper unshifted endpoint has N normal-tail factor (4pi L)^-1/2 and beta integral Gamma(beta), yielding A_+Gamma(beta)L^(-beta-1/2)/sqrt(4pi). Independently evaluated the exact one-dimensional normal-mixture integrals at N=10^8 and 10^20: rescaled lower values 0.13305 and 0.12178 versus limit 0.11171, upper 1.0200 and 1.05361 versus limit 1.07541, the predicted directions of convergence. These are numerical diagnostics only.

## originality

PASS

The stationary Gaussian beta-type mixture, conditional independence and compact limiting support are already the primary 2024 result. The analogous fractional-Gumbel smoothing and extra half-power above an upper edge in a resetting gas were derived in an earlier published 2026 finding. The best-of-knowledge surviving information is the paired LOWER and UPPER profiles for finite-rate two-stiffness SWITCHING, their distinct raw-edge powers, and both conditional environment laws; the reset model is a singular physical limit, not the asserted full two-sided finite-switching theorem.

## value

PASS

At fixed positive trap-switching rates, the stationary maximum has two natural endpoints but their finite-N probabilities decay at different logarithmic exponents. The sharper raw-edge enhancement/suppression and conditional latent-variance distributions distinguish the two environments and give useful rare-event benchmarks for correlated Gaussian extremes; this is a mathematically motivated asymptotic classification beyond known leading compact support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
