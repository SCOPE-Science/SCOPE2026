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

The action is free since every nontrivial row rotation changes the uniquely occupied row in each occupied column. There are two edge types on each column pair and two triangle types on each triple; oriented row differences give the two recorded boundary words. Collapsing the spanning tree makes the two relators on 0,i,j solve for e⁺ij=xj and e⁻ij=xi⁻¹. The remaining words are xj xk xi and xi⁻¹ xj⁻¹ xk⁻¹. Successive positive triangle relators 123, 124, 134 solve for x1=x3⁻¹x2⁻¹, x4=x3, x2=x3, and 12t solves for xt=x3 at every t≥5. Each solved letter occurs once and is absent from the solving word. Such a one/two-cell move preserves the complex up to homotopy: homotope all other attaching loops in the subcomplex containing the solving cell to replace the eliminated letter by its path there, then collapse that cell with its single remaining edge occurrence. Thus x1=x⁻² and all others=x. Words involving 1 then have exponent 0; all others have exponent ±3, with 234 available already at n=5. Attach one degree-three cell; all other loops are now null and attaching along them wedges on 2-spheres. The count 2·binom(n−1,3)−(n−2)−1 is the asserted β. The frozen finite checker was read, not executed; the word argument works for all widths without extrapolation.

## originality

FAIL

The exact homotopy type asserted in the Finding is a direct corollary of the classical Dyer–Sieradski classification of connected finite 2-complexes with finite cyclic fundamental group and the previously published calculation of π1 and H2 for this very quotient. The earlier quotient record not explicitly asserting a wedge does not prevent that implication. The direct word proof is correct, but no further invariant, restriction on the maps, or stronger conclusion is asserted in the Finding.

## value

FAIL

The elementary word reduction is pedagogically useful, but the submitted scientific output is the ordinary wedge type and sphere count, mechanically fixed by an exact known invariant of the same spaces and a classical theorem. It makes no new mathematical claim about equivariance, specified maps or stronger cell structure beyond that covered type. There is no verified distinct valuable remainder to repair as part of this review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
