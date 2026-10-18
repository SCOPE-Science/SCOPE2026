---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The centered unit-edge icosahedron has twelve vertices (0,±1,±φ)/2 and permutations, radius squared (5+√5)/8, and support width w(u)=2h(u). Its twelve vertex-normal spherical pentagons have side inradius sinδ=1/(2R), with sin²δ=(5−√5)/10. Polar integration in five sectors of half-angle α=π/5 has boundary tan θ_b=tanδ/cosψ; integrating cos²θ gives I_C=(5/3)(2α−J), and substitution x=sinψ evaluates J exactly, yielding I_C=π/9+10 sin²δ/(3√3). Multiplying by 12R²/π gives (5+√5)/6+10/(π√3), with 4R² sin²δ=1. Reviewed verify.py: exact Q(√5) coordinates, 30 edges and valency five, plus deterministic numeric quadrature, which is corroborative only. Also checked equivalent term against the complete Platonic table.

## originality

FAIL

The exact same icosahedral second moment appears as an explicit entry of the already-public stronger Resultary finding "Mean-square widths of all five Platonic solids", with the same unit-edge normalization and same pentagonal normal-cell proof. Therefore the audited single-object value is covered by a full-family table. Both records were co-published in the same October 11 reconciliation commit; no chronological priority assertion is made, but a second separately claimed original icosahedral value adds no uncovered result.

## value

PASS

The second random-direction width moment of a regular icosahedron is a natural exact metric invariant, and a transparent spherical-cell evaluation is intrinsically worthwhile; these are not arbitrary numeric slices. Its standalone claim is nevertheless redundant with an existing full Platonic table and cannot pass originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
