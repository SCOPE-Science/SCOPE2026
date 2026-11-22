---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Reviewed the exact frozen RESULT.md field, torus H=(x²+y²−a²)²+z²−1, and both signed parallels z=s. Symbolic reconstruction independently checks H-dot=2zBH and U-dot=zBU for U=x²+y²−a², B=px+qy. On z=s the angular coefficient is −ω−aA_s·(cosθ,sinθ); for |ω|>a||A_s|| the standard tangent-half-angle integral gives physical period 2π/Δ_s, and integrating B over that angular clock gives the sole nontrivial within-surface Floquet multiplier. Expansion yields Δ_+²−Δ_-²=−2a²(uq−vp) while the B numerator depends on pu+qv. Both s signs, ω sign, unit-multiplier and zero-angular-speed boundaries were distinguished. Exact SymPy identities and numerical quadrature are checks, not substitutes for the angular integral proof.

## originality

PASS

Best-of-knowledge new quantitative Floquet/period control for the Jana cubic torus field. Jana gives precisely the model and a zero-free periodicity criterion, while older tori studies classify invariant curves qualitatively. Their conclusions do not imply closed physical periods and two independent controls without the submitted angular integral and first-order variational calculation; exact predecessor is credited.

## value

PASS

The two simultaneously invariant torus cycles provide a natural testbed for distinguishing phase speed from transverse stability: independent determinant and dot-product controls permit equal-time opposite-stability and unequal-time neutral examples, which cannot be recovered from a bare invariant-circle existence theorem. This is a motivated quantitative structural refinement with explicit original-time normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
