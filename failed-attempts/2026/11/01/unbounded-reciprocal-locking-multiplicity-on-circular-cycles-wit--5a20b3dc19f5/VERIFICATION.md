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

For odd m=2q+1, 1+(-1)^(q+1)U_(2q)(x) is even and zero at x=0, hence divisible by x². The quotient defining h_m is analytic at both cosine zeros; h_m(0)=0. On a thin annulus the phase is strictly increasing in the angle and differentiation gives dot Theta_i=omega exactly. Thus the increasing phase-zero sections are radial at angle zero, the periods are 2pi/omega, and the radial contractions give the prescribed transverse multipliers. At r=1 the phase gradients are e_theta and e_theta+h_m e_r, yielding a cos(theta) and (-1)^(q+1) sin(m theta) for the two translations. H_m(psi) is their reciprocal difference. At the 2m alternating extrema of the sine, a<1 preserves alternating signs. Multiplication of the Laurent polynomial by z^m bounds the total root multiplicity by 2m. Thus the 2m roots are simple with m slopes of each sign, and H_m(0)=-a excludes simultaneity. To check local persistence independently, take a section just before oscillator 1 emits, with two radial coordinates and relative phase. In a small neighborhood of each root the crossing order is fixed and receiver states are away from their own emission sections at both kicks. The local return is smooth in state and epsilon by transverse crossings. At epsilon=0 the radial part is the diagonal contraction with the prescribed multipliers and the relative phase is unchanged. The phase displacement divided by epsilon extends smoothly there, and on the cycles its epsilon=0 value is H_m, because the relative phase changes only at the kicks. The fixed-point equations have a block-triangular Jacobian at epsilon=0 with the two nonzero radial displacement derivatives and H'_m. The implicit function theorem, followed by the simple eigenvalue perturbation at 1 (the off-diagonal couplings in the return are O(epsilon)), gives the relative multiplier 1+epsilon H'_m+O(epsilon²). The other multipliers stay inside the unit circle, even if their limiting values coincide. This proves the simultaneous local persistence and the stable/saddle counts. Finally the effective field e_x-a cos(psi)e_theta has distance at most a<1 from e_x, giving winding zero and signed difference +1 from the cycle tangent. The m=1 case needs no exception: the shear vanishes and the balance still has two simple roots.

## originality

FAIL

The central witness of arbitrarily many stable and saddle locks at fixed winding under fixed reciprocal Cartesian translations on identical unit-circle cycles is already given by Resultary a632e71d1e14. On m=4M-1, a=1/2 and omega=lambda_1=lambda_2=1 the full realization and exact leading counts coincide. The differences in theorem wording are real but do not constitute a distinct construction: the other odd class follows from a single sine addition identity on the earlier shear, and the free a, angular speed and contractions are direct parameter extensions of the same argument. This is a rejection for verified core overlap and a mechanically obtainable extension, not a claim that the prior writes the full strengthened quantifiers verbatim.

## value

FAIL

An unbounded multiplicity witness with fixed winding is a useful sharpness test of the cited lower bound, but the earlier construction already gives exactly this test under the same physical restrictions. The only additional precision is filling a residue class of harmonic orders and allowing direct calibration of kick ratio, angular speed and radial decay factors. In this statement that does not establish a new winding obstruction, a new regime of coupling, or a differently motivated exact threshold; it is a routine extension of the existing witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
