---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The exact path unsigned incidence matrix B has full column rank, G=B^T B has 2 on diagonal and +1 on adjacent off-diagonals. The signed-Dirichlet inverse is A_ij=(-1)^(i+j)min(i,j)(m+1-max(i,j))/(m+1); affine tangent barycentric-gradient Gram is H=A-bb^T/t with b=A1, t=1^TA1. Its positive diagonal and exact equal/opposite parity signs give all m-choose-2 ridge angles including sole endpoint zero for odd m. Scaling m^-1 A to the Green kernel, parity sublattice Riemann sums, and integrating 2∫[0,1] a y/[1-(1-a)y] dy yields the given nonuniform logarithmic cosine CDF. Independent exact affine-difference metric inversion for m=3..12 checked signs and exceptional zero; finite checks only corroborate the all-m proof.

## originality

PASS

The graph edge-simplex incidence realization is classical. The previously published graphical-cycle zonotope result has an identical logarithmic squared-cosine CDF after variable change, but its finite angle multiset, sign support, polytope metric and indexed facet normals are different; no preservation/implication to the unsigned path simplex. No inspected prior establishes the parity-resolved complete path-simplex ridge array and its signed law; best-of-knowledge priority with unindexed risk.

## value

PASS

A full intrinsic-Euclidean dihedral spectrum and exact natural uniform-ridge distribution for a canonical graph edge simplex is structural geometric information, sensitive to the graph and unavailable from its combinatorial simplex type; the unique right-angle parity defect distinguishes path from cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
