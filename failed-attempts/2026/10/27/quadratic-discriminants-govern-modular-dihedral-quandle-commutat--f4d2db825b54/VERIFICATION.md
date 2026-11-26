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

The multiplication eᵢeⱼ=e₂ⱼ₋ᵢ becomes f(X⁻¹)g(X²) using ordinary group-algebra products only on the right. Truncation below degree five permits the logarithm and exponential identities with invertible denominators, giving the arguments −w and 2w. Expanding the alternating product leaves coefficients 3p₀₁, 3p₀₂, 4(p₀₃+p₁₂), and 4p₁₃; the degree-four pair (0,4) cancels since 2⁴−1=0 in characteristic five. The single Plücker equation is sufficient: pivot on any nonzero minor and reconstruct two rows, with the equation ensuring the remaining minor. When a=z₁/3 is nonzero one can solve for p₂₃; otherwise the equation is u²−su+bd=0 for b=z₂/3, s=z₃/4, d=z₄/4. Its discriminant is the stated z₃²−2z₂z₄, with zero permitted. The four monomial basis vectors of the augmentation ideal are scalar multiples of commutators and the ideal is closed under the native multiplication. Every zero-leading vector is w+(z−w), while a nonsquare δ obstructs z₂=1, z₄=−δ/2, z₁=z₃=0. For q=5^m the obstruction has z₁=0 and z₂≠0; independently choose z₂, z₃ and one of (q−1)/2 nonsquares to determine z₄ uniquely, giving the count and the length partition.

## originality

FAIL

Resultary 2dece93fb098 is a distinct indexed record whose Finding and proof already give the same arbitrary-field discriminant criterion in the same coordinates, the same width dichotomy, and the identical all-extension-field census. The frozen proof is correct but its principal claimed extensions are demonstrably covered; the determination does not rely on catalogue dating or an inaccessible paper.

## value

FAIL

A pointwise criterion for an entire natural field class would be useful if not already available. This package offers the same criterion, the same Plücker derivation, and the same counts as the matching indexed result. Its finite corroboration and complementary counts do not provide an additional structural fact, different proof, or useful new family to justify it as a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
