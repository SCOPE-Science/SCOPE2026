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

Pinned RESULT.md gives exactly n triangles T_i of C_n^2 for every n>=7, 2n edges and n vertices; vertex links form a surface, boundary edges {i,i+2} form gcd(n,2) circles, and Euler characteristic zero determines annulus or Mobius. No rotation-stabilized nonempty simplex exists: an orbit of size two is antipodal distance >=3 and orbit of size three spacing >=3. The invariant face poset of each reflection has components of cardinalities (3,1), (3,3) or (1,1), geometrically interval-plus-point/two intervals/two points. Cyclic quotient boundary parity gives annulus/Mobius; for any reflected subgroup rotations are free, fixed-set Euler=2 per reflection and Burnside quotient Euler=1. A surface quotient with boundary and chi=1 is disk. I independently reviewed the package verifier combinatorics; its n=7..30 range is corroboration only, not used to infer n>=7 proof. Important local mirror-versus-isolated halfturn neighborhoods do not prevent the quotient being a surface.

## originality

PASS

Best-of-knowledge original part is the actual fixed-point and quotient classification, NOT the known ambient annulus/Mobius classification. Compared the same C_n^2 family against Wani abstract, indexed Resultary findings and exact subgroup geometry; full Wani text remains inaccessible and materially risky; this alone does not prove priority failure.

## value

PASS

A full all-subgroup geometric fixed and quotient classification of the natural dihedral action on a standard infinite family of scale-two cyclic Rips surfaces is a motivated equivariant topology problem. The annulus/Mobius nonequivariant result is known and alone has no claimed value; exact reflection-fixed components and disk quotient for every reflected subgroup are stronger structural consequences useful in equivariant topology and orbit stratification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
