---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The claim is restricted to the hull [0,1/m], not the complement in [0,1]. At a point's first escape, its preceding iterate y has a=floor(1/y)≥m and 1/m<T(y)<1 exactly when L_a<y<R_a. Pulling it back through the preceding digits gives the listed gap. Conversely each such interval escapes at the specified step; its endpoints survive since L_a maps to 0 and R_a to 1/m, which itself maps to 0. The first escape and its pre-escape digit identify the gap uniquely. This also gives an open complement in the hull and avoids any assumption of continuity of the Gauss map at rationals. Multiplying the inverse-branch Möbius matrices gives unit absolute determinant and denominator q_k+q_{k−1}t, so the length formula includes the empty prefix. The root lengths strictly decrease with a and every nonempty prefix satisfies |f_w(x)−f_w(y)|≤m^{−2|w|}|x−y|. The maximal normalized distance is thus m(R_m−L_m)/2, with the claimed limit. The nonterminating set is covered at depth j by intervals of total length at most (sum_{a≥m}a^{−2})^j/m, tending to zero since sum_{a≥2}a^{−2}<sum_{a≥2}1/[a(a−1)]=1. The terminating survivors are countable, so the disjoint gaps have total length 1/m.

## originality

FAIL

The exact formulas are correct but the geometric claim is mechanically implied by the already indexed full-shift branch description at the same reciprocal parameters, plus the elementary rational endpoint check and standard Möbius subtraction. This is implication, not a claim that the earlier source printed the distance formula or that dimension determines distance.

## value

FAIL

The exact gap sizes and sharp filling rate are natural observables, but in this full-branch reciprocal case they are immediate from the prior interval endpoints, uniform contraction, and the half-largest-gap identity. The frozen work adds neither a new restriction on the coding nor independent control of an otherwise unresolved geometric invariant. No distinct valuable remainder is established by the record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
