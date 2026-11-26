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

For fixed d≥2, Plancherel gives the supremum of the multiplier difference on √t·Z^d, not the L² distance between kernels. At fixed Euclidean radius the signed extrema necessarily use opposite endpoints of the sharp ℓ¹/ℓ² ratio interval: the Poisson-minus-heat maximum uses axes and the heat-minus-Poisson maximum uses equal absolute coordinates. The critical equation h=log(2u/a)+au−u²=0 has exactly two simple roots because h is strictly concave, h(a)=log 2, and the limits at both ends are −∞. The scalar maxima have opposite strictly signed derivatives. Their limits at the two ends follow by bounding the unfavorable wing on u<a or u>a, and testing u=a^(−1/2) on the favorable wing. This gives the unique transverse crossing and its strict increase in error with d; the crossing calibration must tend to zero, since a positive lower bound would force the increasing wing to 1 while the decreasing wing stayed below 1. Rounding on the two special rays costs O_d(t) uniformly on compact calibration intervals by vanishing radial first derivatives. Fixed lattice witnesses at calibrations on either side exclude all escaping minimizers by signed pointwise monotonicity; compactness gives attainment and the nonzero one-sided slopes give an O_d(t) calibration displacement for every minimizer. The direction statement is limiting, not a claim of exactly equal lattice magnitudes at every t. Indeed at fixed integer ℓ¹ radius, negative-wing maximizers concentrate all mass in one coordinate and positive-wing maximizers balance magnitudes to within one. Reviewed RESULT.md lines 13–66, VERIFICATION.md and check.py; the latter compares six sampled dimensions, not six consecutive dimension increments. An independent bounded direct scalar maximization gave (c₂,E₂)≈(0.78155787578,0.20968189592) and (c₃,E₃)≈(0.71242187012,0.24296641228); this is a numerical cross-check only. No uniform-in-d remainder or formal certificate is claimed.

## originality

PASS

The supported distinct claim is the fixed-d product-generator operator-norm minimax, including its two different extremizing geometries and sharp lattice calibration rates. Neither kernel-norm calibration on the circle nor square/area-function bounds supplies it. This is a best-of-current-knowledge decision, not historical priority certification.

## value

PASS

The optimized norm is a concrete measure of whether product-Poisson smoothing can substitute uniformly for heat on L² across frequencies. The sharp positive obstruction, competing explicit worst directions and worsening with dimension are informative beyond a qualitative inequivalence of generators. The stationary O_d(t) control transfers the continuum comparison back to integer modes and specifies the time of every optimum, not just one admissible choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
