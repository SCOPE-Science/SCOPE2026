---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two order-24 extensions differ by the quadratic character. Square/nonsquare projection gives half the sum and difference of their Gauss sums; the scaled determinant is their nonzero product and a surviving entry has modulus p. The Jacobi–Gauss identity makes the zero condition J=±p. For t a unit mod 24 and b the positive residue of pt, the two digits of (p²−1)t/24 are (pt−b)/24 and (bp−t)/24, so Stickelberger yields the asserted normalized valuation (up to uniform sign convention). The residues 13,17,19,23 give equal valuations for the pair t,t+12 at every conjugate prime, so J/p is integral; it has unit modulus in every embedding. Inversion fixes J under ζ24→ζ24^11, and among roots of unity in this cyclotomic field only ±1 are fixed. In the other four classes t=1 and t=13 have different valuations and cyclotomic conjugacy transfers the obstruction to all extensions. The subfield restrictions for 17 and 19 indeed have orders 4 and 6, and Frobenius does not swap extensions in these classes. Independently evaluated the compressed Fourier zeros directly in the cyclotomic coefficient basis at 20 primes and all four characters per prime (python3 /workspace/branches/reproduce_reviews.py 1); it does not use the supplied checker's Jacobi-sum enumeration and does not replace the valuation proof.

## originality

FAIL

Akiyama's 1996 pure Jacobi-sum theorem explicitly covers both exceptional congruences and yields exactly the two remaining classes at order 24. Garcia–Karaali–Katz's index-two calculation supplies the Fourier consequences without any new mathematical condition. The claimed slice is already covered, even though the compressed-Fourier wording is different.

## value

FAIL

The exceptional residues are a useful example in the Fourier framework, but the record's narrow invariant has no supported additional payoff beyond translating a published exact classification by the existing index-two reduction. It produces neither a new case of purity nor a new Fourier obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
