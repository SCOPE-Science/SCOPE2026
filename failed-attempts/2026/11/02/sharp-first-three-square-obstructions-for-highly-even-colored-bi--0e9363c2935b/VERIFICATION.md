---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Formal-log differentiation gives b_m(n) polynomial recurrence and exact rational margins [∞,6,5,5,4,4,4,4,3,3,3,3,3,3] for n≤14 at k=6. This yields v2(b_m(n))=k−v2(n) and normalized unit u(2^{v2(n)+1}−1)/(n/2^{v2(n)}) mod 8 for every m=2^ku, k≥6, odd u. Legendre three-squares criterion gives the table (u≡1:4/8;3:5/14;5:3/2;7:1/6, for even/odd k). Independent exact-integer recurrence checked the first low-power obstructions 34,10,13,4,8 and m=96→18. Also independently confirmed published even-m power-series congruence recovers ALL required first-14 residues.

## originality

FAIL

The 2023 Sobolewski–Ulas primary paper already states the GENERAL even-m generating-function congruence B_m(x)≡(1−x)^m(1+2mP(x)) modulo 2^{ν₂(m)+3}. For m divisible by 64 this is strong enough to determine, by straightforward coefficient extraction through n=14, the entire needed normalized residue table and Legendre obstructions. Direct independent check confirmed these exact first-14 values. The claim is thus a routine first-index specialization of a stronger published statement plus Legendre and finite tabulation, even though the exact table and low-power sample values are not expressly printed in that paper. Originality must be assessed by implication, not missing wording; the remaining small computations do not establish an independent broad claim.

## value

PASS

The first forbidden coefficient for natural colored binary-partition sequences is a well-motivated finite invariant. The exact small-index and high-divisibility cutoff table is useful for testing Diophantine partition questions, although not a classification of all forbidden indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
