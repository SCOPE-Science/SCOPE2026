---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In characteristic two the square is a derivation, so checking x,y suffices. Leibniz gives D(xy)=v₁y+v₂x+tr(B)xy and the three displayed coefficient equations. For v≠0, B=uλ_v, c=(λ_v u)u; division by v₁ or v₂ on the corresponding chart gives a regular inverse. For v=0 the equations are B²=0 and Bc=0. For B₀=αwλ_w and c₀=βw, v=tw and u=αw/t+b with λ_w b=β/α yield exactly the polynomial limits stated in the proof. For B₀=0 and c₀≠0 the t² scaling of v and t⁻¹ scaling of u keep c equal to c₀ and specialize B to zero. These curves over an algebraic closure exhaust the boundary of the dense chart. A nonzero v gives two independent images and rank two; at zero v the nonzero block [B|c] has rank one, or all coefficients vanish. A nonzero nilpotent B is specified by its image/kernel line and a nonzero quotient-to-line map, giving q²−1 possibilities and q choices of c; B=0 gives q² choices. The independent direct composition/image-size enumeration gives rank counts (1,9,12) and (1,75,240) over F₂ and F₄.

## originality

FAIL

A distinct indexed record already gives exactly the same square-zero condition on the same derivation algebra, the same rank strata and identical counts. Its explicit square-preserving linear identification with sl₃ also directly yields the entire reduced geometry and the specific open product, so no distinct geometric remainder is established. This is a coverage finding, not a determination of historical priority from repository paths.

## value

FAIL

Rank strata and a rational chart are worthwhile invariants of this restricted algebra, but the frozen package provides no remaining independently useful new invariant after the exact counts and immediate chart from the square-preserving matrix model are credited. Rechecking a known table or presenting different boundary curves for that same chart does not supply a surviving valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
