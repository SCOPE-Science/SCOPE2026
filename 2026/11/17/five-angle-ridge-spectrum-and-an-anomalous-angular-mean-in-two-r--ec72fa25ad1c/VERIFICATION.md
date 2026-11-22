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

Read full RESULT.md proof, underlying Erickson-Kretschmann facets and exact rational source verifier. There are 2q coordinate and q-1 comparison facets, normals in sum-one hyperplane as specified. All FF/FG pairs are ridges; GG cross-row iff first-row zero column i<=second-row zero column k, with i>k forcing four zero coordinates, hence codim>=4. Same-row GG all ridges. Pair counts are q-2 adjacent FF, (q-2)(q-3)/2 disjoint FF, FG signed 2(q-1) each and orthogonal 2(q-1)(q-2), GG (3q^2-q)/2, summing (2q-1)^2. Gram products produce beta, pi/3, alpha, right, pi-beta. The exact mean cancels opposite beta classes, leaving -(q-2)pi/(6(2q-1)^2) and -((3q²-q)/2)asin(1/(2q-1))/(2q-1)^2. At scale q rare pi/3 ridges cause -pi/24 discrepancy despite vanishing probability; an explicit nonuniform integrability phenomenon. Independent numeric recomputation through q=10000 and inspected rational rank verifier for q=2..7 corroborate finite cases, not all-q proof.

## originality

PASS

Erickson-Kretschmann establish the same Monge polytope and facet/vertex census, but the inspected theorem has no full angle spectrum nor rare-ridge moment defect. Related public Resultary mean-width and surface-area findings concern different functionals. The related two-row 2-assignment polytope angle theorem has entirely different vertices/facets and does not imply Monge angles. Historical priority qualified versus unindexed metric papers.

## value

PASS

Complete all-q Euclidean ridge-angle spectrum of a natural Monge polytope, including a measurable failure of uniform integrability where the scaled mean differs from the weak-limit mean. This is nontrivial facet incidence geometry and a motivated sharp finite-to-asymptotic contrast rather than arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
