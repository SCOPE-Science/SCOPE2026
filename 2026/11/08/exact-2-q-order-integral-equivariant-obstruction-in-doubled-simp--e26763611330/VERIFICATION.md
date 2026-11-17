---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The pair (B_q,X_q) with B_q the join of q two-point sets and X_q its codimension-one skeleton gives 0→H_{q-1}(B_q)→H_{q-1}(B_q,X_q)=E→H~_{q-2}(X_q)→0. Orient facets by coordinate order; the signed fundamental cycle z=Σ_b (-1)^{|b|}e_b is primitive, and W_q acts on its line via det ε. E restricted to T=(C2)^q is a free regular lattice, hence projective, and Hom_T(E,Zε)=Z. The restriction of its generator a(e_b)=(-1)^{|b|} to z has multiplier 2^q; the Hom–Ext connecting long exact sequence therefore identifies Ext^1_T(M,Zε)=Z/2^q, with the actual extension a generator. The same a is equivariant for coordinate permutations with facet orientation sign and all flips, giving 2^q times the extension class zero over W; restriction forces order >=2^q, so its exact W order is 2^q. Dividing a by 2^q splits after inverting two. Independent finite signed-facet checks q=3,4,5 confirm face incidence cancellation and signed augmentation norm, but the all-q Hom–Ext proof supplies the quantifier.

## originality

PASS

Björner–Wachs–Welker gives the ordinary wedge formula (2^q−1 spheres) and an equivariant inflation representation over characteristic-zero fields, not the integral extension class order. Ayzenberg–Khoroshavkina and Ayzenberg–Rukhovich study generalized inflations/homotopy and functoriality; inspected relevant sections do not state this canonical Z[W_q]-module Yoneda class of exact order 2^q. No exact published signed augmentation order found. Best-of-knowledge PASS with group-ring folklore risk.

## value

PASS

The exact exponential order of an integral equivariant extension is an independently meaningful obstruction to lifting rational equivariant splittings; it pinpoints what ordinary wedge homology cannot detect and supplies a reusable signed-norm calculation on a natural hyperoctahedral family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
