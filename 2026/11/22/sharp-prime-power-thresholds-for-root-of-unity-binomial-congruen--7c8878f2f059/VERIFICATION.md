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

At n=-1 and m<d=p^r, the root-of-unity average filters the signed elementary symmetric terms of the factors d/i to degrees kt. There are at most p-1 factors of valuation one and all others have valuation at least two, so every term has valuation at least 2kt-(p-1). Congruences for all m at n=-1 therefore hold when r<=L=2t-p+1 and propagate to every integer by Pascal differences and induction on m. For r>L, write j=t-p+1 and c=[p(p-1)+q]p^(r-2) with q as in RESULT.md; t<=c<d. The factors attaining valuations one and two have the counts asserted in the proof. Minimal products in degree t use all p-1 of the former and exactly j of the latter. The normalized valuation-two product consists of p-1 complete blocks of nonzero residues followed by q extra factors. Its complete-block contribution is (1-X^(p-1))^(p-1)=1+X^(p-1) through degree p over F_p. Hence the required coefficient is 1/j! for 2<=j<=p-2, and 1 at both j=p-1 and j=p. The valuation-one normalization is a unit and all degrees >=2t have strictly larger valuation, giving exact valuation L at (n,m)=(-1,c). This is a finite difference of order d-1-c of the top-degree discrepancy, so at least one of the consecutive top-degree inputs from -1 to d-2-c fails. The degree-c valuation is not an asserted top-degree valuation.

## originality

PASS

The new part is failure throughout the p-2 exponents 2t-p+2 through 2t-1. Miska already gives the entire success range and failure beyond that gap; the witness settles the gap and turns the prior bounds into an exact cutoff.

## value

PASS

This closes a gap in a published classification for an infinite, naturally distinguished band, using the first two nontrivial valuation layers and an explicit obstruction. It fixes the exact boundary wherever the existing sufficient bound in this band is used, rather than adding isolated finite tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
