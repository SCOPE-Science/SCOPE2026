---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

If top-two score pair fails JR, a jointly unrepresented group U of size at least n/2 and rival supported on U force n even, every involved score exactly n/2, two identical complementary-support masks and one rival mask, and no score above n/2. Conditional on r half-score candidates their masks are iid uniform over M=binom(n,n/2) half masks; each complementary pair permits occupancy (x,0),(0,y),(1,1), with EGF 2e^z-1+z^2. Coefficient extraction produces the exact formula; for m=3 the three choices times M masks give 3M[p(1-p)]^(3n/2), and uniform tie-break gives 1/3. For fixed even n, a positive probability of every half mask yields conditional bad-event probability tending to one, so P~q^m. Independent exhaustive profiles for (2,3),(2,4),(3,3),(4,3),(4,4) agree with exact occupancy coefficients; all n,m follow analytically.

## originality

PASS

No directly covering theorem after statement-level searches, with residual risks recorded. The surviving claim is not an identified corollary of the compared sources.

## value

PASS

A natural adversarial-tie event in justified representation is quantified for every electorate and candidate count, not merely a small witness. The complementary-mask occupancy EGF, exact three-candidate tie-break law, and fixed-electorate many-candidate scaling supply independently useful distributional information for random approval cultures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
