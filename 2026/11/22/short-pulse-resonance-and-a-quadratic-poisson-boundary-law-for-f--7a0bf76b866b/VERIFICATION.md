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

The derivative of a periodic real BV input has equal positive and negative masses V/2. Coupling them represents the input modulo constants by V/2 times an average of arc indicators (the derivatives agree as measures). The triangle inequality gives the upper bound and an arc of variation two gives equality. Pairing positive and negative Fourier frequencies and dividing by four gives the coefficient 1/(2π²) in (1). With h=t^(1/α), the arc sum divided by h has grid spacing 2πh and converges uniformly at bounded d/h to (∫g−F(d/h))/(2π). One integration by parts gives ∫g=2Γ(1−1/α)(1−2^(1/α−1)). The oscillatory part is O(h/sin(πd)) by summation by parts and integrable g', so diverging d/h gives only B; d/h→0 gives zero. For the Fourier tail, for p in a compact subset of (−1,2), subtract the damped uncut power u^p exp(−δu) from its cutoff version. The difference vanishes near zero and its third derivative has uniformly bounded L¹ norm for δ↓0 (outside the cutoff, the derivative terms are bounded by multiples of u^(p−3)). Three integrations by parts and the damped Gamma integral give the stated cutoff coefficient with O(z^(−3)) error. For fixed α, if the second power 3α−2 exceeds 2, the remainder after the first term already has integrable third derivative; at the integer value 2 its cutoff transform is rapidly decaying. Thus the leading coefficient Γ(2α−1)sin(πα) is strictly negative, forcing compact positive minimizers and the strict short-pulse improvement. Near α=1 the first unused power is p=2+4ε times a smooth function of u^(1+ε). The only potentially singular third-derivative term has the factor p−2, whose product with ∫₀¹u^(p−3)du is bounded, and it vanishes at ε=0. This makes the two-term expansion uniform. At α=1 the displayed positive Laplace mixture yields F₁(z)>0 at every finite z, so the negative minimizers escape as ε↓0. If εz→0 their positive second term dominates: the negative-to-positive ratio is O(εz^(1+ε)), which tends to zero since z≤1/ε eventually; the remainder is smaller as well. If εz→∞, all terms are o(ε²), worse than the test value at z=2/(πε). On the intervening compact εz scale, the limiting profile 1/u²−π/u has its unique minimum −π²/4 at u=2/π, proving both limits and the coefficient π/8 after dividing by 2π.

## originality

PASS

The distinct supported claim is the optimized interior stable-order short-pulse law and especially its singular boundary at order one. Arc extremality and a shrinking pulse also occur in closely related exact work, so they are not counted as new unrestricted principles. The strongest Gaussian exact match is at order two only and supplies neither the sign mechanism of the interior fractional tail nor the quadratic Poisson-boundary coefficient and length scale.

## value

PASS

The exact norm distinguishes interacting, vanishing-length arcs from independent separated jumps. The strict gain for every interior stable exponent, positivity at the Poisson boundary, and simultaneous quadratic gain and diverging rescaled pulse length explain where that effect disappears. These resolve a concrete sharp-constant and structure question beyond the general method of reducing to arcs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
