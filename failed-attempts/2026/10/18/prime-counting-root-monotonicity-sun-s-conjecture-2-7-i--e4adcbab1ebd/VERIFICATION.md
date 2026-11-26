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

For A=π(kn), B=π((k+1)n), the real-root inequality and the strict integer-power inequality are equivalent because both counts are positive. For n≥300, the Brun–Titchmarsh interval estimate with start kn and length n, and the Rosser–Schoenfeld lower bound at kn, apply within their stated ranges. They give k log(B/A)≤k(B−A)/A<2 log(kn)/log n≤4, where kn≤n²; if B=A the strict upper bound is immediate. Meanwhile log A≥log 62>4, using the elementary exponential series bound e<11/4 and (11/4)^4<62. The independent segmented-sieve exact replay covers every n=5,…,299 and k=1,…,n, confirming all 44,840 inequalities, π(300)=62, and minimum positive margin 4 at (n,k)=(6,1). The threshold and finite range join without a gap.

## originality

FAIL

The entire stated mathematical finding is a direct restriction of the distinct indexed result abe6896d468d, which treats all k≥1 on every n≥5 ray and more. This is demonstrable stronger coverage, not a decision about priority or authorship: both records are catalogued on the same day, and the stronger record acknowledges an unnamed bounded-index proof. The assigned claim is a theorem on the bounded-index domain, not a finding about a distinct proof method or about the companion conjecture. Its proof is valid, but no distinct mathematical conclusion survives this comparison.

## value

PASS

Strict root monotonicity of prime counts across Sun's precise uniform domain is a motivated conjectural question, not a selected list of numerical instances. The bounded-index argument combines established inequalities and a finite exhaustive boundary proof. The value of the question and correctness of this argument do not give the conclusion scientific distinctness relative to the covering record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
