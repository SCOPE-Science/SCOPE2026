---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python check.py` with standard Python 3 and no external packages. The input objects are permutation tuples, zero-indexed; each tuple encodes one row's one-entry column positions. The script exhaustively generates \(\binom{23}{3}=1771\) anchored vertex quadruples at order four and \(\binom{119}{3}=273819\) at order five, using the fact that left multiplication sends any designated permutation vertex to the identity and preserves Frobenius volumes. For each quadruple it computes the six pairwise coincidence numbers and an exact integer Gram determinant. It also recomputes selected determinants from direct entry-by-entry difference-matrix coordinates and checks the cyclic witness construction in orders 5–44.

Observed output:

```
exact_full_enumeration 4 anchored= 1771 highest_determinants= [256, 184] anchored_counts= (4, 48) unanchored_counts= (24, 288)
exact_full_enumeration 5 anchored= 273819 highest_determinants= [500, 440] anchored_counts= (224, 2400) unanchored_counts= (6720, 72000)
BIRKHOFF_TETRA_GAP_PASS full_orders=4,5 example_orders=5..44 high_levels_n5=500,440 independent_gram=PASS
```

Proof beyond these finite orders: the four-point diameter lemma bounds the squared volume of every tetrahedron by \(a^2L^2(3L^2-a^2)/144\) when one edge has length \(a\) and all edges are at most \(L\). For four distinct permutation matrices in the Birkhoff polytope, \(L^2=2n\) and any failure of pairwise support-disjointness gives \(a^2\le2(n-1)\). Equality forces exactly one overlapping entry. The cyclic witness establishes sharpness in every order at least five. The unrestricted maximum is achieved only by disjoint permutation supports, since maximum Frobenius pair distance forces both endpoints to be permutation matrices.

The script's finite exhaustive loops are not a replacement for the proof for all integers. The finite order-four statement follows by exact exhaustive computation with a transparent finite search space; independent auditing has not been performed. Results about different matrix norms and higher-dimensional simplex volumes are outside scope.
