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

On the bounded oval the translation-invariant differential dw/(2Y) has unsigned period J/√(ab). Translating by T=(−ab,0) identifies the oval with the identity component and gives the normalized phase in the record, oriented to increase from T on the upper arc. In the translated group, the odd multiple is unchanged because T has order two. With t=−w, the upper endpoint P of the strict band has phase β/2, and the substitution t=b²v gives the stated integral ratio; its integrand is positive and integrable at the complete-period endpoints, so 0<β<1. Schvöllner Lemma 7.1(3) verifies infinite order under exactly a>b. As an independent check, on the integral model X=ab w, V=abY, duplication gives X(2P)=(a−b)²s²/4 and X(4P)=s²((a−b)^4 s²−16a³b³)²/[16(a−b)²(a²+b²)²]. Any odd prime p dividing a²+b² (one exists and p≥5 for the stated coprime a>b) divides neither ab nor a±b; the bracket is −8a³b³ modulo p. Thus X(4P) is nonintegral at p, still so on the integral short model with X'=9X+3(a²b²+ab s²). Nagell–Lutz rules out torsion. In particular β is irrational. Subtracting β/2 from the target arcs gives fractional parts {kβ} in (1−β,1), except for the interior-point deletion at 1−β/2 (the phase of T); irrationality excludes that point as well as 1−β, and k=0 correctly fails at P. This gives the displayed floor differences, their telescoping prefix count, and k=floor(m/β) at jump m. Consecutive floors of m/β give the stated two gaps. The triple construction can also be checked directly: set m=−w/(bs), y=−bs(w+ab)/Y on the positive branch, x=my, z=(a/b)y. Then y²=((u+1)m−u)/(u m(u+1−m)); u/(u+1)<m<1 gives positivity and z<1 by (m−1)(m+u²)<0. The frozen sample code is an exact rational group-law test paired with numerical quadrature, not an infinite proof or certified interval test, and was not run.

## originality

PASS

The elliptic encoding, canonical point, infinite order, strict window, and generic rotation/mechanical-word relation are all prior. Credit is for the explicit period ratio and alignment giving the zero-intercept exact hit counts and indices for this particular arithmetic orbit.

## value

PASS

For the canonical Δ-triple construction the result replaces a density argument that cannot locate the first successful point by an explicit formula for it and for every successful multiplier. The phase alignment additionally gives a uniform discrepancy smaller than one for all prefixes, not just an asymptotic density. This is useful for finding witnesses on that orbit without asserting a global optimum over rational triples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
