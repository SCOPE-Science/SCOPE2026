---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

FAIL

Decisive contradiction in the final theorem and its proof: K is a directed-flag complex of a tournament, so every induced subcomplex on five vertices has all C(5,2)=10 directed edges. The asserted boundary of the triangular bipyramid has only nine edges. In the explicitly claimed representative W={0,1,2,3,7}, the six transitive triangles are 013,017,023,027,137,237 and use all edges except {1,2}; that extra edge is a loop chord between bipyramid apices. Thus K[W] is a bipyramid S² with one attached apex-apex 1-cell, homotopy equivalent to S² ∨ S¹, not a sphere. This contradicts repeated literal "every corresponding induced complex is the boundary" and face count (5,9,6). Independently reconstructed all 462 five-subsets with exactly 55 H2=1 and 407 H2=0, face vector (11,55,110,55), free affine orbit of 55, unimodular cycle coordinates, Smith factors (1^54,2) for tetrahedra and (1^65) after adjoining sphere cycles. Hence the valuable integral-surjectivity subtheorem survives unchanged, but the original combined final claim C FAIL and cannot be passed using a caveat.

## originality

PASS

The surviving induced-H2 carrier census and integral surjection are more refined than Govc’s previously established ambient abstract H2; however the submitted additional claim that these induced subcomplexes are sphere boundaries is false. No originality acceptance can override that correctness failure.

## value

PASS

For the canonical Paley-11 torsion example, the exact minimal-support census and integral spanning of the global H2 including the Z/2 class are motivated and not dictated by its known Moore-wedge homotopy type. A repaired precise claim about the bipyramid triangle subcomplexes would still be mathematically valuable. This does not rescue a false submitted statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
