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

Discrete differentiation commutes with convolution, and the unit step has derivative δ₀, so the variation norm equals the convolution kernel's ℓ¹ norm for each power and is attained. For u=1/8+λ/r the two contacts of 1−4u(1−cosθ)² have orders four at 0 and two at π; the Nyquist peak has sign − and peak modulus ρ_r=1+16λ/r. Its powered height converges to exp(16λ) uniformly for compact λ. To check the tail estimate, on a small neighborhood divide the absolute symbol by its peak height and take its smooth log g. There g≤−c|s|^p and g^(k)=O(|s|^(p−k)) for k≤p, with higher derivatives uniformly bounded (p=4 or 2). With d∼r^(1/p), derivatives through order four of r g(v/d) are bounded by polynomials in |v| uniformly on the rescaled cutoff; the exponential and its derivatives are then dominated by a polynomial times exp(−c'|v|^p). This gives O(d³) for the fourth derivative's L¹ norm before rescaling and a uniform O(R⁻³) for the ℓ¹ mass outside |j|≤Rd. Uniform local convergence and Riemann sums give the quartic and Gaussian masses. Off the two neighborhoods a strict uniform modulus gap with two derivative bounds makes the coefficient remainder o(1) in ℓ¹. At radius r^(3/8), the Gaussian mass inside is O(r^(-1/8)) and the quartic mass outside O(r^(-3/8)); hence the loss from combining them before taking absolute values tends to zero. Fixed u on either side leaves only the corresponding dominant peak, and the second signed moment of the unit-mass quartic inverse transform is zero, forcing sign change and L₄>1. Independent cosine and absolute-integral quadrature at mesh pairs (.01,.025), (.007,.01), (.005,.005), truncated at s=4 and z=50,60,70 respectively and doubled by symmetry, gave 1.2372919, 1.2372952, 1.2372945; this checks the displayed rounded value but is not the asymptotic proof. The uploaded checker was inspected, not executed.

## originality

PASS

Substantial existing coverage of the identical fixed-parameter stencil and both contact orders is verified. The distinct result is the sharp global ℓ¹/BV limit through the moving u=1/8+λ/r layer, compact-uniform in λ. The inspected pointwise limit and uniform boundedness statements do not imply that limit or its two masses by substitution; controlling their absolute masses and their interaction at two spatial scales is essential. No claim of priority for the stencil, threshold, contacts, or individual Fourier profiles.

## value

PASS

The natural stability boundary for the five-point biharmonic iterate has a sharp transition profile in an attained operator norm. It isolates a positive mass that is invisible in the leading coefficient asymptotic and shows why adding absolute masses is legitimate despite two peaks contributing to every spatial site. This is useful for finite-variation stability of the bilateral scheme and is more than the already known criterion for fixed-parameter boundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
