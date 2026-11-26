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

Over the algebraic closure let H be the hyperelliptic degree-two class. Then 2W_i~H for each branch point and sum_i W_i~3H, by the divisor of y. The two-torsion nodes are 0 and W_i+W_j-H. The theta characteristics indexing translates of the theta divisor are W_i and sum_{i in A} W_i-H for triples A modulo complement. They are distinct, using uniqueness of the hyperelliptic pencil among degree-two pencils; the triple classes are ineffective, since equivalence to any W_i can be reduced by taking the complement to an impossible equivalence of two distinct Weierstrass points with H. Incidence means the node class added to the theta characteristic is effective. Adding a pair to a singleton gives an effective singleton precisely when the pair contains its index, and 0 is incident to all singleton tropes. For a triple, adding a pair wholly on either side gives an effective singleton; a mixed pair gives another triple by replacing the index on one side with the other. This establishes the stated graph and the equivariant root-permutation action for odd characteristic, with no surface-automorphism extension assumption. The reduced Laplacian presents Div^0/LZ^32; the deleted column is minus the sum of the others. In basis e_j-e_v, the action subtracts the image of the sink as stated, so adjoining U-I presents coinvariants. The pairing can be written x^T D' modulo Z for Lx=D; it is independent of additive constants in x and is invariant under simultaneous permutation of vertices. In a sink basis it is the inverse reduced Laplacian pairing, hence perfect. Its fixed part is the dual of the coinvariant quotient, giving the same invariant factors. Independently of the supplied JSON operations, /workspace/branches/kummer_orbit_smith.py constructs the folded six-cube on subsets modulo complement with edges flipping one index, takes the fixed origin as sink, and identifies the degree-zero generators in each coordinate-permutation orbit. Columns for Laplacian relations within each orbit become identical after projection. The resulting smaller square integral presentations were Smith-reduced in SymPy over ZZ for all eleven partitions. They reproduced every invariant factor and order, including ranks 11 vs 13 in the two order-3*2^42 cases. Exactly the two listed four-cycle types share their factors. The source's certificate structure was inspected but its script was not executed. This finite computation is exhaustive on conjugacy types, not an inference from curves sampled over finite fields.

## originality

PASS

The graph and root labeling are classical and the identity row is already available. A particularly close same-day result gives eleven arithmetic coinvariant groups on the same configuration but uses the unsigned incidence cokernel, not the graph critical group. No actual statement furnishing the nonidentity graph-critical fixed-group table was found in the inspected matches. Credit the nonidentity integral classification and separation of equal-order types, not the known identity group, configuration, or duality principle.

## value

PASS

The finite list is dictated by all possible Frobenius cycle types for this canonical configuration, not a chosen test range. The full invariant factors distinguish arithmetic actions that identical fixed-group orders cannot, so a researcher with the branch-factorization type can recover a genuinely finer graph invariant without repeating integral computations. The same computation also explains exactly when two cycle types are indistinguishable by this invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
