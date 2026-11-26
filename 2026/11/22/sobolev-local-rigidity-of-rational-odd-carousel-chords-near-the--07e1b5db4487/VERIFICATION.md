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

For each fixed coprime 1 ≤ p < q, odd q ≥ 7 and s > 3/2, the derivative at the circle is convolution against −4 sin δ sin(u−δ) on 0 ≤ u ≤ 2δ (δ=πp/q); its Fourier integral gives (1) including the sign and phase. For |m|≥2, vanishing would imply tan(mδ)=m tan δ. With Q=q/gcd(q,m)>1, the field norm of the root-of-unity identity gives m^{φ(q)}Φ_q(1)=Φ_Q(1)^{φ(q)/φ(Q)}; Q=1 is immediately impossible. The denominator norms are one since Φ_j(−1)=Φ_{2j}(1)=1 for odd j>1, and Φ_Q(1)^{1/φ(Q)}≤√3 by the prime-power formula and the decrease of log(r)/(r−1). This excludes all finite resonances. The uniform-in-m odd residue bound |cos(mδ)|≥sin(π/(2q)) then gives two-sided order −1 ellipticity, with finitely many low modes handled by nonvanishing. The mean fixes rotation and the closure derivative is an isomorphism on the real first harmonics; the closure graph is analytic with zero first derivative. Integrating the analytic H^s exponential gains one derivative even with the exceptional multiplier at −1, so projection to modes |m|≥2 followed by the Banach inverse theorem gives the estimate in exactly the indicated norms. Sharpness follows by taking the amplitude derivative on each closed branch through cos(mt) and then m→∞ through multiples of q, on which the H^{s+β}/H^s derivative ratio tends to zero for β<1. Positive curvature for small H^s perturbations and total turning 2π give the required convex embedded curves. RESULT.md lines 29–97 provides a proof independent of finite tests; checker.py and VERIFICATION.md were inspected, not executed. The description of first harmonics as translation-related in line 101 is imprecise (translations do not affect the tangent), but the closure calculation is correct.

## originality

PASS

The supported distinct claim is the closed-curve, nonlinear, sharp Sobolev inverse estimate for fixed rational perimetral chords at every odd q≥7, and its local rigidity consequence. Related resonance equations and lower-denominator or differently parametrized results do not supply that estimate. This is a limited priority assessment, not a claim that the tangent equation or all local carousel methods are new.

## value

PASS

The work treats a natural family of rotationally prescribed chord data beyond the known small polygon cases. It turns qualitative uniqueness into a stable recovery bound and proves the exact regularity cost; in particular q=7 receives a concrete local theorem without assuming a global carousel classification. Nonresonance across all odd denominators is substantive, and the estimate is useful even when lengths are only approximately equal. No global floating-body result or parameter-uniform constants are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
