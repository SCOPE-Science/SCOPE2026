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

The adjacent-binomial identity and gcd(bn+1,n)=1 settle all odd-prime factors and the cases of odd bn+1. For b,n odd it leaves failure iff the Kummer count in (4n-1)+(bn+1) is at most one. With h the largest positive odd integer at most nu2(b+3), the sum mod 2^h is n. Here is an independent proof of minimality for h>=3: write n_h=1+sum of 2^j over odd j=1,...,h-2. An odd n<n_h has a first missing bit j in that odd chain. The first summand has bit 1 at j (at j=1 directly, otherwise this is the previous odd bit of n), whereas the output bit is 0. A carry-out is forced there, even if an incoming carry exists. If there is only one carry, the next digit j+1 has output 1 and no carry-out; this 1 propagates along the even positions because bit i of 4n-1 agrees with bit i-2 of n for i>=3. Hence n has its bit h-1 set, contradicting n<n_h<2^(h-1). For h=1 the earlier-index claim is vacuous. At n_h the low h bits are disjoint; the high addition is 1+(qn_h-1), q=(b+3)/2^h, with exactly nu2(q)<=1 carries. The distinct thresholds are realized by b=1 and b=2^h-3 for odd h>=3. An independent Euclidean-quotient recurrence also reproduced the frozen 4- and 11-state certificate, its two-step closure, and its acceptance criterion: python /workspace/review-work/check-fourfold.py. That is an exact finite certificate for an unbounded claim, not an extrapolation.

## originality

PASS

The first-failure function, gcd-adjusted divisibility and existence/bounds are prior. In the inspected sources no result gives the arbitrary odd-b least index for a=4 or the unbounded two-adic plateau. The even branch and small overlapping examples are not claimed independently original.

## value

PASS

This is a complete unbounded parameter slice of Sun's naturally defined least-failure function, replacing a general bound with an exact location. The two-adic plateaus and arbitrarily late first failures describe when divisibility first breaks, not only whether it breaks. The earlier-index obstruction is needed and is not supplied by known upper bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
