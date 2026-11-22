---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS — The Vámos rank-four independence complex is the full 3-skeleton of a 7-simplex with exactly five forbidden 4-faces removed. Each forbidden face meets any other in <=2 vertices; the 4-boundary of F∪{x} maps to ±F in relative chains with no second forbidden face, proving integral surjectivity of ∧⁴A→E, hence reduced H3=Z^{35−5}=Z^30 and no other reduced integral homology. Incidence degrees distinguish {0,1,6,7} (two) and {2,3,4,5} (three), giving intrinsic full G=D4×D4 of order 64. The rational character χ(g)=tr(∧⁴A)(g)−signed trace on five forbidden facets; character orthogonality gives the stated 5×5 multiplicity matrix, with trivial-low row zero, trivial-high column dimension one, and full trivial tensor absent. Rational averaging of barycentrically subdivided ordinary geometric quotient yields homology 0/1/0 in top degree for low/high/full groups, respectively. Independent permutations generated order64, χ(e)=30, and average traces gave low0 high1 full0. No integral quotient torsion classification or equivariant lattice splitting is claimed.

## originality

PASS

PASS best of knowledge — The published matroid Tutte polynomial and shellable wedge rank already give nonequivariant rank30. Karn–Nasr–Proudfoot–Vecchi's primary Vámos Section 5 explicitly establishes the **same automorphism group D4×D4**, but its representation is an equivariant Kazhdan–Lusztig coefficient of dimension 33, not the 30-dimensional simplicial top homology character. Moci–Pezzoli provide a general equivariant matroid-homology representation framework; their inspected applications do not compute the complete 25-term Vámos D4×D4 decomposition or the two intrinsic quotient invariant ranks. The explicit signed five-facet exact sequence and asymmetric quotient results are additional. Unindexed older computations of Vámos equivariant characters remain possible.

## value

PASS

PASS — Vámos is a canonical nonrepresentable sparse-paving matroid; its two intrinsically distinguished D4 actions have **different** rational quotient topology despite equal group order and the same nonequivariant wedge rank. The exact 30-dimensional character and five-facet integral exact sequence make a new, motivated structural invariant available, not just a Tutte polynomial recomputation. Rational quotient results are not assertions of integral contractibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
