---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The five partial derivatives of x0u²+x1uv+x2v² are (u²,uv,v²,2x0u+x1v,x1u+2x2v), and f lies in (u,v)². Thus the relative Jacobian quotient is the split graded square-zero algebra A⊕M with two-term presentation [[2x0,x1],[x1,2x2]] and determinant Δ=4x0x2−x1². The matrix remains injective modulo every prime because Δ remains nonzero, proving Z-torsion-free graded pieces and flatness. For char≠2 the smooth conic parameterization [s²:2st:t²] factors matrix into a rank-one map and Euler sequence gives i_*O_P1(-1). In char2 the matrix is [[0,x1],[x1,0]], with cokernel O_L(-1)^2 and Fitting ideal (x1²). The free resolution computes the all-degree Hilbert function binom(m+2,2)+2m. Independent symbolic derivative/determinant/Hilbert checks corroborated selected field/degree cases; all-base theorem rests on the resolution.

## originality

PASS

Gondim–Russo identify the classical Perazzo cubic and reduced singular plane. The Oct18 published exact Jacobian square-zero result covers the same odd-characteristic conic-supported theta sheaf and Hilbert series (after rescaling x1); none of those is claimed new here. That theorem explicitly excludes characteristic two. The integral model flatness and degeneration at two into two nilpotent line directions with doubled Fitting line survive as a motivated new arithmetic-scheme boundary.

## value

PASS

A canonical integral Perazzo model has constant reduced singular plane and Hilbert polynomial but a characteristic-dependent nilpotent sheaf: one conic-supported direction degenerates to two line-supported directions at two. This exact bad-prime scheme structure is a natural geometric degeneration invariant and not a trivial restatement of the known odd-fiber theta-line.

The dated certificate retains the supplied scientific assessment, sources and limitations.
