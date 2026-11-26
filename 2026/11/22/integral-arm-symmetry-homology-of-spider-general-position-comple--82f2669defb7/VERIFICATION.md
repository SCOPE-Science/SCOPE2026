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

A face of size at least three cannot include the center or two vertices from one arm, since one of that triple lies between the other two. All choices of one vertex per arm or fewer qualify. Thus the join J of the r arm vertex sets acquires only the internal-arm edges and the central star with its new vertex. For r≥3 the join has H₁=0 and is (r−2)-connected; the augmented join complex gives (ℓ−1)^r top generators, and a simply connected CW complex with this sole free reduced homology is the corresponding wedge of spheres, by Hurewicz and homological Whitehead. The singleton case ℓ=1 is a contractible simplex. Adding the star and internal edges contributes r(ℓ+binom(ℓ,2))−1 circles. Integrally, the projection of a 1-cycle to all added edges has exactly the central coefficient-sum constraint; its boundary at the arm vertices can be canceled along paths in J. The kernel of projection on homology is zero because H₁(J)=0. Increasing-depth and outward orientations are preserved, giving the asserted equivariant lattice, not just its rank. In top degree, orient joins by arm order: permuting arms contributes the permutation sign, while the augmentation factors are permuted. Counting equal tensor indices on each permutation cycle yields the character. Rational chains on the actual quotient are coinvariants after barycentric subdivision removes inversions; exact averaging identifies homology with invariants. The degree-one invariant constraints leave binom(ℓ,2)+ℓ−1 degrees of freedom, and the signed tensor invariants are exactly the alternating tensors, of dimension binom(ℓ−1,r), nonzero precisely for ℓ≥r+1.

## originality

PASS

The labelled face description is prior input; the quotient ranks are also covered by a stronger, separately indexed integral quotient theorem. The distinct supported contribution is the canonical integral arm-action classification before quotienting (and hence its characters). The stronger quotient statement explicitly distinguishes that contribution and does not recover it from the quotient.

## value

PASS

For all equal-arm spiders the result separates two different sources of integral symmetry: the central augmentation constraint plus freely permuted depth-pair edges in degree one, and signed permutation of top tensor cycles. The cycle projection determines the lattice even at primes dividing the order of the group, where rational character calculations would not recover it. This is a natural automorphism classification beyond counting faces or reporting the absolute sphere counts; the quotient threshold illustrates the significance of the sign but is not itself the distinctive contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
