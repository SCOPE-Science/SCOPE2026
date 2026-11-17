---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The full quadratic equatorial trace fourth moment equals [2||A||_F²-4||An||²+3(n^TAn)²]/(d²-1) for tracefree real symmetric A, with normalized whole-sphere energy 2||A||²/[d(d+2)]. Splitting into W tracefree, e±⊗W, odd and even 2x2 blocks accounts for all d(d+1)/2-1 modes; the even generalized eigenvalue trace T_d and determinant (d+1)c²/(2d) give h±. The smallest K_d min{h_-,(1-c)/2} crosses at 3dc²+4c-d-2=0, yielding unique c*_d. The d=3 top eigenvalue must be treated separately. Independently reconstructed generalized crossing factor by SymPy and independently assembled d=3,4,5,8 fourth-moment matrices. These finite checks support the all-d structural proof.

## originality

PASS

The complete two-oblique-equator spectral frame theorem for ALL dimensions d>=3 has a nontrivial d>=4 extension. The d=3 optimum c=5/9 and exact Gram spectrum are already present in the six-node great-circle sampling theorem because triples quadrature-integrate squared quadratics; do not credit that special case as novel. The higher-d two-equator block spectrum and dimension-dependent optimal cosine do not follow from that d=3 source.

## value

PASS

Provides the full spectrum and a dimension-dependent, uniquely optimal oblique frame for a natural two-hyperplane continuous measurement problem on harmonic quadratic tensors. The d>=4 generality, stable bounded condition number, and exact design angle furnish a nontrivial useful classification despite the previously known d=3 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
