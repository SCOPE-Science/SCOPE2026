---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: For λ,D>0, q∈(0,1), 0<δ≤μ<∞, the OU variance ODE yields σ_t²=(D/λ)[1-(1-q)e^{-2λt}], and Gaussian symmetric KL reward f(t)=c²(1-e^{-ωt})²/[2(1+c(1-e^{-ωt}))], c=(1-q)/q, ω=2λ. Independent symbolic differentiation verifies exactly f''=(c²ω²/2)(1-y)(2-4y-3cy²-c²y³)/(1+cy)³. Its cubic decreases strictly and has one zero. The tangency residual hδ(t)=(t-δ)f'(t)-f(t)+f(δ) increases until t_inf and then decreases to the strictly negative limit f(δ)-f(∞), hence for δ<t_inf exactly one bδ>t_inf, and none for δ≥t_inf. Joining the supporting chord δ--bδ to the strict-concave post-bδ curve produces a global concave majorant; Jensen, strict contact sets and the prescribed mean identify the unique optimum: two atoms at δ,bδ for δ<μ<bδ, deterministic otherwise, with boundary cases μ=δ and μ=bδ. Finite mean/bounded reward permit renewal-reward, even with heavy-tailed admissible intervals. Independent high-precision roots for c=1,ω=1,δ=.2 give t_inf=.47609687563148 and bδ=.66175510208479, with supporting-line checks, while the universal claim rests on calculus, not the grid. No assertion about pathwise thermodynamic entropy production.

## originality

PASS

PASS (best-of-knowledge; qualified): A published earlier Gaussian OU renewal-clock theorem solves the same Jeffreys divergence at fixed mean with merely W>0 and NO positive minimum interval. It has an unattained burst supremum when the mean is below its critical time and states that positive dwell constraints change the feasible class. The present lower-bounded constraint δ>0 changes the exact concave envelope and yields a new attained two-atom law with a δ-dependent tangent and unique transition: not an equality or fixed-parameter corollary of that earlier statement. The underlying one-inflection lemma and concavification approach, plus Farago's Gaussian reward and physical interpretation, are not new. Priority against a more general constrained one-inflection envelope theorem remains an explicit risk.

## value

PASS

PASS: A strictly positive minimum physical dwell time is a natural constraint, not an arbitrary slice. It eliminates a nonattained zero-wait supremum, produces an achievable optimal renewal schedule with a sharp deterministic-versus-random transition, and gives the explicit parameter boundary bδ. This is a motivated exact structural classification for renewal controls of a fixed physical information reward, despite the classical Jensen/envelope method and without claiming implementation-wide dissipation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
