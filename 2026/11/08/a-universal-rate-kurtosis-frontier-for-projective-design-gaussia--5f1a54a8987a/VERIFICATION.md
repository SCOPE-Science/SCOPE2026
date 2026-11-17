---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For a planar iid rank-one orthogonal projector P with E P=I/2 and E(uᵀPu)²=3||u||⁴/8, A=I−ηP has exact directional squared contraction ρ=1−b/2 and quartic multiplier t4=1−b+3b²/8, b=η(2−η)>0. Synchronous coupling contracts W2 and quartic drift gives unique stationary finite fourth moment; q=(1−ρ)s enforces covariance sI. The homogeneous quartic operator contracts by t4, forcing a unique radial directional fourth moment m=3s²(8−2b)/(8−3b), so κ=3b/(8−3b)=3(1−ρ)/(1+3ρ). Since b≤1 with equality only η=1, fastest synchronous squared contraction ρ=1/2 has κ=3/5. Independent exact symbolic three-pair-projector design identities and 21 rational parameter cases corroborate. This says nothing about total variation or SDE discretization.

## originality

PASS

Prior scalar random-coefficient autoregression explains non-Gaussian stationary laws and random-batch methods explain randomized interaction algorithms; the inspected formulas do not give the new planar projective-second-moment-design invariant quartic law or exact κ–ρ relation for calibrated isotropic Gaussian forcing. Published isotropic noisy Kaczmarz fourth-cumulant attenuation uses a different noise mechanism. Residual risk: a general matrix-affine moment formula could imply this case; no exhaustive priority claim.

## value

PASS

Covariance calibration is a standard validation target for stochastic numerical samplers, but it need not control non-Gaussian higher moments. The exact unavoidable fourth cumulant and its inverse tradeoff with synchronous contraction rate supplies a useful quantifiable algorithmic warning and natural projective-design universality, not a lone tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
