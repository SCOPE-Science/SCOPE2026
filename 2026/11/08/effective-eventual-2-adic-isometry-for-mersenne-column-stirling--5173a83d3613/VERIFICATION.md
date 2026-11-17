---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For k=2^m-1,m>=4,h=v2(k!)=2^m-m-1, n>=max(m,h+1),2^n>=n+2+h+v2(a-b), normalized inclusion-exclusion yields quotient congruent F(2)-F(1) mod 2^{n+2} for all a>b>=1. Odd j: q_j=j^{2^n}=1+z_j with v2(z)>=n+2; divided difference binomial tail v2>=2n+3; multiplying by coefficients loses ≤h. Even j: v2((q_j^a-q_j^b)/(a-b))≥2^n-v2(a-b), and explicit second cutoff handles it. Zhao-Zhao-Hong Thm1.3 gives v2(F(2)-F(1))=n+1; therefore exact difference valuation n+1+v2(a-b). Verified independent modular Stirling cases for k=15 and 31 and multipliers 2,3,17,257 (b=1), including large dyadic separation. Assumptions avoid low-index exception.

## originality

PASS

PASS for all-m≥4 normalized isometry and effective cutoff; 2014 theorem covers adjacent doubling only, and published 2026-10-18 two-scale theorem covers k=15 (m=4) for all multiplier pairs and its resonant boundary. Neither states or implies the uniform all-Mersenne-column normalized quotient congruence or the infinitely many k≥31 cases; material prior k=15 overlap is explicitly acknowledged.

## value

PASS

PASS: transfers a known single-multiplier valuation to all multiplier pairs with explicit finite cutoff, closing a natural open family in 2-adic Stirling difference studies for every Mersenne block count k≥31. The isometry has a meaningful global quantifier and excludes sporadic low-precision exceptions; not merely one substituted value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
