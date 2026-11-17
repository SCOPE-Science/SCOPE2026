---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The specified characteristic-two symmetric determinant is F=abc+af²+be²+cd²: its diagonal partials are exactly bc+f², ac+e², ab+d², and off-diagonal partials vanish. Euler (3=1) eliminates F. The three affine charts a,b,c≠0 cover the projective scheme, each giving k[d,e,eps]/(eps²), eps=f+de. Their radical glues as ν₂(P²), and a codimension-three complete intersection of type (2,2,2) has dualizing sheaf O, degree eight and Hilbert polynomial 4m²+2. Square-zero ideal is ω(P²)=O(-3); H¹=0. The Picard retraction argument rules out global splitting; Ext¹(Ω_P²,O(-3))=H¹(T(-3))=k yields uniqueness of the nonsplit abstract ribbon. Chart/Ext arguments checked directly; the optional mod-two script and finite Hilbert checks were inspected in source tree and not treated as proof of global facts.

## originality

FAIL

FAIL: an October 18, 2026 published theorem about the symmetric 3-by-3 PERMANENT states the IDENTICAL characteristic-two determinant polynomial and intrinsic Jacobian ideal, nonreduced Veronese support, square-zero ideal O(-3), complete intersection, degree eight, dualizing sheaf, H¹, and exact Hilbert polynomial. In characteristic two permanent equals determinant, so a title/parameter distinction is fictitious. The submitted global nonsplitting and Ext¹ uniqueness are direct standard consequences of this already-determined scheme, not an independent new geometric classification.

## value

FAIL

FAIL: while the first identification of this singular-scheme geometry would be worthwhile, its scheme, K3 properties and all numerical invariants had already been explicitly determined. The residual nonsplitting statement follows by the elementary Picard/retraction obstruction and the one-dimensional Euler-sequence Ext computation; no independently motivated new theorem or classification remains after prior coverage. Correctness and new packaging do not establish new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
