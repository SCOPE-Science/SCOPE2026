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

The stated object is distinct nonempty reverse-complement palindromic scattered output strings, not embeddings, for the ascending permutation of 2m symbols repeated k>=1. A target U=Vθ(V^rev) embeds iff its weak descent count d(U)=2D(V)+1_{last(V)>=m} is <=k-1. This is a genuine iff via greedy period changes. The transfer recurrence for halfwords ending at i has B_0=t(1+z²S), B_i=[1+t(1-z²)]B_{i-1}; adding the central θ-pair weight and summing gives the exact rational bivariate generating function. Its z coefficients are polynomial in t; empty target omitted. Independent brute subsets, deduplicated by resulting string, agree with halfword descent enumeration for (m,k)=(1,1),(1,3),(1,5),(2,1),(2,2),(2,3),(3,1),(3,2), including m=2,k=3 total 59. This checks finite cases only; symbolic recurrence proves all m,k. No contradiction detected in symmetry or normalization.

## originality

PASS

The new mathematical content is an all-even-alphabet, all-repetition distinct-output half-length bivariate rational identity with a proven θ-center correction. General ordinary palindrome/subsequence algorithms and published occurrence-weighted spectra are not the same exact invariant; relevant full primary texts and indexed related results were compared. No decisive covering implication found; residual risk explicitly retained.

## value

PASS

Reverse-complement constraints are natural in words with paired alphabets (e.g. complementary DNA symbols), and permutation powers are a canonical periodic host. Counting distinct strings rather than embeddings is a genuinely different, nontrivial deduplication invariant, and a closed bivariate generating function across all alphabet sizes, repetition counts and half-lengths gives exact data not obtainable from length maxima alone. The weak-descent transfer is a reusable structural explanation. An exact self-contained complete spectrum qualifies without an additional downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
