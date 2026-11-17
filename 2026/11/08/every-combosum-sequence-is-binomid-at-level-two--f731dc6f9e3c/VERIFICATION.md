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

For any prime p and height r, valuations of f define additive submonoids S_{p,r}. For finite S prefix count F, integer sumset growth yields Delta(u,k)=F(u+k)-F(u)-F(k)>=0. The strict refinement when 1 not in S and u+1 in S follows from equality of finite sumsets: if both initial prefix sets have >=2 members they must be common-step arithmetic progressions; the two elements u+1,k+1 then produce a further in-range semigroup element beyond the equality sumset, contradiction. Each prime-valuation exponent of B_c(u+k,k) decomposes exactly as Delta(u,k)+Delta(u,k+1)+a_1-a_(u+1), always nonnegative including u=0, k=0, a1=1. Sum over finite heights gives integrality for all primes and signed sequences. Independently checked ALL additively closed masks through index 12 (171, 11286 inequalities), without using finite checks as universal proof.

## originality

PASS

Shapiro 2023 explicitly asks if every ComboSum sequence is binomid at every level; his Proposition 23 proves only baseline binomid and Theorem 15 provides all levels for the narrower divisor-product class. The complete Oct26 interlaced-divisor-chain theorem covers a proper subclass not every ComboSum, while its proof uses f_n|f_(n+2) unavailable for arbitrary additive semigroup supports. The new uniform level-two semigroup strict-refinement theorem is not implied by inspected known results.

## value

PASS

It settles the first genuinely open level of a named natural all-level divisibility question for the full ComboSum class, rather than a convenient subgroup, using an independently meaningful additive-semigroup equality-rigidity inequality. Higher-level conjectures remain open; this bounded first-level partial resolution is substantively valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
