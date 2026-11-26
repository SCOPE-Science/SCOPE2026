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

At positive even L, return is exactly the all-even multinomial event. Multinomial sequence counts give the cosh coefficient PGF and all falling moments, including r=0 and r=d. Exponentially tilted even-Poisson site sizes conditioned on their sum reproduce precisely these weights. At fixed density the tilt tends to a finite positive value. The support points (1,0),(0,1),(0,2) of (zero indicator, half site size) generate the full difference lattice and a positive definite covariance. The 2D Fourier local CLT is uniform for tilts in a compact neighborhood of the limit (uniform exponential moments and off-origin damping). Dividing by the 1D local CLT at its exact mean, summing on bounded normalized intervals, and using that the resulting normal density has total mass 1 proves conditional weak convergence with the stated Schur complement. No replacement of the actual centering by its limit is used. The strict mean-fraction inequality follows from the increasing positive difference λ tanh λ − log cosh λ. Independently, for the critical window let Q_m be even-time return probability on m coordinates. The parity Fourier formula is Q_m=2^{-m} Σ_j binom(m,j)(1−2j/m)^L. The two endpoints contribute 2^{1−m}; the remaining sum relative to those endpoints is at most (1+exp(−2L/m))^m−1=o(1) for m=d or m=d−r (fixed r), by reflection and the bound on j≤m/2. Thus Q_{d−r}/Q_d→2^r. Omitting r designated coordinates contributes the unconditional factor (1−r/d)^L and gives exactly a uniform (d−r)-cube walk; the conditional factorial moment is therefore (d)_r(1−r/d)^L Q_{d−r}/Q_d→(2e^{−c})^r. The Poisson moment argument gives weak convergence and the zero mass (use a half-integer cutoff); the unconditioned moments omit the Q ratio. This independently verifies the factor of two and the positive d log 2 shift of equal-probability coverage levels. Small exact coefficient tests corroborate only the finite identity.

## originality

PASS

Best-of-knowledge pass for the quantitative endpoint-conditioned support law, particularly the doubled critical-window intensity, not for the occupancy encoding, the conditional local-limit method, or ordinary coupon collection. In the strongest distinct Resultary comparison the unconditioned distinct-direction count is the same observable after complementation, but its joint second moments with displacement do not identify its law on an exact return. The exact catalogue hit is the target record itself. The inspected hypercube sample-path abstract studies vertex coverage, not direction coverage. Potential older full-text implications remain an access risk, not a negative result.

## value

PASS

Coordinate support describes which face contains a conditioned path; it is distinct both from endpoint displacement and from vertex coverage. The result quantifies endpoint conditioning in two regimes with observable changes: a different mean fraction and conditioned variance at fixed density, and twice the missing-direction intensity (one explicit d log 2 shift) at critical coverage. The latter is a sharp boundary-sensitive comparison at the same time and dynamics, not a known unconditioned coupon count relabeled as a bridge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
