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

Both binary cubics are squarefree in characteristic 5, so Euler's identity shows their two partials cannot vanish together away from zero. The common F₂₅ model follows by matching root triples in both pairs with the same projectivity and hence the same scalar. An independent geometric replay of the arithmetic lattices is as follows. Write each form as a nonzero constant times a product of three linear forms summing to zero: (x,−y,y−x) in the split case and (x,(−x+√2 y)/2,(−x−√2 y)/2) in the nonsplit case. The nine root-pair lines R_ij and the eighteen graphs Γ(ζ^k g) from permutation g of the three forms and cube root ζ are distinct; the smooth cubic theorem exhausts the lines. Frobenius inverts ζ and conjugates g by the root permutation (identity or s=(12), numbering roots 0,1,2). It fixes 9+6 and 1+2 lines respectively, so the surfaces cannot be F₅-isomorphic. For a Frobenius-stable marking by six disjoint lines, take R_00,R_11,R_22 and all three Γ(ζ^k g) with g=(012) in the split case. In the nonsplit case take R_11,R_22, the two Γ(ζ^k s) for k=1,2, and Γ(g),Γ(g⁻¹). To check disjointness use that a graph meets R_ij exactly when g sends i to j, and two graphs meet exactly when their relative matrix has eigenvalue 1 in the two-dimensional permutation representation. The six classes are exceptional divisors in a geometric plane blowup. Frobenius fixes the pullback H of a plane line, since 3H=−K+sum of the six exceptional classes. It permutes the six as four singletons and one pair, or as three pairs. The full fixed lattice therefore has saturated diagonal bases, with Gram diagonals (1,−1,−1,−1,−1,−2) and (1,−2,−2,−2). This verifies the ranks, determinants and Smith invariants independently of the frozen marking; the displayed Gram matrices have the same determinants and Smith invariants by pivoting on the −1 entries. The cycle and point-count arithmetic was additionally checked by enumerating the 806 F₅ two-planes and normalized projective points (15/3 lines, 51/31 points). With all lines defined over F₂₅, Picard Frobenius is an involution and the divisor-generated H² trace gives the asserted formulas at every extension degree. Geometric invariants descend to Pic over a finite field because Br(F₅)=0. Replay via the root and graph description or the supplied verify_exceptional_cubics.py, which was inspected but not executed. No conclusion is needed about a second exceptional component or about which twist descends from the resolution.

## originality

PASS

Credit the model-specific comparison of the two characteristic-five forms, especially the identification and integral lattice of the explicit split tangent twist. Do not credit new Weyl types, the common quadratic-extension counts, or the Fermat model's point-count law. The nonsplit equation is the Fermat cubic in alternate coordinates, and its counts and permutation-lattice structure have strong prior coverage. The general class tables give the abstract Frobenius orbit and eigenvalue types, but the inspected sources do not attach the split type or a fixed Picard lattice to this explicit tangent equation or compare the two exact descents. The individual abstract class invariants are not claimed as new here.

## value

PASS

The tangent equation and the exceptional equation arise before computation in one concrete resolution. Distinguishing them as F₅ forms avoids misreading extension-field point counts as evidence for a unique descent. The value is the exact arithmetic identification of the tangent form and its integral lattice in that comparison, not recomputing the Fermat point counts or rediscovering a possible Weyl type. The proved fixed lattices detect arithmetic data that equality over F₂₅ and the cited extension counts lose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
