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

The diagonal expectation satisfies the Reynolds identity of weight −1 and fixes the unit. The cited graded theorem applies to all n>=1. Its product in the coordinate tensor basis has coefficient delta_jk/2; the factor 2^(n−1) in degree n matches the matrix-unit product, with the degree-zero left and right actions matching rows and columns. Localizing the central polynomial subring gives the stated order. The ideal tM₂(O) is its radical: for x in this ideal the diagonal of 1−x reduces to 1 modulo t and the off-diagonals to 0, so the inverse given by the adjugate lies in the order. The quotient is k×k. Identify P1=O⊕tO and P2=tO⊕O as columns. Then Je1=tO², J²e1=t²O², and the proposed map is (x,y)↦t(x+y). It is onto and is an isomorphism on the tops, hence is a projective cover (the order is semiperfect with the two coordinate idempotents lifting the quotient). Its kernel is anti-diagonally isomorphic to P1∩P2=tO². Since this nonzero kernel is the kernel of a projective cover, the target Je1 is not projective. Starting with the cover P1→S1 gives the repeating syzygy in the minimal resolution and infinite projective dimension. Central localization preserves projective resolutions and bounds global dimension of the localization by that of the original ring, proving the asserted infinite global dimension.

## originality

FAIL

The construction is correct, but its claimed content is covered by direct specialization of inspected prior constructions. On the Reynolds side Theorem 4.7 explicitly includes finite-group averaging; taking the two-coordinate swap makes its structure constants scalar matrix-unit constants in every positive degree. On the order side the published projective-lattice construction already computes the kernel from intersections of projective lattices. Here the simple's radical is the two-coordinate lattice tO². The two shifted projective lattice summands for this lattice are (tO,t²O) and (t²O,tO); their sum and their only pairwise intersection are (tO,tO) and (t²O,t²O), respectively. The latter is homothetic to the former, so the repeated kernel is the direct two-summand case of the established construction. This comparison does not assert that an earlier paper printed this Reynolds example verbatim. The failure is mechanical prior implication, not the inability to access the older papers.

## value

FAIL

A proper unital average is a natural test case, and an explicit minimal resolution can be useful in an exposition. Here, however, the graded description for group averages, followed by the smallest two-summand case of the standard lattice-intersection calculation, yields the whole exact invariant by degree rescaling and two coordinatewise minima/maxima. The example adds neither a new obstruction nor a nonroutine boundary/classification, and the precise repeating kernel requires no genuinely additional invariant calculation beyond that specialization. This is not a rejection based on the small size or on lack of downstream applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
