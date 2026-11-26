---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Substitution in the constant-step method gives the stated zero-prehistory Green function. With s=5/(5+3μ), the discriminant is −27s²(10s²−14s+5)/500<0. The one real root R is positive; s=10R³/(15R²−6R+1) increases on (0,1), and m²=R²/(15R²−6R+1) for the conjugate modulus. The denominator is greater than R² and equals one at R=2/5 in (0,1), giving Schur stability and the exact dominance switch. Simple poles give a positive real amplitude and a nonzero complex amplitude. A dominant positive real mode is eventually positive; a dominant complex pair has both signs infinitely often because its rotation is dense or else a nonzero finite-period cosine has zero mean. At μ=15/16 the roots are 2/5 and (7±i√51)/25; independent exact residue calculations give A=5/3 and squared pair-to-real amplitude ratio 20/17. Irrationality follows from the rational nonintegral value 2cosθ=7/5, ensuring both signs even at equal moduli. The stated G_6 was reproduced by an independent ordered-composition expansion, not by executing the uploaded recurrence script. The signed gain is one from the absolutely convergent generating function at z=1; the sum of absolute coefficients is larger if any coefficient is negative. For the background A-stability, a unit amplification root with inverse w requires Re(3μ)=2(Re w−1)^3, so the closed right μ-half-plane has no crossing except the simple consistency root at 0; roots tend to zero as |μ| tends to infinity there, giving the stated stiff decay.

## originality

FAIL

The eventual sign frontier is mechanically implied by the earlier Oct. 26 general-history analysis, including at equality. To see the exact match, set d=10+6μ in the earlier recurrence and take initial history (1,0,0). It has y_{n+3}=G_n/d for n≥0. The published geometric-history amplitude identities are algebraic in the starting value t, so t=0 gives the amplitudes for this history without a new spectral argument. The real amplitude is positive and the pair amplitude is nonzero; at the crossing the ratio 2|pair|/real equals |R−u|/|Im u|=√(20/17). The same earlier proof supplies the identical irrational endpoint angle, so density resolves the equality case for this history as well. A negative coefficient there and continuity already imply a transient-negative interval on the eventual-positive side. Independently, a distinct same-date CQ record gives the identical generating function up to a positive scalar, with a stronger all-index theorem, the identical sixth-coefficient quartic, and a negative sixth coefficient on a whole interval containing 187/200. The gain conclusion is the signed-mass normalization plus the elementary strict increase on taking absolute values. Neither the rational evaluation nor an all-index positivity recast is a distinct valuable repair. Rejection does not presume an order for same-day releases: the earlier general-history implication is sufficient for the central frontier, and the exact same-day overlap is reported separately.

## value

PASS

As a mathematical diagnostic, eventual sign versus all-index positivity matters for bounded nonnegative forcing: nonmonotonicity of the normalized causal response can occur below the asymptotic oscillatory boundary. This is a useful structural distinction in a natural stiff integrator. The isolated exact rational evaluation would not be independently valuable as a repair once the identical stronger positivity analysis is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
