---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

In the weighted projective plane P(1,1,2), all odd degree k=2r+1 monomials x^p y^q a^j have p+q+2j=k. Eliminating p gives full lattice points (q,j) in trapezoid conv((0,0),(k,0),(1,r),(0,r)). The four primitive inward normals (1,0),(0,1),(-1,-2),(0,-1) have adjacent determinants 1; the extra ray resolves the unique determinant-two cone, giving a -2 exceptional section and smooth toric surface F_2. All weighted odd-degree monomials vanish only at [0:0:1] and the full polytope linear system embeds resolved F_2. Normalized area 2Area=(k²−1)/2. Independently checked all fan determinants, ray relation and area symbolically and for r=1..19; no issue with stated restricted geometric result.

## originality

FAIL

The previously published exact polarized toric polygon already implies the new abstract F2 identification by standard fan theory; title/nonliteral notation cannot rescue originality.

## value

FAIL

The isomorphism and smoothness are mathematically useful descriptions of natural surfaces, but the complete toric polygon and weighted-projective model already occur in primary work. Reading off normals, checking four 2×2 determinants and recognizing the standard F2 fan are routine consequences of that exact source, rather than a distinct unknown geometric invariant or motivated gap left open by it; as a new independent finding this fails the substantive-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
