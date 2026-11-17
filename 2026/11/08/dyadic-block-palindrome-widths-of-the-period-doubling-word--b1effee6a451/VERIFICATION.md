---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: The shortest proper border of any word is unbordered and nonoverlapping; refining any longer chosen outer border forces lower maximum width, so greedily removing shortest borders is optimal. For binary period doubling p(i)=v2(i+1) mod2, the reflection p(n−1−a)=v2(a) mod2 for n=4^m classifies each remaining boundary group into either two mirrored single-symbol borders or one mirrored two-symbol border, ending in center 10. Counting even v2(j) produces L_{2m}=(2·4^m+1)/3. For odd exponent the injective uniform morphism maps borders to doubled borders and excludes odd lengths because intermediate centers end in 0. Thus L_{2m+1}=L_{2m}. Independently optimized all outer-border options by dynamic programming for k≤8; universal result rests on valuation proof.

## originality

PASS

PASS best-of-knowledge: Generic greedy largest block-palindrome factorization was already known from Goto–I–Bannai–Inenaga and Gabrić–Shallit, and is credited. The period-doubling word itself has established palindromic Ziv–Lempel and Crochemore factorizations, a different invariant. None of the inspected general block-palindrome statements yields the all-k exact dyadic formula or alternating normalized limits without nontrivial 2-adic boundary counting. Other Resultary period-doubling width results concern repetition factorization, not mirrored-equal blocks.

## value

PASS

PASS: The natural maximal block-palindrome width for a canonical automatic word is classified for every dyadic prefix with an explicit greedy structure and asymptotically alternating 2/3 and 1/3 normalized subsequential limits. This exact infinite family is not a generic algorithm restatement or tiny finite improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
