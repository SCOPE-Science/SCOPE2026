---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For w_i=1 at exactly i=2^j (j>=0) and w_0=0, k(n) counts marked positions and h=ceil(k/2). Distinct powers cannot form a 3-term progression or collide as two-pair sums; each palindromic factor contains <=2 ones, establishing the lower bound. Checked the reflected two-marker construction E_-1=0,E_j=3*4^j+1-E_{j-1}, two-case all-prefix factor split, and forced all-zero final palindrome at 2^r-1 (including r=2). Thus h<=P(n)<=h+1 all n>=0, P(E_j)=j+1, P(2^r-1)=ceil(r/2)+1, and P(n)=0.5log2(n)+O(1). Independent direct palindrome DP for all 700 prefixes reproduced both boundaries and examples. This finite DP corroborates, but the infinite proof is the reflection/counting argument.

## originality

PASS

The object is the binary power-marker word and invariant is minimal number of prefix palindromes, not number or length of distinct palindromic factors. Full geometric-marker factor-language theorem covers the same exact word but only occurrence/spectrum/maximal factors, not the constrained optimal tiling of every prefix. Full accessible Frid–Laborde–Peltomäki automatic-word paper treats different automatic families and general regularity, not this two-value power-marker profile. Best-of-knowledge original with bounded priority risk.

## value

PASS

A canonical sparse automatic sequence receives an all-length one-unit pinning bound, an exact logarithmic growth coefficient and two unbounded sharpness families. It answers a motivated prefix-factorization invariant rather than a tiny arbitrary slice, even without exact dichotomy at every nonextremal n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
