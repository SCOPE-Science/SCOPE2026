---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Example 4.1 gives the fixed plane curve, distinct from the ambient K3. On taking a coordinate-sign quotient, squaring the flipped coordinate gives a quadratic; its discriminant is 32(t⁴+3t²+1) for x₀ and 32(t⁴−3t²+1) for each of x₁,x₂. These give smooth genus-one models after rescaling over ℂ (the two distinct nonzero roots for t² yield four distinct roots), and t→it identifies the two forms. Substitution u=(w+1)/t² gives (u²−1)t²=2u+a, so X=2u and Y=2t(u²−1) yield the stated cubic with roots −2,2,−a. The Legendre parameter is (2−a)/4=−1/4 or 5/4, giving j=148176/25 by the Legendre formula. Exact independent checks: python3 -B /workspace/audit-evidence/4_legendre_check.py, output in 4_replay.txt in that directory. Squaring all coordinates gives the full sign-group quotient (generic fibers are the sign orbits); its conic determinant is −80. The invariant holomorphic forms for each involution thus have dimension one and no common trivial character, so they are the three different nontrivial Klein-four characters. By conjugation over ℂ the same holds for H¹(O), the tangent space of Pic⁰, so the sum of pullbacks on the Jacobians is an isogeny onto Jac(C). No product polarization or isomorphism of underlying abelian varieties follows.

## originality

FAIL

Howe–Leprévost–Poonen Proposition 15 and its proof already give the plane Ciani-quartic construction, the coordinate-sign quotient formula and the product pullback isogeny (indeed its degree and polarized kernel description). After the diagonal change x₀=iX, x₁=Y, x₂=Z, Example 4.1 is exactly a single specialization with symmetric mixed coefficients −6. The required parameters and j follow by direct substitution, not by a new theorem about a special locus.

## value

FAIL

The fixed curve and its Jacobian are natural objects, but the three models and common j are direct evaluations of existing Ciani quotient formulas and the cube isogeny follows already from the explicit prior construction. Reporting the arithmetic evaluation for the K3 example is useful exposition, not a surviving unknown exact invariant under the audit standard. There is no substantiated distinct claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
