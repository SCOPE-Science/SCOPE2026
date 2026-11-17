---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the double D²(A1*...*A6), triangle vertices correspond to three pairwise disjoint color-pair labels; every two-simplex and, critically, every one-simplex has exactly one six-color perfect-matching label (the third color pair is the pair of unused colors). Hence signed ∂2 is an integral direct sum across 15 matching blocks and H2=ker ∂2 since no 3-simplices. Each block is the top boundary of a join of three discrete sets P_ij=A_i×A_j and the integral Künneth chain model identifies its kernel naturally with tensor over Z of three augmentation lattices ker(Z[P_ij]→Z). The eight-term cycles from differences of vertices form an integral basis. Γ=product S(A_i) preserves these blocks and acts naturally, giving the boxed full integral module, rank product(n_i n_j-1), trace product(f_i f_j-1). Fresh independent GF2 top-boundary ranks are 555 of 960 triangles for all n_i=2 and 765 of 1440 triangles for (2,3,2,2,2,2), agreeing b2=405 and 675; the integral statement is proved from block splitting.

## originality

PASS

The published Björner–Wachs–Welker inflation theorem (Theorem 6.2, Corollary 6.3) already determines the ordinary wedge decomposition and integral ranks, while its Corollary 8.5 develops an equivariant decomposition over a characteristic-zero field. Both are explicitly prior: the rational representation/character and numerical Betti data are not newly claimed. The surviving exact integer Γ-lattice decomposition is obtained by a specific 15-block decomposition of the actual top-boundary map and eight-term primitive integral generators, providing integral action beyond rational equivalence. No indexed exact integral six-color decomposition was found; residual risk includes an unindexed integral version of field-level equivariant inflation.

## value

PASS

An integral Γ-lattice is a stricter invariant than a rational character or sphere count and can retain extension/modular information. The unique matching-block incidence partition yields an explicit canonical integral basis of all top cycles with natural within-class permutation action, reusable for integral equivariant homology of six-color join doubles. This is a motivated structural lemma of a natural simplicial double, not merely recomputation of known inflation Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
