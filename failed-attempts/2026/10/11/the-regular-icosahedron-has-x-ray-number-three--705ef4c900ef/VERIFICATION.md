---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The assigned RESULT.md gives all twelve explicit vertices over Q(sqrt5), identifies twenty triangular supporting faces, and lists five outward facet normals at (phi,0,1) with strictly positive x-coordinates. Signed-coordinate and cyclic symmetries cover all vertices by the coordinate lines; the Gauss-image inclusion nu(F) subset nu(v) extends vertex coverage to faces. The lower bound X>=dimension makes 3 sharp. The actual verify.py was examined, not inferred from VERIFY_OK; its exact facet, support, normal, hemisphere and 1/3-cosine tests match the proof. The finite model only certifies the explicit icosahedron, which is all the claim asserts.

## originality

FAIL

A fully read published classification already proves X(I)=3 as a literal theorem component, using exactly the same standard vertex model, normals and three coordinate axes. Thus the candidate is a special case of a strictly stronger existing classification; different title or separate checking cannot create new originality.

## value

FAIL

Although the exact X-ray number of a regular solid is a natural invariant, the entire result and its explicit line certificate already occur in the broader published five-Platonic-solid classification. The candidate provides no new regime, bound, obstruction, or independent motivation beyond that published special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
