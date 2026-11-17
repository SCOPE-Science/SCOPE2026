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

The two displayed syzygies identify the blow-up incidence P1-bundle over the minor plane; restricting to a smooth conic makes a finite birational normalization of the quartic. The Serre-dual 8x8 evaluation matrix has determinant -1 on the exhibited conic, forcing balanced splitting Q=O(2)². The conductor E is the (2,2) incidence curve, smooth genus one; duality gives conductor divisor class (2,2), hence reduced with coefficient one. In char2, the quadratic middle coefficient B(u,v)=uv for that conic has two distinct simple zeros; Riemann–Hurwitz gives total different degree four, so each wild e=2 branch contributes exactly two. The F2 split-normalization correction #S=#Y-#E+#C and #E(F2)=4 imply Frobenius trace -1 and a_n=-a_(n-1)-2a_(n-2), hence the stated zeta function. Independent sympy reconstruction found balanced splitting determinant -1 and direct rational counts #E(F2)=4 and #S(F2)=8; finite extension checks in inspected source run to F16, but the zeta formula rests on the geometric normalization argument.

## originality

PASS

The classical secant-scroll construction and normalization geometry are covered by Polo-Blanco, van der Put and Top (their quartic classification assumes char zero or >3). The wild two-branch different-exponent law and exact characteristic-two finite-field zeta are not assertions of the inspected classical work. Other char-two quartics in Resultary (Steiner Roman, Burkhardt, etc.) are different varieties.

## value

PASS

Characteristic-two collapse from four tame complex pinch points to two wild branches and an exact finite-field zeta quantify a natural degeneration of classical quartic scroll geometry. The conductor and Frobenius corrections are specific reusable invariants of this singular ruled surface.

The dated certificate retains the supplied scientific assessment, sources and limitations.
