---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Two n-multisets are confusable exactly when their multiset intersection contains a size-two multiset. Choosing any doubled symbol of each repeated-symbol word gives distinct symbols across such words, because a common doubled symbol would be a common two-survivor output. Replacing these words by their constants is injective, preserves the distinct-symbol words, and introduces no conflicts. Missing constants can be added; the distinct-symbol part is exactly an n-uniform pair packing. Counting and the reverse construction establish both the identity and the existential normalization. For n>q there are no packing blocks, and for n=q there is one. For n=2 the expression is q+binom(q,2), the total number of length-two multisets, as expected when no deletions occur. The maximum partial triple-system formula gives the four residue classes by elementary simplification, including q=2 via the empty packing convention.

## originality

FAIL

The revised motivating paper, arXiv:2601.05636v2 (13 July 2026), states exactly this all-parameter theorem in §4.3, Theorem 10. Its repeated-symbol argument mechanically gives the proposed normalization. The frozen prior-work discussion is applicable to v1, not to the relevant v2. The length-three coding specialization also predates the record in the constant-weight ℓ₁-metric literature. This failure is established by matching mathematics in accessible primary sources, not by an unavailable source or a search hit.

## value

FAIL

The coding-to-packing theorem is useful, but is already available with the same argument, and the injection and numerical corollaries follow mechanically. Restating the result with another label or attaching the small MILP comparisons adds no distinct scientific finding. No genuine surviving repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
