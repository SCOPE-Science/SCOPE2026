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

Prue–Scrimshaw, Theorem 3.2 and the paragraph following it, explicitly give the sufficient subdivision criterion for unlabeled configurations. After one subdivision every path between distinct essential vertices has length at least two and every homotopically essential closed path has length at least six, satisfying the bounds two and four for three particles. In the resulting unordered cubical complex, three-cells are precisely 3-edge matchings, there are no four-cells, and the boundary has the six signed endpoint replacements. I independently generated the signed row incidence, obtaining (c2,c3)=(1386,432),(3840,1296),(8190,2880),(14976,5400). Sparse elimination over F3 (the frozen verifier uses F2) returned ranks 432,1296,2880,5398, bounding the rational nullities by 0,0,0,2. For the two alternating face triples the factors are vertex-disjoint squares, so their subdivided products embed in the cubical configuration space and represent the proposed geometric tori. The two signed 512-term chains have zero integer boundary, and top-rim coordinate evaluations on the two chains give the identity matrix. The rational upper bound is attained, and these integer-valued evaluations force integer coefficients on every integral cycle in this rational span. Thus the generators are a full integral basis, not only independent modulo a prime. Replay: python3 /workspace/review-evidence/topology.py prism; output prism.log. No lower degrees or larger circumferences audited.

## originality

PASS

The strongest inspected matching topics differ by point configuration versus geodesic general position, by graph, by number of particles, or by fixed-size versus asymptotic range. The exactly matching Resultary hit was this same record. Neither the subdivision theorem nor existing general asymptotic results supply the claimed finite integral ranks and primitive basis.

## value

PASS

The first four prisms are a natural fixed-particle progression in which vanishing precedes a concrete change in the geometry of simultaneous motions. At six, the two alternating square products account for all integral three-dimensional homology. This is more useful than just a Betti number: the primitive basis identifies actual simultaneous motions that could be used in studying actions or homology pairings, and absence of hidden classes in smaller prisms does not follow merely from the lack of these tori.

The dated certificate retains the supplied scientific assessment, sources and limitations.
