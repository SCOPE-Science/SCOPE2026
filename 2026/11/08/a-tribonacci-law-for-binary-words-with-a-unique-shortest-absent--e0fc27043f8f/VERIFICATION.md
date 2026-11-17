---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For any nonunary binary word x^r y t (y opposite x), the first-occurrence recurrence partitions absent subsequences by first letter. The missing-length recurrence is L(w)=1+L(t) and c(w)=c(t)+1_{L(w[2..])=L(t)}c(w[2..]). The proof correctly characterizes uniqueness by a nonempty unique-SAS tail with r>=2, or r=1 and the tail beginning with x; unary words supply the base. The exact unambiguous grammar yields F=z/(1-z)+uz²F+2uz³/(1-z)F, hence 2F=2z/(1-z-uz²-uz³) and coefficient formula. Independently re-enumerated literal absent binary subsequences and all n,k counts through length 10; all matched. The all-length claim follows from the grammar, not finite checks.

## originality

PASS

Best of knowledge: earlier general-alphabet characterizations establish membership of 1-nearly k-universal words, and existing sequences exhibit tribonacci coefficients in other meanings. None of the accessible relevant prior statements examined gives the exact number of individual binary source words refined simultaneously by length n and universality k or the bivariate rational series. General membership algorithms do not by themselves state the evaluated enumerator. Residual risk remains that this series is implicit in unexamined Simon-congruence class counts.

## value

PASS

Unique shortest absent subsequences are a natural boundary of substring/subsequence universality; the exact number of binary words of each length and universality level, together with a clean constructive grammar and exponential rarity constant, is a motivated useful counting invariant. The scalar tribonacci sequence alone is familiar, but the interpretation and bivariate refinement are not merely an arbitrary numeric coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
