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

A coefficient-field-fixing unital map is determined by the image of t, necessarily in (t), and all q^3 images are allowed. Formal substitution reverses the order of the corresponding endomorphisms but does not change commutation. Expanding the two compositions gives (a-a^2)v=b(u-u^2) and (a-a^3)w-c(u-u^3)+2bv(u-a)=0. Where both coefficients of v and w are nonzero, each u gives one pair (v,w). At a=-1 in odd characteristic the second equation after eliminating v becomes -(c+b^2)(u-u^3)=0; w is free, giving q^2 or 3q. At a=0,1 in odd characteristic, b nonzero forces u=0 or 1, with v free only for u=a and w always free; b=0 and c nonzero gives three roots and two free coefficients. With b=c=0 these maps are central. In characteristic two the mixed term vanishes and the roots of u^3=u and u^2=u are both {0,1}, so each nonzero (b,c) at a=0,1 gives 2q^2 partners. Counting f in the disjoint strata, taking the first moment and merging coincident exponents at q=2,3 gives the stated polynomial, ordered pair total, probability and center. Independently enumerated q=2,3,4,5,9 by Horner evaluation modulo t^4 using ordinary truncated convolution and comparing both orders for each unordered pair; incremented both centralizer sizes on a match and added self-commutation once per f. Replay using Z/p for prime q, and quadratic bases with x^2+x+1 and x^2+1 for q=4 and 9. The computed histograms matched the formula at all five q; totals were 64, 387, 1216, 2725, 25353. The frozen script and stored counts were inspected, not executed.

## originality

FAIL

The distinct Resultary record on centralizer spectra and a binary commutativity cutoff states the exact same full monoid census. The result is demonstrably covered regardless of which record was derived or posted first; their shared date does not establish priority.

## value

FAIL

A full composition-centralizer census including singular maps and small-characteristic jumps is a natural invariant, but the entire exact census is already available in the matched catalogue finding, and the aggregates are immediate consequences. The frozen record does not supply a distinct unknown invariant or other valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
