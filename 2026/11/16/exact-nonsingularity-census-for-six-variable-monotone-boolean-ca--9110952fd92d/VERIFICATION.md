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

For each monotone 6-variable function the cofactor decomposition f=(a,b) with a<=b is bijective. The cofactor Walsh coefficients A±B give all 64 eigenvalues of unnormalized Boolean convolution; full 64-point butterfly appears separately in the inspected verifier. An independently written and compiled exact C++ cofactor enumeration reproduced all 7,828,354 functions, 3,913,460 odd supports (every one gap 1), 3,914,894 even supports, precisely 23,732 even zero-free supports (each gap 2), and all 12 support-size strata. The original C++ checks dimensions 1 through 5 for absence of even nonsingular supports. Integer bounds and bit masks are appropriate; finite exhaustive bijection is sufficient for this finite theorem, not for dimensions >6. Fourier diagonalization gives inverse norms and condition numbers.

## originality

PASS

The 2012 paper proves that some six-variable even supports are nonsingular and describes Walsh/Cayley equivalence; 2016 gives general monotone Walsh formulas; neither inspected statement yields the exact 23,732-class partition, its 12 support-size strata, or sharp first-exception gap. This is not a new Walsh transform or existence theorem. No identical published record was returned by targeted Resultary searches excluding the same newly posted claim; a hidden prior census remains possible.

## value

PASS

The first dimension in which even monotone support can avoid a zero Walsh multiplier is mathematically natural and previously motivated by a constructed exception. A complete exact frequency, support-size distribution and sharp inverse-norm law quantify how exceptional that counterexample is at the first threshold; the invariant is natural and not merely a tiny arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
