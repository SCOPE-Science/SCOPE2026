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

The cited Apéry formula applies with d=1, k=n−1 and a=R_n because R_(n+j)=b^j a+R_j and a≥n−2. The key minimization can also be seen directly: b^j=(b−1)R_j+1, so a combination with coin face value r' and coin count c contributes b^n r'+ac. In a fixed residue r, r'>r cannot beat a representation of r with at most r<a≤b^n coins. For fixed face value choose a minimum-coin representation lexicographically maximal from the largest coin down. For any nontop index j, (b+1)R_j=R_(j+1)+bR_(j−1) for j≥2, while (b+1)R_1=R_2. Also bR_j+R_i=R_(j+1)+(R_i−1) for i<j, with R_i−1=bR_(i−1) for i≥2 and zero for i=1. Exchanging never increases the count and improves the lexicographic choice. Thus nontop digits are ≤b, and a digit b has no positive lower digit. Each lower tail then has value at most R_(j+1)−1 through level j, so this representation is greedy. In the residue array 0≤r<R_n, the b regular copies of the smaller staircase have vertically shifted heights tb^(n−1); endpoint differences between copies and at the final residue vanish. All upward jumps are b by induction, starting with q_2(r)=br. A jump at r starts a missing suffix of length R_n−r in precisely b distinct rows, separated by multiples of R_n; monotonicity precludes other maximal blocks. Jump indices have distinct greedy digits with bottom coordinate 1 through b, and complementing digits via (b−1)R_j=R_(j+1)−R_j−1 yields offset n−1, the product, and both extrema. There are exactly b^n blocks; no uniqueness of a longest block is asserted.

## originality

PASS

Prior papers supply the explicit Apéry set and classical numerical-semigroup invariants, not credited as novel. The supported distinct result is the b-fold histogram and factorized maximal-gap length spectrum. No equivalent spectrum or otherwise directly dominating result was established in the inspected statements.

## value

PASS

The gap lengths refine the known Frobenius number and genus for a natural, well-studied family. The exact multiplicity law and digit factorization reveal a uniform regularity not captured by those statistics; the result is more informative than an endpoint or an isolated finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
