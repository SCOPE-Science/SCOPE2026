---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The statement is about the Euclidean derivative inverse of a single planar cell, not an end-to-end solver. AP has positive real eigenvalues by SPD similarity, so J=I+AP is invertible, and nonexpansivity is equivalent to JᵀJ−I⪰0. In r-aligned coordinates, u,v>0 imply positive trace for this symmetric test matrix, so its determinant is decisive. With d=ατ, S=α+τ, D=α−τ, z=cos 2θ, and K=(1−γ)²D²/4, direct expansion gives dγ[4+S(1+γ)+γd]−dγD(1−γ)z−K(1−z²). If D=0 this is positive. Otherwise completing the square gives the advertised vertex z₀=2dγ/[D(1−γ)] and minimum F=dγ[4+S(1+γ)]−K. If z₀≥1, then K≤dγD(1−γ)/2, which implies F>0 because S>D and γ>0. Thus every negative or zero unconstrained minimum is physically attained. F increases strictly in γ with F(0)<0<F(1), proving the threshold and all strict and equality cases. Independent fractional arithmetic gives det(JᵀJ−I)=−2853/2000 and det(sym J)=123591/40000 in the rational example, and direct bisection gives γ*=0.0542649822871. The checked example shows monotonicity is not a contraction test for the same pair. Frozen verify_inverse_frontier.py was inspected, not executed; finite samples do not establish the continuum result.

## originality

FAIL

The inverse test is exactly the published pointwise vector-play monotonicity test at a reciprocal, rescaled pair. The same prior angular determinant polynomial then gives the entire threshold and attaining orientation by routine completion of the square. This is positive coverage by implication, not an assertion that the paper states the inverse theorem verbatim, and not an inference from the unrelated unshifted monotonicity sufficient condition or positive eigenvalues.

## value

FAIL

Inverse conditioning is well motivated in a local magnetic constitutive solve, and the rational witness is pedagogically useful. However, the frozen frontier is the elementary all-angle envelope of an existing exact pointwise formula at reciprocal parameters. The extra example is a routine specialization of those tests, not a distinct structural witness requiring a new argument. As a standalone finding it supplies no nonmechanical boundary or extra Newton/constitutive consequence; that limitation, not the narrow planar scope itself, drives this verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
