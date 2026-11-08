---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Nonnegative balanced Eulerian binary order2 de Bruijn multigraphs give profile coordinates (a,b,c,d,b,c+d-b,d,h), n=a+h+b+2c+3d. Five disjoint connected-support cases yield GF 2z/(1-z)+z²/(1-z²)+2z³/((1-z)(1-z²)(1-z³))+z4(1+z³)/((1-z)²(1-z²)(1-z³)(1-z4)). Pole order 5 at z=1 yields n^4/288. Independent full binary word profile enumeration n=1..14 checks values; exact symbolic rational simplification proves this GF IDENTICAL to earlier record3 GF (not just first coefficients).

## originality

FAIL

Decisive prior coverage: same repository record3, committed 2026-11-02T04:19:35Z, gives identical observable, full all-n GF, and strictly stronger exact period12 quasipolynomial. This record5 was committed 2026-11-02T04:21:18Z. Algebraic rational identity exact, not a near-match by title. Its leading growth, coefficients and optimal code cardinality are immediate corollaries, so claim is covered.

## value

FAIL

In this historical context record5 merely re-enumerates an already published exact natural invariant, with no new structural lemma, boundary, faster algorithm, or more precise conclusion beyond strictly stronger record3. Correct finite verification cannot rescue independent value from a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
