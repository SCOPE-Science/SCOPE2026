---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

All nonempty rook faces have trivial stabilizer under the cyclic 3-row rotation: each occupied column has exactly one selected row. Quotient orbit cells are n vertices, n(n-1) oriented edges, 2*C(n,3) triangles with the displayed integral boundary signs. The spanning-tree cycle basis eliminates triangle variables and leaves H1=<x2,...,xn | xi+xj+xk=0, 2<=i<j<k<=n>. For n=3 no relations gives Z^2, for n=4 one primitive triple relation gives Z^2, and n>=5 has at least four generators so pair-sharing differences force all xi equal and 3x=0 with a map to Z/3 proving exact order. At n=3 free-edge simplicial collapses give wedge S1∨S1; n=4 original chessboard surface is torus and odd-order orientation-preserving covering keeps torus. For n>=5 classic chessboard connectivity gives simply connected cover, hence π1 quotient C3; top H2 is free as kernel of integer ∂2 and its rank is χ-1=n(n-2)(n-4)/3-1. Direct integral presentation is all-width proof; bounded Smith checks n=3..10 independently corroborate.

## originality

PASS

Earlier homology results for ordinary chessboard complexes are about the cover and other Resultary records concern column rotation or different row/column dimensions. The row C3 geometric quotient and all-width H1 torsion transition are a distinct exact integral invariant. Standard covering-space theory supplies π1 given simple connectivity but does not compute the complete signed orbit-cell presentation.

## value

PASS

A natural group action on the basic 3×n chessboard complex acquires order-three torsion exactly at n=5 although the cover has torsion-free homology; the sharp wedge/torus/torsion change and all-width free H2 rank are meaningful classification data and provide test cases for equivariant combinatorial topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
