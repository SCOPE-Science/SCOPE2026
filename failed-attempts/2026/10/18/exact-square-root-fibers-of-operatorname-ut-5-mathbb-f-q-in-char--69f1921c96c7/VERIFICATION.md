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

Multiplying N by itself gives the six target entries and the free corner. When a=d=0 the remaining constraints give the outer product (b,e)^T(c,g); zero and nonzero rank-one outputs have respectively 2q²−1 and q−1 factorizations. Otherwise the final equation contributes q choices for (h,i). For B≠0 one can choose b and f, with c, a, d, e, g then fixed; for B=0 and A alone nonzero, c=0, b is nonzero, a and f are determined, d and e are free, and g is fixed (the C case is symmetric). When A=B=C=0 and (a,d)≠(0,0), b≠0 forces D=0 and contributes q⁴(q−1)², c≠0 gives its mirror, and b=c=0 leaves (D,E)=f(a,d). This reproduces all strata, including the exceptional identity. The five positive sizes are strictly ordered for q≥2. The only forbidden targets within the six coordinates number q²(q−1)²+q³(q−1)², giving the stated image polynomial. An independent complete enumeration matched every target for q=2,4,8 (including all 262,144 targets for q=8) and total mass q^10.

## originality

FAIL

Distinct content is not established against a separate indexed finding that explicitly supplies the entire prescribed-target table over every even q, as well as the spectrum and image polynomial. This is verified equivalent coverage, not an inference that the other record historically came first, nor a conclusion about authorship or dependence. The membership and image polynomial are also already stated in a different catalogue result; removing those and the known identity fiber does not remove the full overlap.

## value

FAIL

An all-field prescribed-fiber classification in this first nonsurjective dimension is a useful exact invariant in isolation. As a distinct contribution, however, the frozen result supplies no additional invariant, scope, or consequence beyond an available exact table and its target strata; a second correct computation of those same data does not establish new scientific value under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
