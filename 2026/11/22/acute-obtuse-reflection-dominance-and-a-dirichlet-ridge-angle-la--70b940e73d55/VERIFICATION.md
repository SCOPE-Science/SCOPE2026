---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The ambient hyperplane has tangent space 1⊥ and affine dimension n−1 (the full coordinate simplex is a summand). The known simplex-sum tubing face theorem makes proper intervals facets and distinct compatible pairs ridges. The minimum coordinate sum on a tube S on each summand is one if the summand's tube is a subset of S and zero otherwise, so its outward intrinsic normal is −(1_S−|S|1/n). Its normalized dot product with another such normal gives the stated signed cosine, positive for nested and negative for disjoint nonadjacent tubes, and strictly between −1 and 1. The interior angle is the supplement of the normal angle. For nested lengths a<b the longer tube has n positions and the shorter one b−a+1 starts. For disjoint lengths, the two positive gaps sum to n−a−b and rooting at a prescribed tube counts once if a<b and twice if a=b. Summing nested counts and counting n times all positive four-part compositions divided by 2 for disjoint pairs yields O_n,A_n,R_n and the acute probability; n=3 gives six obtuse ridges and no acute ones. For an acute pair (a,b), the complementary nested types are (a,n−b) and (b,n−a), coinciding only for a=b. Given a nested type (c,d) in this image, the disjoint unordered lengths {c,n−d} are uniquely recovered, so summing even when angles collide cannot double-count the reflected contribution. For each contributing type the ratio is 2(r+1)/(r−1)>2. The disjoint four-block sample is a uniform composition after rooting uniformly at one tube; nested block sizes are also uniform apart from O(n²) boundary descriptions in Θ(n³) possibilities. The normalized point meshes converge by simplex Riemann sums to Dirichlet(1,1,1,1); the angle maps are continuous almost surely under this law. Exchangeability gives the same conditional cosine magnitude (two designated coordinates) in either class. Combining conditional convergence with the exact acute weight gives the independent-branch limit. The positive-weight extension is within the same intrinsic normal-fan realization only.

## originality

PASS

The tube face structure and projected normal-ray mechanism are prior, and the unrefined total ridge count is combinatorial face data. The strongest same-day analogue for Loday's path associahedron shares the functional cosines and composition-to-Dirichlet method; it does not give the cycle multiplicities, strict reflected factor greater than two, or the four-coordinate 1:2 limit. The pass is on this cycle-specific metric synthesis and refinements, not on the general angle calculation for projected characteristic normals or the Dirichlet method.

## value

PASS

The cycle simplex-sum is a canonical realization, and its Euclidean angles are not determined as numbers by the abstract face lattice. A refined complete ridge multiset gives useful geometric reference data. More decisively, the angle-by-angle reflected multiplicity inequality survives collisions, and both conditional cosine laws have a common Dirichlet limit despite the finite and asymptotic count imbalance. The combination resolves natural questions about angular geometry beyond recovering the type-B f-vector or reusing the generic dot-product formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
