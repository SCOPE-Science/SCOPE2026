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

This passes the repaired statement. The frozen proof omitted the change of model: the first tabulated line y+ez=0 is not a bitangent in the cyclic coordinates, where restriction has a simple zero at (1:0:0). In the cited Ciani coordinates the quartic is x^4+y^4+z^4+3e(x^2y^2+x^2z^2+y^2z^2), the Klein member of the pencil. Both plane quartic embeddings are canonical; their projective equivalence carries the entire incidence graph. I checked all 28 binary-quartic restrictions on the symmetric model over the quadratic field; each has even intersection multiplicities. I matched the 21 reflection-line equations to Gévay–Pokora §2.1 and independently reconstructed both incidence graphs by exact concurrent-triple determinants, recovering the intersection counts and checking the labelled bijection on both entire edge sets. The simple zero of the characteristic polynomial ensures connectedness. Two independent incidence minors have determinant 2^18 3^23 7^5 and prime-local elimination gives 36 units and twelve nonunits 2^4, 18, 54, 108, 756^5 (multiplicities). The repair corrects the frozen proof's count of eleven and notes why the mod-two quotient forces at least twelve generators. The geometry is invariant under coordinates, so the corrected proof retains the asserted cyclic-model graph rather than computing a different object.

## originality

PASS

Best of current knowledge, the supported distinct result is the full integral group of the specific 49-vertex Klein Levi graph and the resulting numerical obstructions. Neither the arrangement, the tabulated incidences nor the geometric duality is claimed as new. The strongest related exact results change which point multiplicities are retained, and the identical catalog record is the assigned one. A specific residual literature risk remains.

## value

PASS

This is the complete flag graph of the classical bitangent/fourfold-crossing configuration and hence a natural named geometric incidence object. The integral chip-firing group, its exponent and its generation rank make precise the divisor-class obstructions on that graph, independently of which known geometric model is used. Those obstructions would not be provided by the incidence or tree count alone or by the closely related quadruple-only group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
