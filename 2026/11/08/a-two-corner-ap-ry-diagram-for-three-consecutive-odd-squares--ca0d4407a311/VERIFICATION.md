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

For odd n≥7, gcd(n²,(n+2)²)=1. Verified all three polynomial reduction relations with positive multiples of a=n² and nonnegative coefficients. They strictly reduce any x b + y c from x≥n+2, y≥n+2 or upper-right forbidden rectangle into T_n; termination by decreasing positive weight. T_n has (n+2)²−8(n+1)/2=n² points, and every residue occurs by reducing nonnegative multiples of b; hence distinct minimal Apéry representatives. Its two maximal coordinate corners are (n−7,n+1) and (n+1,(n+1)/2), giving precisely two pseudo-Frobenius numbers; summing rectangle coordinates and applying genus Apéry sum identity gives closed genus. Cubic PF difference changes order after n=11 for odd n. Independently ran Dijkstra minimal representatives and PF/genus for n=7,9,11,13,15,17,19,31,51 and all matched, finite check not used as infinite proof.

## originality

PASS

Best-of-knowledge new complete two-corner Apéry, type-two pseudo-Frobenius and genus classification for the natural family of three consecutive odd squares; previously proved ordinary-consecutive-square families do not mathematically cover it.

## value

PASS

A complete infinite-family Apéry diagram and type/genus/pseudo-Frobenius classification for three consecutive odd square denominations gives a natural exact semigroup invariant. The two-corner picture and sharp Frobenius switching index have independent classification utility, beyond mere calculation of isolated numerical values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
