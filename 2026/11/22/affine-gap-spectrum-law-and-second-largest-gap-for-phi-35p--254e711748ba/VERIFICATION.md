---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Fresh check of repairs/4/RESULT.md: the claim concerns the second-largest distinct difference between adjacent supported exponents for primes p=35q+r>35. The residue is necessarily a unit. The rational factorization gives the recorded 25 coefficients and the period-35 reciprocal; multiplying by the substituted numerator gives the displayed word on each of the 24 blocks. The last block has length u-23 because the quotient degree is 24(u-1); the leading term guarantees support even if the truncated prefix has fewer than 35 entries. For fixed residue the first supported offset stays fixed and the last moves by 35, so exactly a full cyclic multiset is added internally and cross-block gaps are unchanged. The independent integer reproduction under branches/5935181d-8585-4392-9d90-3a76d6dff600/independent_check.py (invoke full() to reproduce the exhaustive run) derived the coefficient list, generated all 576 base/slope pairs, and verified full quotient and gap agreement for 72 indices. The generated table and summary establish A_24=B_24=2, no intermediate gap in either histogram, and every displayed A_s=a_r and B_s=a_r+b_r. Every B_s is positive, covering even q=1. The known maximum-gap theorem for prime p validates the upper cutoff, independent of whether the composite base quotients are counted as examples. All 24 units are exhausted and the periodic proof, not the 72 spot checks, extends the result to every q. The frozen checker and CSV were inspected rather than executing the uploaded program; the independent table is a numerical reconstruction, not a claim of a bytewise CSV comparison. The repair keeps that checker and CSV as unchanged support. The mathematical conclusion of the original also checks; its failure was not a correctness failure.

## originality

PASS

This verdict is for the repaired claim only. The original's claimed new all-gap affine law fails the originality comparison: two distinct Resultary results cover exactly that law and its cyclic-word coefficients in stronger regimes, and a primary coefficient-block theorem gives the same repetition behind it. The corrected publication files withdraw that originality claim. They state instead the explicit second-largest-gap residue relation and exact multiplicities at base 35, with the maximum and general affine law credited. The strongest located exact classifications, at base 15 or for binary polynomials, do not imply the special distance-to-zero identity at base 35. No dated priority between the two same-day catalogue results and the original is inferred.

## value

PASS

The substantive remainder identifies a natural gap observable immediately below the classical maximum in the first ternary base outside the smallest-prime-three case. This is not merely a fresh table of all frequencies from a known routine: the exact distance-to-zero rule, forbidden interval above it and asymmetric multiplicity data give a sharp next-gap law for an infinite prime series. They provide a concise case against which proposed general ternary second-gap laws can be tested. The correction retains those exact facts and attributes the known affine machinery rather than presenting that substitution as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
