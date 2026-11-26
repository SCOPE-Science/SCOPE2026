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

D consists exactly of subsets containing no complete closed cross, hence is the fixed-ground-set Alexander dual of the open-neighborhood complex of the complement. In fact that open-neighborhood complex consists directly of subsets with both coordinate supports proper. On its nonempty face poset the support map has an equivariant section (A,B)↦A×B with T⊆r(T)×c(T). These maps give a homotopy equivalence by poset order homotopy, natural also under transpose. The product of simplex-boundary face posets realizes the corresponding sphere product; Künneth gives two sign lines and their product. For duality, the boundary connecting map identifies reduced homology of D with relative homology of the ground simplex modulo D shifted by one. In that relative complex a basis face has complementary face in the open-neighborhood complex. Pairing their orientations by exterior product into the determinant line on all cells gives the complementary cochain differential, up to a degree sign, and the determinant twist under every cell permutation. This yields N−i−3, the row exponent q, the column exponent p, and transpose determinant (−1)^binom(n,2). On the top product line the flip adds (−1)^((n−2)^2); the two other lines are exchanged. The maximal cliques of the rook graph are its rows and columns; the two size/parallel classes yield the stated full group and the only extra square symmetry. After barycentric subdivision there are no simplex inversions, quotient rational chains are coinvariants, and averaging gives the graded invariants. The only square invariant candidate under the coordinate subgroup is the lower line for odd n, and its transpose is +1 precisely at n≡3 mod 4. Independent closed-cross-mask enumeration gave the specified face counts and all 72, 144, and 1152 elementwise reduced Lefschetz traces on the three test boards, with means 1, −1, 0 (python3 -B /workspace/repro/1.py; /workspace/repro/1.log). This checks alternating traces, not each graded representation on its own.

## originality

PASS

The earlier all-board three-sphere classification covers the ordinary ranks and degrees completely. The supported distinct results are the integral graded action, in particular the determinant-twisted flip, and the quotient law. Neither the prior ordinary equivalence nor the adjacent equivariant rook-complex results give these as stated or by ordinary homotopy invariance.

## value

PASS

This is a complete symmetry invariant for a natural family. The transpose sign produces a genuine rational orbit-space distinction even though the ordinary Betti pattern has the same three-line form; the formula also resolves all subgroup quotient rational Betti numbers without computing their separate chain complexes. It does not classify integral quotients or equivariant homotopy types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
