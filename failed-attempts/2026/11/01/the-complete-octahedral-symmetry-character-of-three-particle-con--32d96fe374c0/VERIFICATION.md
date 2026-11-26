---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The object is the unordered collision-free topological configuration space, not a finite vertex configuration complex. The orientation-preserving signed coordinate permutations act faithfully on four body-diagonal lines and give S_4; central inversion splits off C_2. The natural comparison theorem for the Świątkowski complex and the equivariant reduced inclusion justify computing the action on reduced weight-three chains. An independent reconstruction (independent_check.py; ranks.out and characters.out) checked the chain dimensions (364,1404,1620,540), square-zero differentials and mod-32003 ranks (363,1033,540). Over Q the first and last ranks have upper bounds 363 and 540 by augmentation and domain dimension; Ko–Park gives b_1=7+1=8 for this planar 3-connected graph, forcing the middle rational rank 1033. The rational Betti vector is (1,8,47,0). Equal rational and mod-p homology dimensions in all degrees exclude p-torsion by universal coefficients, so the rational trace reduces to the calculated quotient trace; an integral finite-order trace of magnitude <=8 is uniquely determined by that residue for H_1. The independent signed chain supertraces, with no H_3 and trivial H_0, give all H_2 traces by Euler–Poincaré. Exact character inner products agree with the displayed multiplicities. The central trace -1 gives eigenspace dimensions 23 and 24. For the orbit statement, triangulate the finite ordered product equivariantly with the collision diagonals a subcomplex; after subdivision their complement retracts equivariantly onto a simplicial model, by renormalizing barycentric coordinates off the diagonal subcomplex. After subdividing to eliminate inversions, quotient homology over Q is computed by coinvariants for the finite action, equivalently invariants by averaging. This applies to the unordered configuration space and then its W-quotient, proving rational acyclicity without a freeness assumption on W. The frozen scripts were not executed and integral torsion is outside scope.

## originality

FAIL

The distinct November 8 catalogue record 4a7f5ab15bea gives the same three-particle space and ten-row full rational character for the same graph group, and states stronger integral homology. Its representative permutations give precisely the frozen signed-cycle classes with the same traces. The choice of wreath-product bipartitions versus S_4 x C_2 Specht labels is just a change of character basis. Both the eigenspace dimensions and absence of fixed vectors are stated there, and quotient rational acyclicity follows from finite-group rational coinvariants. This establishes equivalent mathematical coverage, not historical precedence or dependence from the November 1 and 8 path dates.

## value

FAIL

The character of a canonical graph configuration space is meaningful, but the frozen result does not add a distinct exact invariant to the checked catalogue. It recasts the same complete rational character in different labels and draws immediate representation-theoretic and rational quotient consequences. It supplies neither new integral information nor an independent structural theorem for configurations or their quotients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
