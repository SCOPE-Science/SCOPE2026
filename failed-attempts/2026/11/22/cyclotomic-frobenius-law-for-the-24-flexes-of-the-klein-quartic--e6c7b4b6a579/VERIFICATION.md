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

The actual Finding is correct for the fixed smooth plane model and p >= 5, p != 7. Independently reconstructed the Hessian, verified both equations at the four coordinate representatives modulo Phi_7, formed the minimal polynomials by orbit products, and recomputed the separation discriminants and cross-resultants. The nonzero affine eliminant excludes common components (the line at infinity is not a component); the 22 distinct affine projections and two infinity points exhaust the degree-24 intersection, with every local length one. In these characteristics the Hessian detects tangent contact m=3 or 4 with local order m-2: in local tangent coordinates it is a unit times the second derivative of the local graph, and m(m-1) is invertible. Thus all 24 flexes are ordinary. Three fixed vertices, a three-element orbit with stabilizer {+1,-1}, and three regular sextic orbits give all rows, extension counts and zeta factors, and the last three orbits force the stated exact splitting fields. Minor sign error in the proof/certificate, not in the Finding: with the standard convention Res_y(f,h)=Norm(h mod f) for monic f, the resultant is +xABCD, not -xABCD. The Sylvester determinant at x=1 is -232, whereas SymPy 1.14.0 resultant reports +232. The proof uses the eliminant only up to a unit. Reproduction: python /workspace/flex_and_octic_reproduction.py (SymPy 1.14.0); frozen VERIFY.py inspected, not executed.

## originality

FAIL

The distinct same-day Resultary record 1b8d3c6d03f9 proves the identical uniform arithmetic classification of the same 24 flexes. This is demonstrable coverage, not a chronological priority finding. The coordinate certificate is an alternate proof of the same classification, not a distinct claim of the Finding. Earlier characteristic-five and geometric coverage is also real but narrower.

## value

FAIL

A complete Frobenius law for a natural flex divisor is useful: it gives extension counts and splitting degrees exactly. As a separate finding, however, this record gives no new such invariant or new range beyond the equivalent record. The explicit representatives are useful as proof data, but the submitted finding does not identify a separately needed fact or a substantive simplification beyond alternate certification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
