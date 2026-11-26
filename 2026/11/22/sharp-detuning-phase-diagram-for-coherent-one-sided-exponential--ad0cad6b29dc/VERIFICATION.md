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

Summing the causal geometric series on 0≤x<1 gives a uniformly bounded Zak extension to its closed one-sided cell; an edge zero lowers the essential infimum because the open cell approaches it through sets of positive measure. The numerator is U-rzV with U=1+c exp(-iθx), V=exp(-iθ)+c exp(-iθx); U and V cannot vanish together. The unit-circle criterion is Q=q(1+c²)+2cF=0, with F=Re[(1-r² exp(iθ)) exp(-iφ)], φ=θx. Q(0)>0. For θ≤π, F decreases to F(θ); requiring its minimum to be ≤−q gives r≥cos(θ/2). For θ>π, its unique minimum −|1-r² exp(iθ)| is interior (the displacement of the cosine places the minimum before the edge, where F′(θ)>0). The quadratic roots from these minima are positive reciprocal endpoints, including the singleton at onset; at h=1/2 they are (1±r)/(1∓r). The initial rising branch in the long regime is already above the target level; after the minimum a second open-cell intersection occurs precisely for Q(θ)>0, or an edge zero at equality. Tangency at the two long-regime amplitude endpoints and the short-regime one-sided edge behavior follow from the same geometry. The claimed conservative frame bound uses r^x≥r and the upper denominator bounds; inverse Fourier transformation gives the stated two distinct equally elevated Cauchy poles. Independently checked eight phase and boundary examples by harmonic roots and direct Zak sums, including the half-frequency endpoint and the long-detuning E=0 boundary: python3 /workspace/reproductions/check_frozen_math.py 3. No uploaded checker was executed; finite examples are corroboration only.

## originality

PASS

Pass is for the complete detuning classification and zero-geometry extension beyond h=1/2, which the finding explicitly credits. The strongest located predecessor treats a single detuning and cannot fix the movement of the cosine minimum through the cell edge as h varies. The general Zak criterion yields the starting test but does not evaluate the phase-constrained minimum or count its level crossings. No equivalent statement was identified in the material actually read; several pertinent full texts were not accessible.

## value

PASS

A critical two-tone window is a natural next case after the single pole and half-frequency slice. An explicit reciprocal forbidden amplitude interval is directly useful for choosing stable windows; the change from edge loss to an interior tangency, with a two-zero chamber, supplies more than a positivity check or a reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
