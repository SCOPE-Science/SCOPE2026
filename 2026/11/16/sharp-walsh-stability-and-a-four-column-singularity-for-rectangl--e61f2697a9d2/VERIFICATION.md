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

For binary 3×n matrices with no 2×2 all-ones rectangle, each heavy column of two ones consumes one of the three row pairs; an all-one column consumes all pairs, and no row pair can be consumed twice. This gives an exact partition into at most three distinct pair-labelled heavy columns, or one all-one heavy column, with all other columns light. The signed enumerator formula sums over injective pair-to-column assignments and weighted light A_j=1+σ1+σ2+σ3. Every A_j is even; 3-heavy permanent has six odd terms and hence is even, yielding 2^{n−2} divides all Walsh multipliers for n≥3. Explicit frequency columns [1]*(n−3),3,3,5 yield exactly −2^{n−2}; for n=2 columns [3,3] yield −2. All [3] gives W=0 for n≥4. At n2/3, counts of admissible matrices are N2=54,N3=334 and even coordinate marginals imply each W≡2 mod4, so no zero. Independently generated entire frequency spectra n2,3,4 gave (N,zero,gap,gcd)=(54,0,2,2),(334,0,2,2),(1952,621,4,4), with Parseval exact. Therefore sharp all-n gap and l2 inverse-on-range norms follow; 621 nullity is exhaustive only n4.

## originality

PASS

Bounded semantic Resultary search plus primary-literature comparison finds no earlier theorem dominating the precise full stated claim. Explicit equivalences and narrower covered portions are identified. This is best-of-knowledge, not a guarantee of global novelty. The previously known ingredients and different domains of related results are not claimed new.

## value

PASS

Sharp all-width spectral threshold, dyadic gap, and first singular nullity classify deconvolution for the natural 3×n C4-free incidence codebook. Not just known enumeration or mechanically derived ordinary matrix counts; the heavy-column permanent parity and explicit signed extremizers carry new structural information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
