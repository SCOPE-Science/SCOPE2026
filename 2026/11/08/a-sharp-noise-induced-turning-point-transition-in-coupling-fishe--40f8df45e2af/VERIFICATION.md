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

Stationary covariance solves K_b Sigma+Sigma K_b=2 diag(1,1+d) uniquely for |b|<1, giving the specified Gaussian snapshot FI F(z,d), z=b². Independently checked symbolic Lyapunov solution, Gaussian Fisher trace identity, and exact derivative factorization ∂zF proportional to cubic P(z,d) with negative denominator. P(0,d)<0, P(1,d)<0, and P_zz<0 on 0<=z<=1; hence only zero or two interior simple roots or one double root. P/d^4=A(z)-sum_{j=1}^4 B_j(z)/d^j with all B_j>0; the maximum is continuous and strictly increasing from negative to positive, so there is exactly one transition at d*=33.219537333... z*=0.1389386404..., which independently solves P=P_z=0. Nondegenerate double root gives square-root split; large d root scaling z_-~4/(3d), z_+→(9-sqrt57)/4. Formula is for known d, not the marginalized nuisance Fisher information. Critical numerical digits are uncertified approximations; uniqueness is analytic.

## originality

PASS

Best-of-knowledge targeted statement comparison against actual published same-object sources. The existing general principles and any known same-size phenomena are explicitly credited; the surviving contribution is the precise additional scoped statement (see four checks and residual risks).

## value

PASS

Sharp global qualitative-to-quantitative transition in a physically motivated, exactly solvable two-coordinate nonequilibrium stochastic model: precise noise threshold, two-turning-point count, bifurcation singularity and asymptotic branch scales. The source paper already notes qualitative nonmonotonicity and gives the FI formula; the complete one-threshold classification is additional and potentially useful for coupling identifiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
