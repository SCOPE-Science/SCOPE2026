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

In rank two choose independent unit-modulus rows u,v and write z_j=v_j/u_j. At most two ratio values imply at most two projective column classes, since each column is scaled from the evaluation of every row's two coefficients at that ratio. If at least three distinct values occur, every linear combination αu+βv that is an actual row must satisfy a constant real affine functional on at least three points of the unit circle; a nonconstant one has at most two. Hence αβ=0, giving at most two row classes. Rank one, including one-row or one-column shapes, has one class. Conversely at most two proportional classes in either direction bound the rank by two. For Fourier rows, proportionality means χ(r−s) is independent of χ∈C, exactly the H_C relation; the column condition is its K_R dual. This establishes the capped rank identity, not an exact rank above two. For 3p and four distinct indices no four-set lies in one mod-p fiber (capacity 3). Its differences generate the p-coordinate, and also the 3-coordinate unless the set is pure mod 3. Therefore H_C is trivial or the order-three subgroup, and likewise dually. Rank two means exactly one mod-3-pure side, opposite a set on two mod-p fibers; rank one is impossible. The two roles are disjoint because a mod-3-pure four-set has four distinct mod-p residues. The counts 3 binom(p,4) and (3+9+3) binom(p,2), multiplied by two, give the exact incidence law. The independent replay used exact cyclotomic determinants, not finite-field ranks, for all 3,969 nonempty rectangles at order six and affine-orbit weighted four-set pairs at orders 15 and 21, obtaining 4,500 and 66,150 rank-two pairs and no rank-one pairs at the latter two orders.

## originality

PASS

Credit the earlier exact order-15 census and earlier 3×3 incidence theorems. The supported contribution is the explicit finite-abelian all-rectangle coset criterion together with the exact occurrence classification and all-p 4×4 incidence formula. Do not credit the three-point unit-modulus obstruction as independently new. The known-three-point-lemma attribution is a material overlap risk, since the precise general 3×3 proportional-pair formulation would already imply the rectangular structural step. The available earlier statements establish size-three Fourier results and the single-modulus size-four census; they do not verify that decisive earlier formulation or the full all-p size-four implication.

## value

PASS

The rank-two cutoff is a natural identifiability threshold for restrictions of a character table. The coset criterion replaces determinant searches by a direct structural test, and the 3p result gives the complete rank-two occurrence set and precise four-channel incidence over an infinite family, not merely a known small-modulus table or a singularity total that conflates defects. Value is assigned to this exact criterion and incidence, not to the elementary unit-circle observation by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
