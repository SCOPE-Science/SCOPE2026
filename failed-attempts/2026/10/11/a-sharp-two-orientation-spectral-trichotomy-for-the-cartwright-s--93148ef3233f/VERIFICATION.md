---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

From the source characteristic polynomials, a_+(m)=2-3m²-m³, a_-(m)=2-3m²+m³. A reciprocal real quadratic z²-az+1 has unit-circle roots iff |a|<=2 and spectral radius (|a|+sqrt(a²-4))/2 otherwise. Direct exact integer calculations for m=-5..5 reproduce all small exceptional cases; elementary monotone inequalities show |a_±(m)|>=18 for |m|>=4. The sharp boundary is rho(18)=9+4sqrt(5). Source trace identity translates m to the stated secondary parameter, but m itself remains undetermined. No dynamics or pseudo-Anosov implication is claimed.

## originality

FAIL

Decisive stronger prior coverage: the focal primary Propositions 5.1 and 5.2 already supply exact characteristic polynomials for BOTH twist orientations as functions of the same m, together with the trace identity. Applying the textbook reciprocal-quadratic modulus criterion yields precisely the submitted regimes and sharp numerical threshold without new geometric input.

## value

FAIL

The source already gives a complete spectral description for all integer m. Replacing the exact characteristic polynomial with a three-case |m| table and one threshold uses routine root-discriminant inequalities; it neither computes the unresolved geometric intersection m nor establishes independent topology or dynamics. This is a mechanically implied special case rather than an independently motivated unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
