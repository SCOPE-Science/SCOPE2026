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

The antipodal pairs are graph edges, so every independent simplex is disjoint from its antipodal translate and embeds with its boundary in the quotient. The independent audit replay rebuilt the 197 faces including the empty face and checked the 98 nonempty orbit cells (6,24,38,24,6). It treated the frozen CERTIFICATE.json rows as data: the eleven tree edges span the 1-skeleton, and the 37 valid triangles add one new edge at a time until all 48 are covered, killing every non-tree generator. The action is free on this simply connected complex, giving π1(Y)=C2. All 32 collapse pairs were replayed as unique cofaces in the remaining quotient and verified upstairs in disjoint antipodal pairs; the residual vector (6,16,12) gives Euler characteristic 2 and a 2-dimensional model. H2 is a subgroup of a free top chain group and has rank one. The nonzero degree-one mod-two class has integral Bockstein the order-two summand of H²(Y;Z)=Z⊕Z/2. That summand is not in the image of multiplication by two, so its mod-two reduction, Sq¹(x)=x², is nonzero. UCT gives two degree-two classes and there are no higher degrees, proving the ring. The replay inputs are the frozen graph definition and CERTIFICATE.json (tree, triangle and collapse rows); the supplied verify.py was inspected, not executed, and no separate replay program was retained. The given prior cover statement is correct, but its citation should point to Agarwal–Basak arXiv:2608.30601v1, Theorem 11, not Theorem 12. This reference-number error does not affect the independent geometric argument or correctness of the theorem.

## originality

FAIL

The exact quotient homology and ring in the Finding are mechanically determined by the prior M12 cover homotopy type and the ordinary rank-one Gysin sequence, not by any new graph-specific obstruction. The elementary quotient collapse is a valid alternate proof, but a new certificate does not make these invariants new. No reliance on an unavailable source or presumed priority of a same-day record is needed for this decision.

## value

FAIL

The example illustrates the difference between homology of a cover and its quotient, and the elementary-collapse certificate is sound. But the claimed quotient invariants are a standard consequence of the known homotopy type and freeness; neither the torsion nor the nonzero square is new geometric information here. The Finding does not claim a finer homotopy invariant for which the explicit collapse would be indispensable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
