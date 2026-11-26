---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Neither g polynomial has a rational root (only ±1 are possible); both are cubic and the displayed roots lie in (3,4) and (12,13). Squaring their roots twice sends (C,D) to (−6,9) to (18,93) and to (−25,167) to (291,27939), respectively, via (C,D)→(C²−2D,D²−2C). These are exactly the coefficients of the minimal polynomials for eta; the defining cubic for theta has negative discriminant and the substitution for eta preserves the unique real root. Thus gamma^4=eta; Q(eta) has degree three and is contained in Q(gamma), so the fields coincide and gamma is a norm-one unit in the full integer ring. Independently, the g discriminants are −135 and −8416. Shifting either polynomial by x=y+1 gives y³−3y−3 and y³−10y²−22y−12. Dedekind's index criterion excludes 3 in the first case and includes 2 in the second; a further factor of 2 in the second index would give a field discriminant ≡2 mod 4, impossible. There are no other candidate primes. The field discriminants are therefore −135 and −2104, agreeing with the frozen index calculations. In rank one a nonfundamental gamma is a proper power of a unit 1<u≤sqrt(gamma); the cited Artin bound would give |D_K|<56 or <232, contradictory. The rank-one regulator is log gamma as stated. Read the frozen notes, verify.py and its recorded verification_output.txt without executing the uploaded code.

## originality

FAIL

The exact fundamental-unit generators are already tabulated at both discriminants. The cited paper gives the corresponding eta polynomials and square-exception parameters. Taking the reciprocal generators from the exact rows and comparing their fourth-power polynomials with those eta polynomials yields both identities mechanically. No source inspected explicitly prints both fourth-power identities, but the complete exact data already determine them by this direct comparison.

## value

FAIL

The exact exponent is well motivated in the square-exception family, and the proof gives a correct self-contained check of the two cases. But both generators were already supplied by exact tables and the exponents are an immediate polynomial readout. No new structural criterion or unknown instance survives the table comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
