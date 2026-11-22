---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

A maximal independent set is exactly a cyclic 3/4/5-gap composition; this gives a_n recursion, Z_n=3a_(n-3)+4a_(n-4)+5a_(n-5), and ordered one-site and two-site counts a_n and a_d a_(n-d), hence the stated circulant spectrum. At nonzero Fourier frequency, covariance is a nonnegative squared Fourier coefficient average. In every n>=11 a legal replacement (3,5)↔(4,4) changes one chosen vertex, forcing positive frequency; n=8 also allows it. Explicit small odd cycles and n=10 witness positivity; n=6 has three opposite pairs, leaving odd modes null. The constant mode is |S| variance/n and vanishes exactly if the interval ceil(n/5)..floor(n/3) has one integer, which occurs at 5,6,7,8,11. Independent exhaustive bit-mask enumeration and DFT checked all n=5..14; the gap-slide argument, not this finite enumeration, proves n>=12.

## originality

PASS

The exact isolated eleven-cycle loss of rank for uniform maximal independent sets of square cycles is not implied by published all-dominating-set power-cycle polynomials, ordinary-cycle maximal-independent-set covariance, or general independent domination bounds. Rank and complete Fourier covariance are more specific than configuration counts. Remains a priority risk from an unlocated equivalent cyclic renewal/affine-span theorem.

## value

PASS

An exact all-length covariance and affine-hull rank classification for a natural graph ensemble reveals a nonmonotone isolated n=11 identifiability defect after n=9,10 success. This is a mathematically motivated, nontrivial finite exception with a uniform positivity proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
