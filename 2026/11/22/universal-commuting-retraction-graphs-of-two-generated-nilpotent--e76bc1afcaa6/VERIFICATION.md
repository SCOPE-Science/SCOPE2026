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

For a retract H=e(L), idempotence gives H∩[L,L]=e([L,L])=[H,H]. The image of the quotient projection is therefore the abelianization of H, not just a quotient of it. By induction down the lower central series, a subalgebra surjecting onto the abelianization generates the entire nilpotent algebra. Quotient ranks 0, 1, 2 thus force the zero map, a one-dimensional image (alternation, including in characteristic two), and the identity, respectively. For a fixed rank-one quotient projection P onto U along W, fix a nonzero v in U and its normalized functional λ with kernel W. Every lift is x↦λ(πx)u with πu=v, and all q^(n−2) such maps are Lie homomorphisms and idempotent. A commuting quotient projection preserves both lines U,W and is either P or I−P. With usual composition, distinct same-fiber lifts satisfy ef=e and fe=f; complementary fibers instead give ef=fe=0. Pairing the q(q+1) quotient projections by complement gives the claimed disjoint complete bipartite components. With M=2mb nontrivial vertices, the commuting ordered pairs are M+2 diagonals, 2mb² ordered proper edges, and 4M+2 other ordered pairs involving 0 or 1, hence M(b+5)+4. The rank and clique polynomials, maximal families, limit and graph reconstruction follow. The two five-dimensional examples have lower-central classes 3 and 4 and the same q,n. The generator-image checker was read, not executed; its prime-field examples cannot justify general fields, which the characteristic-independent proof covers.

## originality

PASS

The graph shape and quotient-lifting idea have clear precedents. The supported distinct claim is the entire ordinary Lie graph for arbitrary finite-dimensional two-generated nilpotent Lie algebras, at all prime powers including characteristic two and beyond the class range of the standard Lazard correspondence; no inspected precedent has that scope.

## value

PASS

This classifies a natural incidence invariant for a whole class of algebras, not just a rank list or another example. It identifies exactly which pairs commute, how many lifts follow each abelianized projection, and exactly what the graph can recover (field size and dimension but not class), hence shows independence from arbitrary higher bracket relations. The special-case counts and analogy alone are not credited as value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
