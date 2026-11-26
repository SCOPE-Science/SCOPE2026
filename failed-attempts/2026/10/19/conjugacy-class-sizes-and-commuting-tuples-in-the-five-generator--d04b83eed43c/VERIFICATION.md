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

Saliola's path algebra theorem applies over every field. Each arrow lowers subset size by at least two. The only internal vertices have size 2 or 3, ten of each; they have incoming/outgoing multiplicities (5,1) or (1,5), and cannot be joined to each other. Each of the 100 length-two paths belongs to one internal vertex, the arrow sets of these blocks are disjoint, and the other 74 of the 194 arrows annihilate the radical. The 20 direct summands consist of B and its opposite, and polynomial group inversion sends the opposite factor to the same group functor over every test ring. The commutator ab′−a′b has common kernel zero on the noncentral coordinates (take b′=1 and arbitrary a′), giving center dimension 174 and class two. In one factor the commutator rank is 0, 1 or 5, and dividing the corresponding element counts by q to that rank gives the three class coefficients. For commuting tuples either the b-vector is zero or aᵢ=v bᵢ for a unique v; multiplying by freely chosen central coordinates and taking the product gives the displayed all-s formula. The exponent support is the union of integer intervals [5b,20+4b], b=0,…,20, leaving precisely the stated six holes; evaluation at T=1 gives the stated total. Independent replay, python3 /workspace/frozen_math_replay.py 5, reconstructs composable pairs literally and verifies the disjoint blocks and exponent set; the all-field and all-arity assertions follow from the argument, not the finite replay.

## originality

FAIL

The main size polynomial is an exact prior specialization beyond the frozen record's pair-count comparison. The local rectangular group H₅ is Rossmann's graphical group of the star K₅,₁ as a group functor; Example 5.4 explicitly evaluates its entire ordinary class-size polynomial over every finite field. Saliola's subset quiver and the radical-preserving source/sink decomposition mechanically give 20 such factors and 74 additive factors by subset-size bookkeeping. The six missing exponents are the support of the resulting product. Higher arities are also mechanically determined in this case, not by the pair total alone: all noncentral centralizers of a star factor are abelian, so the standard all-arity centralizer recurrence applied to the known star size polynomial yields the displayed formula. No claim is made that the prior papers print the five-generator formula verbatim.

## value

FAIL

The five-letter algebra is natural, and its block description is convenient, but the narrow invariant as presented is a product recomputation of the known star invariant, with the all-arity count a direct centralizer specialization. The exponent holes encode only the support of that product, and no independently useful unknown exact fact remains once those implications are credited. No substantive narrower repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
