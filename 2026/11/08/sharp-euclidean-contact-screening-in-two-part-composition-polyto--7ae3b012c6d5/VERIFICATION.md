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

From the two prefix-sum inequalities and nonnegativity one derives all vertices 0, A_i=pe_i, B_j=(p+q)e_(p+j), C_ij=pe_i+qe_(p+j). For a two-block symmetric center, the four exact squared-distance forms and F=(q-2)(p+q)^2-qp^2, K=p²+3pq+q² show B_j always on the proposed sphere; A_i exactly when F<0; mixed vertices never; origin only for p=q=1. The proposed center is a convex combination of its contacting vertices, giving global minimality and uniqueness by weighted variance identity. Since q(q-2)=(q-1)^2-1 is not square when q>=3, no integer F=0 case. Independently verified 576 rational p,q distance/contact comparisons including the boundary. This proof, not the test grid, covers all positive integer p,q.

## originality

PASS

Athanasiadis defines these exact composition polytopes and proves lattice counting/gamma-positivity, while Chapoton and Pitman–Stanley give more general combinatorial constructions. Those results do not compute Euclidean minimal enclosing balls under the canonical coordinate metric. A same-day octopus arbor-polytope circumball classification was read in full, but its inequalities cap individual first-block coordinates, yielding a different Euclidean vertex set; its three-phase result does not imply the present exact F-dependent contact collapse. No stronger same-object metric theorem was found in targeted primary and Resultary comparisons; historical priority remains qualified.

## value

PASS

The canonical Euclidean minimum-ball radius, center and full equality contacts of every two-part composition polytope are natural metric invariants, not determined by its Ehrhart series or combinatorial simplex type. The exact F sign phase screens an entire initial vertex block with no integer tie and yields a structural base case for higher-part compositions; no broad downstream theorem is necessary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
