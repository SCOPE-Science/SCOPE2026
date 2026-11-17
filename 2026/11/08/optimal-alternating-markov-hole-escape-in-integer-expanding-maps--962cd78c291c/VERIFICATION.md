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

For symbolic base-b coding the forbidden holes are cylinders 00 and (b-1)(b-1). The source-proof update A_c maps a vector of ending-symbol counts to V except at the chosen endpoint, where it is V-v_endpoint. Positivity of the linear continuation functionals, plus exchanging endpoints, implies choosing the larger current endpoint count minimizes every remaining horizon and strictly wins if unequal. After the first deletion the opposite endpoint count is uniquely largest; hence unique strict alternation for n>=2. The alternating count satisfies A_(n+2)=b A_(n+1)-A_n, A0=b,A1=b²-1, including the b=2 repeated root and exact b>=3 roots. The fixed-hole characteristic polynomial has larger positive root, proving strict escape-rate advantage. Independent exhaustive enumeration of 2^n schedules for b=2..5 and n=1..7 checked equality and uniqueness; the monotone comparison proves all b,n.

## originality

PASS

The binary base-2 finite-horizon extremizer, optimal count (n+2)/2^(n+1), and uniqueness were published on Nov 2 and are fully prior-covered, not claimed anew. The surviving uniform b>=3 proof has a distinct exact recurrence and root-dependent rate across all integer bases, with strict finite-horizon uniqueness and superiority over either fixed hole.

## value

PASS

A complete optimizer for nonadaptive opening of two symmetric b-ary holes at every finite horizon is an exact controlled dynamical invariant. The transition at b=2 versus b>=3 and improved escape exponent over fixed-hole choices are motivated structural information, even after removing the covered binary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
