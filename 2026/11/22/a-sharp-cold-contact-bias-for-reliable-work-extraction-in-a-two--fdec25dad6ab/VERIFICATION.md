---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two OU variance maps give the stated periodic variances and covariance √a V₀. Write Δ=V₁−V₀ and D=det Cov(X₀,X₁)=H(1−a)V₀>0. Then Wick's variance expression uses T=Δ²+2D, while the correlation between the Gaussian sum and difference is Δ/√(Δ²+4D). The work sign is the product sign, so the exact arcsine probability and mean/standard-deviation ratio are both strictly increasing in Δ²/D in the engine regime Δ>0. In u=(a−z)/(1−a) the variances scaled by C are (hz+u)/(z+u) and (h+u)/(1+u), respectively. Thus Δ²/D is a positive constant times u²/P(u) where P=(z+u)(1+u)(hz+u). Its derivative has the sign of 2P−uP′=2hz²+z[h(1+z)+1]u−u³, independently confirming the claimed cubic and prefactor after the change of variable. This cubic sign expression has exactly one positive zero and is strictly positive at u=√z, so the maximizing hot dwell is shorter than half. The mean instead maximizes 1+z−a−z/a at a=√z. At z→1 the limiting cubic factors as (u+1)(u²−u−2h); at z→0 rescaling u by √z gives the positive limiting root √(h+1), yielding both timing laws. Independent bisection for h=2 and 2λτ=2 gives hot fraction 0.344570234 and success probability 0.561633965. The archived verifier and notes were inspected, not executed. The calculation is for one stationary cycle with equal coordinate relaxation, not accumulated correlated work.

## originality

PASS

The sampled harmonic OU covariance, Gaussian quadrant identity, and reliability metric are standard ingredients. The contribution is the global joint optimization over thermal-contact times, its explicit cubic and strict cold bias, and its contrast to the mean optimum. The strongest inspected results overlap in model, metric or time allocation, but do not cover that combination.

## value

PASS

For a stochastic engine, a time split that improves the probability of genuinely extracting work need not maximize mean work. The exact, persistent separation between those optima is a structural result, and the cubic and small/large-duration limits make it a useful benchmark. It is not merely the small numerical gain in one example, nor does it imply long-run reliability or optimal control under unequal mobilities and rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
