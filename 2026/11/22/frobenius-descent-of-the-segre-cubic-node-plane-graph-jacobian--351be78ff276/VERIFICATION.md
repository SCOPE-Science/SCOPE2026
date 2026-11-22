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

# Exact verification and scope

The complete source is `verify_segre_graph.py` and the sole declared dependency is `sympy>=1.12`. Running `python verify_segre_graph.py` produces eleven printed Smith tables followed by `SEGRE_GRAPH_FROBENIUS_INTEGRAL_VERIFIED_OK` on successful execution.

The program constructs all ten complementary-triple node labels and fifteen perfect matching plane labels, checks six plane incidences per node and four nodes per plane, and independently verifies \(II^{\mathsf T}=4I+2J\). It constructs the whole \(25\times25\) integer Laplacian, factors the characteristic polynomial, verifies all \(720\) six-label relabellings preserve adjacency, and recomputes the Smith presentation of the Frobenius coinvariants for all eleven cycle partitions using three different root choices. It independently confirms that the reduced Laplacian determinant equals both the product of the full Smith factors and \(2^{29}5^8\), as required by the spectral matrix-tree formula.

All operations on the critical-group presentations use exact integer arithmetic. These are finite exhaustive computations for every conjugacy class, not sampling across curve or field coefficients. The remaining mathematical proof steps are the standard integral identification of the degree-zero divisor lattice with the chosen root basis and the perfect Galois-equivariant graph monodromy pairing, both described in `RESULT.md`.

These checks certify the explicitly constructed integer matrices and their mathematical consequences as presented. They do not establish comprehensive historical priority, and they do not identify this graph Jacobian with algebraic cycles or arithmetic class groups on the threefold. Independent mathematical audit has not been performed.
