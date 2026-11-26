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

The continuous unordered two-point space is modeled by disjoint-closure cubical cells: the Prue–Scrimshaw bounds for two points are one edge between essential vertices and three edges around an essential loop, valid for the simple wheel. Its inclusion is equivariant, so the homology isomorphism is equivariant regardless of the retraction used. For the quotient conclusion one can make a two-particle equivariant strong retraction explicitly: in a common edge order the coordinates x<y and interpolate to (0,1); in two adjacent edges with coordinates x,y measured from the common vertex interpolate to (x,y)/max(x,y); on disjoint closed edges keep configurations fixed. These formulas respect edge reversals, particle exchange and overlaps (when one particle is on the common vertex, push the other to its far endpoint; when max=1 the relevant configurations are fixed). They therefore glue and pass to both quotients. The cubical 1-skeleton is the connected two-token graph; the cell counts give Euler characteristic −n. For the top boundary, normalize every square in the e-fiber using e as its first oriented factor (with coefficient negated when this requires switching). The coefficient sum at the one-cells (e,v) is then the boundary on the vertex-deleted graph up to a single overall sign. The spoke fibers live on paths, killing their square coefficients, and the remaining rim-only fibers also live on paths. This resolves the proof's implicit orientation normalization and forces injectivity. Orient fixed edge factors and multiply by minus one when they are exchanged. Nontrivial rotations have no fixed cells unless a half-turn, for which the n/2 paired vertices and n/2 negative swaps cancel. For reflections, fixed spoke and rim factors or disjoint swapped rim pairs give the stated signed table; in the even vertex-axis case two swaps at fixed vertices are not disjoint, while in the even edge-axis case the two fixed reversed rim edges form one positive square. H_0 is trivial as a representation, so Hopf trace gives 1−T_0+T_1−T_2 and exactly the reflection-sign twist of the rim-edge module plus a line. The constant rim-edge vector and extra line survive rotations and both change sign under reflections. Subdivide the finite cubical complex equivariantly and average rational chains for the orbit homology. Independent replay python3 /workspace/review-evidence/reproduce.py 1, log /workspace/review-evidence/1.txt, verifies all 260 signed characters and mod-two rank/connectedness checks for 4≤n≤16, including both even axes at n=4. The computations are finite checks only; the supplied nested verification/check_wheel.py was inspected, not run.

## originality

FAIL

Distinct indexed record 84359f9fd52d gives the exact same all-n character, rational module and ordinary cyclic/full-dihedral quotient conclusions. Its wheel subscript counts total vertices rather than just rim vertices. This establishes equivalent coverage, not a historical priority or derivation claim; its catalogue path date is later. The original graph configuration homology ranks and stable discretization are independently established in the literature and are not claimed as new here.

## value

FAIL

The exact signed action and the cyclic/full-dihedral quotient contrast are meaningful invariants. But the submitted scope is an exact restatement of the indexed all-length result via the natural hub-triangle basis. Ranks, signs on both reflection classes, and both quotient conclusions are already covered, so there is no distinct invariant or scope left to credit as a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
