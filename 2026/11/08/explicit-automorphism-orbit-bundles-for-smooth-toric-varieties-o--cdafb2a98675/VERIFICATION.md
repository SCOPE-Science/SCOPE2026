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

For s,r>=1 and split E=⊕_{j=0}^t O_{P^s}(b_j)^{m_j}, b_0=0<b_1<...<b_t, lines convention: (i) evaluation at any base point of degree-increasing bundle maps is surjective and diagonal GL(m_j) plus those shears acts transitively on the minimum-nonzero-degree stratum; base PGL transitivity lifts. (ii) For t>0 the nef rays are H and D=xi+b_t H; H contracts P^r fibres whereas |D| is generically injective on the locus with nonzero degree-zero coordinate (Veronese degree b_t recovers base, remaining sections recover fibre). Thus full Aut preserves the unique fibre-type contraction and acts by E≅g*E⊗L; the finite splitting-degree multiset forces L trivial and triangularity forces preservation of all F_j. (iii) A line over a chosen lowest nonzero level is the graph of ℓ→⊕_{h>j}O(b_h)^{m_h}, so U_j=Tot(⊕_{h>j}O(b_h-b_j)⊠O_{P^{m_j-1}}(1)^{m_h}) over P^s×P^{m_j-1}. (iv) Closure P(F_j) has codimension Σ_{h<j}m_h, vector bundle multiplicativity gives the exact motive; the boundary P(F_1) has codimension m0. Product t=0 and Hirzebruch / threefold edge cases agree. Finite census does not prove (i)–(ii).

## originality

PASS

Best-of-knowledge PASS restricted to the explicit integrated all-dimensional orbit-BUNDLE classification, classes and sharp boundary multiplicity law. Bazhov already covers arbitrary complete toric orbit equivalence abstractly; BB theory supplies general affine strata and motivic decompositions; Kleinschmidt supplies the class of objects. They are not claimed as new. A relevant 2026 primary article has only a threefold subcase and explicitly asks for the higher-dimensional smooth classification. This is a natural, nonautomatic closed-form geometric specialization; no inspected earlier source states the entire all-parameter full Aut geometric conclusion. Residual possibility that the combination has already been worked out elsewhere is material.

## value

PASS

The family is the natural exhaustive Picard-two subclass of smooth complete toric varieties, and the 2026 classification question singles out the phenomenon. Full geometric orbit bundle descriptions, their Grothendieck classes and a sharp homogeneous-in-codimension-k criterion for every splitting multiplicity and dimension are meaningful complete geometric invariants. The proof needs full-group invariance, not merely a fibre-point count or a trivial renaming. Value is bounded to this explicit subclass classification; it is not a solution for arbitrary Picard rank and no novelty is claimed for the general toric orbit criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
