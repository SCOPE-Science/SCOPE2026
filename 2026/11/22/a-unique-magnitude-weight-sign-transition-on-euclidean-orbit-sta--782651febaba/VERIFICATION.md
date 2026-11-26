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

The positive mixture of Gaussian distance kernels is strictly positive definite on distinct Euclidean points; uniqueness and rim transitivity reduce the system to the constant-on-rim sector. In the center plus unit rim-indicator basis the determinant is Q−nE²>0, with E=e^(−rt) and Q=Σe^(−tℓ_j). The rim weight is (1−E)/(Q−nE²)>0, while the center sign is the sign of Σe^((r−ℓ_j)t)−n. This function has value zero at zero, slope n(r−mean chord), everywhere positive second derivative and divergence at infinity (the self-chord has length zero). That proves both cases including equality; the microscopic denominator 2r−mean chord is strictly positive. For polygon rims the mean chord is (2/n)cot(π/(2n))>1. The continuous analogue has initial slope 1−4/π<0, strict convexity and divergence from any interval of chord length less than one, giving a unique simple positive zero and D>0. The uniform Euler–Maclaurin endpoint jump is 4πt, so the average differs from I(t) by πt/(3n²)+O(n⁻⁴). Uniform convergence traps the root on both sides of the simple limit, and solving first for O(n⁻²) error then substituting yields the sharp coefficient. For divisibility, there is a direct check independent of the Fourier proof: f_t(x)=exp(−2t sin πx) is strictly convex on [0,1], since f_t''/f_t=4π²t² cos²(πx)+2π²t sin(πx)>0. The endpoint-matched sum is the trapezoid rule; any proper panel refinement strictly decreases its value while it remains strictly above the integral. Evaluating at the unique roots gives t_n<t_mn<t_∞, only a divisibility ordering as claimed. Independent quadrature gave t_∞≈1.36351481573219, D≈0.06794808738018 and coefficient ≈21.01412167889. The supplied checker and verification note were inspected, not executed; numerical values are corroboration only.

## originality

PASS

The exact microscopic endpoint and symmetry-reduction method have verified antecedents. The supported distinct result is the classification at all positive scales including equality, coupled to the sharp vertex-polygon threshold expansion and divisibility order. The compared microscopic, circumcenter-criterion, block-constant and polygon-chord results do not state or imply that combined law. Euler–Maclaurin and nested trapezoid ordering themselves are standard.

## value

PASS

Scale-dependent signs determine when the weighting of a natural one-point extension is positive. The classification yields a sharp, easily computable geometric criterion beyond a microscopic limit, and regular polygons give a canonical discretization with a sharp bias in the scale of positivity. The value is in the classification and correction, not the routine two-by-two solve or quadrature in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
