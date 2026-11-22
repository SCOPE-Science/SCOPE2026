---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Dimensionless reversible Langevin generator L=∂²−V'∂ with V=x⁴/4−ρx²/2 and stationary Gibbs density gives the Poisson-energy formula F=2Z^{-1}∫e^V J². Direct substitution yields J(x)=(√π/2)e^{ρ²/4}erfc((x²−ρ)/2) and a square-integrable corrector. After u=x² the partition function Z=e^Q∫u^{-1/2}exp(−(u−ρ)²/4)du has Gaussian-saddle coefficients a_k=(4k)!/[16^k(2k)!k!], as does the interior barrier integral B=∫_{−√ρ/2}^{√ρ/2}exp(−ρx²/2+x⁴/4)dx under x=√(2/ρ)z. On the barrier J is √π e^Q times a negligible error, and outside it the integrand is exponentially subdominant compared with π e^{2Q}B, so arbitrary fixed-order Laplace expansion makes the two full algebraic series cancel in 2πe^{2Q}B/Z. Therefore F=√2 π exp(ρ²/4)(1+O_N(ρ^{-2N})) for every fixed N, with no stronger uniform-N or exponential-error assertion. Independently derived the two coefficient formulas and verified exact equality for k=0,...,9 using rational arithmetic; high-order finite checks corroborate only the coefficient identity, not the Gaussian tail estimates.

## originality

PASS

The same quartic stationary correlation integral and leading Kramers limit existed in classical Brownian double-well literature, and this is expressly credited. The claim is narrowly the all-orders vanishing of polynomial corrections for the unnormalized integrated position covariance, which the inspected prior first-order normalized correlation-time formulas do not provide; best-of-knowledge originality with a genuine strong implicit-coverage risk.

## value

PASS

The exact absence of every inverse-power correction for a natural double-well additive diffusion and its integrated phase is a delicate analytic rigidity statement: two separately nontrivial full saddle series cancel. Knowing this exact asymptotic structure changes high-barrier approximation practice and distinguishes normalized correlation times from physical phase-variance growth. The known integral alone does not make the cancellation a routine textbook deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
