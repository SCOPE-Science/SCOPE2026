---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The directed-path criterion forces at most one u_i, one v_j and the common c in a face. Every pair (u_i,v_j) is admissible, whereas the triple (c,u_i,v_j) is admissible precisely for i!=j; i=j forms a directed 3-cycle. These are all possible faces. Each off-diagonal edge has exactly one triangle coface and can be removed with it; the S_m-invariant disjoint pair family leaves edges c-u_i,c-v_i,u_i-v_i. The orbitwise elementary collapses preserve the retained intersection faces, hence give an equivariant strong deformation retraction. Each circle is permuted without reversing orientation: π1=F_m, H1=Z^{m} as permutation lattice, fixed circles equal individually fixed page indices, quotient circles equal page orbits. For m=1 there are no free pairs and already exactly one circle. The all-m argument is combinatorial; independent enumeration verified exact faces/count 2m^2+3m+2 for m=1,2,3,4.

## originality

PASS

The exact directed shared-arrow book family and its S_m-equivariant collapse/fixed-space representation are not covered by the inspected directed-forest general framework or indexed polygon, grid and bidirected computations; the shared-arrow family has a different simplex classification. The general technique of elementary collapse is not claimed novel. Best-of-knowledge PASS subject to unindexed-equivalence risk.

## value

PASS

A uniform all-page answer for directed-cycle multipath complexes, including integral symmetry action and every subgroup fixed space, addresses a motivated family within an explicit prior homotopy-classification problem; it is not a one-off tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
