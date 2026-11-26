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

The nonempty support of a fixed point would contain a whole 5-cycle of adjacent row vertices, so the action is free and simplex interiors have no stabilizers. Orbit CW boundaries use alternating deletion and the sign of the unique translate to the representative. An independent program, replayable as python3 /workspace/branches/reproduce_1_2.py 1, enumerated all nonempty vertex masks using a column-major indexing, chose minimum-mask orbit representatives, checked all signed boundary compositions, and reduced each boundary separately by integer unit pivots. The face counts were (20,150,540,1010,1020,590,200,30) upstairs and (4,30,108,202,204,118,40,6) downstairs. Both free-rank vectors were (1,0,0,2,1,0,0,0); the sole nonunit boundary invariant was 5 in degree 2 of the quotient, giving exactly Z/5 in H1. Cokernel torsion of d_(k+1) is the torsion of H_k because their quotient is the free image of d_k. The independent tree-and-triangle presentation eliminated all 131 upstairs generators, so this is the universal cover with deck group C5. Hurewicz and H2=0 give pi2=0 and pi3=Z^2; transfer and the equal third Betti numbers give the identity action rationally and hence integrally on the lattice. In the covering-classifier Serre sequence the only possible incoming differentials to (3,0) would use fiber H^1 or H^2, both zero; a beta(a) is nonzero on BC5, so its pullback is nonzero. On the matching Moore wedge both factors come from the two-dimensional Moore summand, making their product zero. The corrected consequence is non-equivalence to that wedge, not nonexistence of a wedge with the same homology. The source checker was inspected, not executed; the independent program does not compute a cochain-level cup product or repeat the optional direct quotient Tietze route.

## originality

PASS

Prior work has the underlying periodic graph and its Euler statistic, and there is a closely parallel fivefold chessboard quotient with a Bockstein product. None of the distinct inspected sources gives the signed orbit-chain answer for the 4-by-5 toroidal graph or the two-connectedness of its covering complex needed for this product argument. This judgment is for the corrected exact space-and-invariant claim, not for a new general group-cohomology mechanism.

## value

PASS

This small coprime torus has a natural free prime-order action and a known Euler statistic that cannot see either the torsion or the product. The complete integral groups and a specific nonzero cup product distinguish the quotient from a matching Moore wedge and give a useful hard-square comparison at an exact, reproducible parameter, without suggesting a general classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
