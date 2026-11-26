---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Squares generate the odd abelian kernel A, so the commutator subgroup is A and the quotient C₂ gives two linear codegrees 1 and 2. For a nontrivial linear character λ of A the inversion orbit has length two. On A the induced representation is diagonal with entries λ(a), λ(a)⁻¹, and outside A it is antidiagonal and not the identity. Its kernel is exactly ker λ. These representations are irreducible (the distinct diagonal characters' lines are exchanged by the involution), distinct by inversion pair, and exhaust by the degree-square sum. Each contributes codegree |A:ker λ|=ord(λ). The dual group has A's order distribution, so nontrivial multiplicities are halved, with no collision at 1 or 2. Counting p-power codegrees with missing multiplicities zero yields |Aₚ[pᵏ]|; differences of successive base-p logs count cyclic factors of exponent at least pᵏ. This reconstructs the kernel internally, including A trivial, and its isomorphism extends to the inversion semidirect product. A bounded exact check counted kernels directly using root-of-unity exponents in the displayed two-dimensional representations (enumerating A×{0,1}); for example the order-nine kernels C₉ and C₃² gave nonlinear multiplicities {3:1,9:3} and {3:4}, respectively.

## originality

FAIL

The character and codegree formula is mechanically covered by the full-orbit and induced-kernel formula for abelian-kernel cyclic Frobenius groups in a distinct indexed record, from the same date (relative priority unresolved). For inversion the intersection collapses to one kernel, the orbits have length two, and reconstruction is the known finite-abelian order-spectrum argument applied to the recovered multiplicities. An earlier indexed scalar-affine result also states the exact formula on the elementary-abelian subfamily. The failure is established implication, not a claim that the complete frozen theorem appeared verbatim or that the same-day record came first.

## value

FAIL

Internal rigidity is a natural question for this invariant, but here the general induced-codegree calculation and known abelian determination mechanism already supply it without a new kernel obstruction. Packaging the inversion-orbit factor of two and the standard torsion-log differences is a routine specialization, not a distinct structural result beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
