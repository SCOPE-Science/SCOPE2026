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

Modulo constants, real BV functions are integrals of interior unit steps against their finite signed distributional derivatives. The triangle inequality gives the norm upper bound by a maximal step, and a step attains it. The change x=cos θ takes normalized arcsine measure to dθ/π; the step's coefficients at k≥1 are √2 sin(kθ)/(πk). Parseval gives the nonnegative cosine tail, reflection symmetry, and the degree-zero optimum 1/2. At 2nδ=c, the scaled tail is a Riemann sum for G(c)=∫₁^∞(1−cos(ct))/t² dt, locally uniform by truncation at large t. Integration by parts gives G′=π/2−Si(c). Alternating Taylor bounds give Si(2)>π/2 and G(2)>1.34559>4/3. Si is strictly increasing before π, G is convex on [π,2π], and G(c)≤1+2/c for c≥2π by integrating the cosine tail by parts. These certify that its first stationary point is the unique global maximum. For 2nδ→∞, Abel summation bounds the scaled oscillatory part by O(1/(n sin δ)) and the nonoscillatory part tends to 1. Comparing to c*/(2n) excludes this escape for every maximizing sequence; all remaining subsequential limits equal c*. The Taylor expansion of 1−cos δ then gives the n⁻² endpoint distance.

## originality

PASS

Best of the inspected evidence for the sharp normalized BV-to-L² residual and its moving maximizer law. The exact indexed match is the frozen record itself. The nearby periodic and Chebyshev projection results do not give the same norm, and pointwise localization of a prescribed singularity does not give the maximizing step location or constant.

## value

PASS

This is a natural sharp approximation norm for a canonical weight and a class that allows discontinuities. The result shows why plugging fixed jumps into a pointwise or global rate misses the worst case: their limiting constant is smaller and the optimizers cluster on an n⁻² spatial endpoint scale. It provides both an all-degree exact expression and a sharp asymptotic mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
