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

The derivative is twice the off-diagonal cofactor. At rank n−1 a symmetric adjugate is λuuᵀ, so the off-diagonal derivatives vanish exactly when the kernel is a coordinate line, i.e. there is a zero row. Lower rank kills all cofactors. For r=n−2≥3 all hollow matrices of rank ≤r are images of Q_r^n by WWᵀ after symmetric congruence and zero padding. The rank-r isotropic quadric is integral; an isotropic basis exists (e₁±ie₂ and e₁+ie_j for j≥3). For full rank, equality of images implies equality of column spaces and the bases differ by O(r), giving affine dimension n(r−1)−r(r−1)/2=N−3. The full-rank example with two repeated rows has no zero row in its Gram matrix (an isotropic basis spans the nondegenerate ambient space, so no nonzero row pairs to zero with every row). Each L_i has dimension N−n and contains rank n−1 points with all other rows nonzero, by the all-ones off-diagonal block. Thus the listed irreducible varieties are maximal. The gradient locus of ambient codimension ≥3 rules out repeated factors and intersections of distinct hypersurface factors; S₂ and R₁ give normality. Along L_i the exact Schur form is −det(B)vᵀB⁻¹v; over the completed local base one diagonalizes by unit pivots and square roots. On D_n, the given kernel generators have disjoint supports, and hollow variations at (1,r+1), (3,r+2), (r+1,r+2) restrict to independent coefficients (−2,0,0), (0,0,−2), (0,1,0) in diagonal/off-diagonal/diagonal order. The differential is rank three on a dense open; the projective chart loses no normal direction since the radial direction restricts to zero. Formal coordinates give ac−b² with N−4 smooth parameters. Both quadratic cones have multiplicity two. The finite archived checks are supplementary, not needed for this proof. No global scheme decomposition or special intersection model has been verified.

## originality

FAIL

The distinct indexed record 8072f618df0b demonstrably covers the entire proposed contribution, including the exact components, their dimensions, and both formal transverse models. Its corank-two chart covers every rank-(n−2) point with no zero row, stronger than the generic-open claim, and it works over algebraically closed fields of characteristic not two. Restricting that theorem to C leaves no distinct classification or local-type claim. This is a decision about equivalent coverage in the indexed evidence, not an assertion that the later-dated record had historical priority. The inspected earlier literature establishes important pieces, but does not by itself establish earlier priority for the whole classification.

## value

PASS

Classifying all reduced singular components of this natural discriminant and distinguishing the two geometric sources of ordinary quadratic singularities is substantive. The corank-two and coordinate-kernel mechanisms have quantitatively different normal dimensions, data useful for studying local resolutions and the singular strata. This evaluates the mathematics, not its originality as an additional record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
